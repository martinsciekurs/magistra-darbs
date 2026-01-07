#!/usr/bin/env python3
"""DocGen CLI - Generate documentation for repositories using LangGraph."""

import argparse
import subprocess
import time
from dotenv import load_dotenv
load_dotenv()

from pathlib import Path
from docgen.utils.repo_fetcher import fetch_repo, normalize_repo_name
from docgen.analyzer import CodeParser, SourceFinder, add_call_dependencies, get_documentation_order
from docgen.analyzer.test_mapper import generate_test_mapping_file
from docgen.utils import save_yaml, map_language_name, step, success, info, dim, header
from docgen.utils.logger import setup_logger
from docgen.llm.graph import create_docgen_graph, DocGenState
from docgen.llm.graph.nodes import document_modules_node, synthesize_node
from docgen.llm.client import get_token_usage, reset_token_usage
from docgen.llm.langfuse_client import flush_and_end
from docgen.scripts.init_docusaurus_site import init_docusaurus_site
from docgen.utils.generate_docs import generate_docusaurus_docs

# Set up logger
logger = setup_logger()
from docgen.utils.logger import warning, error
from docgen.utils import load_yaml


def rerun_stages(repo_name: str, stages: list[str]):
    """Re-run specific documentation stages without regenerating everything.

    Args:
        repo_name: Name of the repository (folder in .docs/)
        stages: List of stages to re-run ("modules", "synthesis", "site")
    """
    docs_dir = Path(".docs") / repo_name

    if not docs_dir.exists():
        error(f"Documentation not found for {repo_name}. Run full pipeline first.")
        return False

    if "modules" in stages:
        step("Re-running module documentation")

        # Load required state
        repo_analysis = load_yaml(repo_name, "4_llm_summary.yaml")
        file_docs = load_yaml(repo_name, "9_file_docs.yaml") or []

        # Build minimal state
        state: DocGenState = {
            "repo_name": repo_name,
            "repo_path": str(docs_dir / "repo"),
            "repo_analysis": repo_analysis,
            "file_docs": file_docs,
            "errors": [],
            "force": True,
        }

        # Delete existing file to force regeneration
        module_docs_path = docs_dir / "11_module_docs.yaml"
        if module_docs_path.exists():
            module_docs_path.unlink()
            dim("  Deleted existing 11_module_docs.yaml")

        document_modules_node(state)
        success("  Module documentation regenerated")

    if "synthesis" in stages:
        step("Re-running synthesis documentation")

        # Load required state
        repo_analysis = load_yaml(repo_name, "4_llm_summary.yaml")
        module_docs = load_yaml(repo_name, "11_module_docs.yaml") or []

        # Build minimal state
        state: DocGenState = {
            "repo_name": repo_name,
            "repo_path": str(docs_dir / "repo"),
            "repo_analysis": repo_analysis,
            "module_docs": module_docs,
            "errors": [],
            "force": True,
        }

        # Delete existing file to force regeneration
        synthesis_path = docs_dir / "15_synthesis_doc.yaml"
        if synthesis_path.exists():
            synthesis_path.unlink()
            dim("  Deleted existing 15_synthesis_doc.yaml")

        synthesize_node(state)
        success("  Synthesis documentation regenerated")

    if "site" in stages:
        step("Regenerating Docusaurus site")
        if generate_docusaurus_docs(repo_name):
            success("  Site regenerated")
        else:
            warning("  Failed to regenerate site")

    return True


def extract_functions(code: str, language: str, file_name: str) -> dict:
    """Extract functions from source code."""
    parser = CodeParser(language)
    result = parser.parse_file(code, file_name)
    return {
        "file_name": file_name,
        "imports": result["imports"],
        "functions": result["functions"],
    }


def main():
    """Main entry point using LangGraph pipeline."""
    parser = argparse.ArgumentParser(description="Generate documentation for a repository")
    parser.add_argument("repo", help="Repository URL or local path")
    parser.add_argument(
        "--start-server",
        action="store_true",
        help="Automatically start Docusaurus dev server after generating docs"
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Force regeneration of all documentation, ignoring caches and checkpoints"
    )
    parser.add_argument(
        "--commit",
        type=str,
        default=None,
        help="Specific commit SHA, tag, or branch to checkout (fetches full history)"
    )
    parser.add_argument(
        "--rerun",
        nargs="+",
        choices=["modules", "synthesis", "site"],
        default=None,
        help="Re-run specific stages without regenerating everything (e.g., --rerun modules synthesis site)"
    )
    args = parser.parse_args()

    # Reset token usage tracking and time
    reset_token_usage()
    start_time = time.time()

    # Handle --rerun mode (partial regeneration)
    if args.rerun:
        repo_name = normalize_repo_name(args.repo)
        header(f"Re-running stages for {repo_name}: {', '.join(args.rerun)}")
        if rerun_stages(repo_name, args.rerun):
            success(f"Done! Re-ran stages: {', '.join(args.rerun)}")
        flush_and_end()
        return

    # Fetch repository
    repo_path, repo_name = fetch_repo(args.repo, commit=args.commit)

    # Find source files grouped by language
    step("Analyzing repository")
    source_finder = SourceFinder(repo_path)
    files_by_language = source_finder.files_by_language

    if files_by_language:
        lang_summary = ", ".join([f"{lang}: {len(files)} files" for lang, files in files_by_language.items()])
        dim(f"  {lang_summary}")
    else:
        info("Could not detect languages (not a Git repository or no committed files)")

    # 1. Save file tree
    all_files = []
    for files in files_by_language.values():
        all_files.extend(files)
    file_tree = [f"{repo_name}/{f}" for f in sorted(all_files)]
    save_yaml(repo_name, "1_file_tree.yaml", file_tree, plain_text=True)

    # 2. Save node extraction
    extracted_code_elements = []
    repo_path_obj = Path(repo_path)
    
    for linguist_lang, files in files_by_language.items():
        parser_lang = map_language_name(linguist_lang)
        if parser_lang is None:
            dim(f"  Skipping {linguist_lang} - not supported")
            continue
        
        for file_path in files:
            full_path = repo_path_obj / file_path
            if not full_path.exists():
                warning(f"File not found: {full_path}")
                continue
            
            try:
                with open(full_path, 'r', encoding='utf-8') as f:
                    code = f.read()
                result = extract_functions(code, parser_lang, file_path)
                extracted_code_elements.append(result)
            except Exception as e:
                error(f"Error processing {file_path}: {e}")
                continue
    
    # Add call dependencies (who calls whom)
    extracted_code_elements = add_call_dependencies(extracted_code_elements)
    save_yaml(repo_name, "2_node_extraction.yaml", extracted_code_elements)

    # 3. Topological sort for documentation order
    doc_order = get_documentation_order(extracted_code_elements)
    save_yaml(repo_name, "3_doc_order.yaml", doc_order)
    dim(f"  Found {len(doc_order)} functions to document")

    # 3b. Generate test mapping for code examples
    from docgen.utils.config import ENABLE_CODE_EXAMPLES
    if ENABLE_CODE_EXAMPLES:
        test_mapping = generate_test_mapping_file(repo_name, repo_path_obj)
        if test_mapping:
            dim(f"  Found tests for {len(test_mapping)} functions")
        else:
            dim(f"  No test files found")

    # Create and run LangGraph pipeline with checkpointing
    header("LangGraph Documentation Pipeline")
    
    # If force is enabled, delete checkpoint database to start fresh
    if args.force:
        checkpoint_path = Path(".docs") / repo_name / "checkpoints" / "checkpoints.db"
        if checkpoint_path.exists():
            step("Force mode: clearing checkpoints")
            checkpoint_path.unlink()
            dim(f"  Deleted checkpoint database")
    
    graph = create_docgen_graph(repo_name=repo_name)
    
    # Run the graph with thread_id for checkpointing
    # Using the same thread_id will automatically resume from last checkpoint if program crashed
    config = {"configurable": {"thread_id": f"{repo_name}-docgen"}}
    
    # Check if there's an existing checkpoint to resume from (skip if force is enabled)
    initial_state: DocGenState = {
        "repo_path": str(repo_path),
        "repo_name": repo_name,
        "errors": [],
        "force": args.force,
    }
    
    if args.force:
        # Force mode: always start fresh, ignore checkpoints
        dim("  Force mode: starting fresh (ignoring checkpoints)")
        result = graph.invoke(initial_state, config)
    else:
        try:
            existing_state = graph.get_state(config)
            if existing_state and existing_state.next:
                # Resume from checkpoint - pass None to use checkpointed state
                dim(f"  Resuming from checkpoint: next nodes {existing_state.next}")
                result = graph.invoke(None, config)
            else:
                # No checkpoint or execution completed - start fresh
                result = graph.invoke(initial_state, config)
        except Exception:
            # No checkpoint exists - start fresh
            result = graph.invoke(initial_state, config)
    
    # Report errors if any
    if result.get("errors"):
        warning("Errors encountered:")
        for err in result["errors"]:
            dim(f"  {err}")
    
    header("Pipeline Complete")
    
    # 13. Initialize Docusaurus site if not present (or if force is enabled)
    site_dir = Path('.docs') / repo_name / 'site'
    if args.force and site_dir.exists():
        step("Force mode: re-initializing Docusaurus site")
        import shutil
        shutil.rmtree(site_dir)
        init_docusaurus_site(repo_name)
    elif not site_dir.exists():
        step("Initializing Docusaurus site")
        init_docusaurus_site(repo_name)
    else:
        dim(f"  Docusaurus site already exists")
    
    # 14. Generate Docusaurus markdown files from YAML docs
    step("Generating Docusaurus markdown files")
    if generate_docusaurus_docs(repo_name):
        success("Docusaurus markdown files generated")
    else:
        warning("Failed to generate Docusaurus markdown files")
    
    # Calculate elapsed time
    elapsed_time = time.time() - start_time
    
    # Get token usage
    usage = get_token_usage()
    
    # Print statistics
    header("Statistics")
    total_calls = usage["llm"]["calls"] + usage["embeddings"]["calls"]
    if total_calls > 0:
        info(f"Token Usage:")
        
        # LLM tokens
        if usage["llm"]["calls"] > 0:
            dim(f"  LLM:")
            dim(f"    Prompt tokens: {usage['llm']['prompt_tokens']:,}")
            dim(f"    Completion tokens: {usage['llm']['completion_tokens']:,}")
            dim(f"    Total tokens: {usage['llm']['total_tokens']:,}")
            dim(f"    Calls: {usage['llm']['calls']}")
        
        # Embedding tokens
        if usage["embeddings"]["calls"] > 0:
            dim(f"  Embeddings:")
            dim(f"    Tokens: {usage['embeddings']['tokens']:,}")
            dim(f"    Calls: {usage['embeddings']['calls']}")
        
        # Grand total
        grand_total = usage["llm"]["total_tokens"] + usage["embeddings"]["tokens"]
        dim(f"  Grand total: {grand_total:,} tokens ({total_calls} calls)")
    else:
        dim("  No token usage tracked (may be using Ollama or no API calls made)")
    
    # Log time
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    if minutes > 0:
        info(f"Total time: {minutes}m {seconds}s")
    else:
        info(f"Total time: {seconds}s")
    
    success(f"Documentation generated in .docs/{repo_name}/")
    
    # 15. Optionally start Docusaurus dev server
    if args.start_server:
        step("Starting Docusaurus dev server")
        try:
            # Check if npm is available
            subprocess.run(['npm', '--version'], check=True, capture_output=True)
            
            # Check if node_modules exists, if not run npm install
            if not (site_dir / 'node_modules').exists():
                dim("  Installing dependencies...")
                subprocess.run(['npm', 'install'], cwd=site_dir, check=True)
            
            dim(f"  Starting dev server at http://localhost:3000")
            dim(f"  Press Ctrl+C to stop the server")
            # Start the server (this will block)
            subprocess.run(['npm', 'start'], cwd=site_dir, check=True)
        except subprocess.CalledProcessError as e:
            error(f"Failed to start dev server: {e}")
            info(f"  You can start it manually: cd {site_dir} && npm start")
        except FileNotFoundError:
            error("npm not found. Please install Node.js and npm, then run:")
            info(f"  cd {site_dir} && npm install && npm start")
    else:
        info(f"To start the dev server, run: cd {site_dir} && npm start")
    
    # Flush Langfuse data if enabled
    flush_and_end()

if __name__ == "__main__":
    main()
