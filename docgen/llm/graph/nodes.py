"""LangGraph nodes for the DocGen documentation pipeline.

Each node wraps existing logic from main.py with:
1. Load existing docs from YAML (for resume)
2. Process only new items
3. Save after each item (crash recovery)
4. Return updated state
"""

import re
import yaml
from pathlib import Path

from docgen.llm.graph.state import DocGenState
from docgen.llm.client import call_llm
from docgen.llm.structured_client import call_llm_structured
from docgen.llm.schemas import (
    RepoAnalysis,
    RepoAnalysisEvaluation,
    Docstring,
    SynthesisDoc,
    ConfidenceScore,
    DocstringEvaluation,
    SynthesisEvaluation,
    ProposedTOC,
    DynamicSynthesisDoc,
    CodeExample,
    CodeExampleValidation,
    ArchitectureDiagram,
)
from docgen.llm.prompts import (
    get_repo_analysis_prompt,
    get_reflection_evaluation_prompt,
    get_reflection_regeneration_prompt,
    get_function_doc_prompt,
    get_class_doc_prompt,
    get_file_doc_prompt,
    get_module_doc_prompt,
    get_synthesis_doc_prompt,
    get_docstring_evaluation_prompt,
    get_docstring_regeneration_prompt,
    get_synthesis_evaluation_prompt,
    get_synthesis_regeneration_prompt,
    get_toc_proposal_prompt,
    get_toc_refinement_prompt,
    get_dynamic_synthesis_prompt,
    get_code_example_prompt_with_tests,
    get_code_example_prompt_from_code,
    get_code_example_validation_prompt,
    get_code_example_retry_prompt,
    get_architecture_diagram_prompt,
)
from docgen.llm.doc_generator import (
    load_repo_analysis,
    _build_function_lookup,
    _get_file_imports,
    _get_dependency_docs,
    _get_similar_function_docs,
    _extract_signature_from_code,
    _format_imports,
    _format_called_by,
    _group_functions_by_class,
    extract_relevant_file_context,
    _extract_usage_snippets,
)
from docgen.llm import init_chroma, embed_functions, get_similar
from docgen.utils import save_yaml
from docgen.utils.logger import setup_logger, step, success, dim, warning, error, info
from docgen.llm.validation import (
    validate_repo_analysis_yaml,
    validate_docstring,
    validate_code_example_syntax,
    validate_code_example_basic,
)
from docgen.utils.config import (
    ENABLE_EMBEDDINGS,
    HITL_CONFIDENCE_THRESHOLD,
    REFLECTION_CONFIDENCE_THRESHOLD,
    MAX_REFLECTION_ITERATIONS,
    ENABLE_TOC_HITL,
    ENABLE_CODE_EXAMPLES,
    CODE_EXAMPLE_MAX_RETRIES,
)
from docgen.analyzer import MarkdownFinder
from docgen.analyzer.test_mapper import load_test_mapping

logger = setup_logger()


def _load_repo_analysis_with_retry(repo_name: str, max_retries: int = 2) -> tuple[str | None, str | None]:
    """Load repo analysis with retry logic.
    
    Args:
        repo_name: Name of the repository
        max_retries: Maximum number of attempts (default: 2)
        
    Returns:
        Tuple of (repo_analysis, error_message). If successful, error_message is None.
        If failed after retries, repo_analysis is None and error_message contains the error.
    """
    last_error = None
    for attempt in range(max_retries):
        try:
            repo_analysis = load_repo_analysis(repo_name)
            if repo_analysis and repo_analysis.strip():
                return repo_analysis, None
            last_error = "Repository analysis is empty"
        except Exception as e:
            last_error = str(e)
            if attempt < max_retries - 1:
                dim(f"  Retry {attempt + 1}/{max_retries}: Failed to load repo analysis, retrying...")
    
    return None, f"Failed to load repository analysis after {max_retries} attempts: {last_error}"


def _synthesis_doc_to_yaml(synthesis: SynthesisDoc) -> str:
    """Convert SynthesisDoc Pydantic model to YAML string for file storage."""
    data = {
        "introduction": synthesis.introduction,
        "why": synthesis.why,
        "quick_start": synthesis.quick_start,
        "architecture": synthesis.architecture,
        "key_concepts": synthesis.key_concepts,
        "how_to_guides": [
            {
                "title": guide.title,
                "content": guide.content,
            }
            for guide in synthesis.how_to_guides
        ],
    }
    return yaml.dump(data, default_flow_style=False, allow_unicode=True, sort_keys=False)


def _repair_docstring_with_llm(original: str, issues: list[str], *, repo_name: str, node_id: str) -> str:
    """Repair a docstring that has validation issues using structured output."""
    prompt = f"""The docstring below has issues. Rewrite it to fix them.

Constraints:
- Output ONLY the docstring (plain text). No backticks. No code fences.
- Keep it concise and faithful to the provided function.

Issues:
{chr(10).join('- ' + e for e in issues)}

Docstring to fix:
{original}
"""
    result = call_llm_structured(
        prompt,
        Docstring,
        generation_name="docstring_repair",
        metadata={"repo_name": repo_name, "phase": "docstring_repair", "node_id": node_id},
    )
    return result.docstring.strip()


def _generate_docstring_with_reflection(
    original_prompt: str,
    context: str,
    doc_type: str,
    repo_name: str,
    metadata: dict,
    *,
    max_iterations: int = MAX_REFLECTION_ITERATIONS,
    confidence_threshold: int = REFLECTION_CONFIDENCE_THRESHOLD
) -> str:
    """Generate a docstring with reflection loop (evaluate and improve).
    
    Args:
        original_prompt: The base prompt used for generation
        context: The code/context being documented
        doc_type: Type of docstring ("function", "class", "file", "module")
        repo_name: Repository name for metadata
        metadata: Metadata dict for LLM calls
        max_iterations: Maximum number of reflection iterations
        confidence_threshold: Minimum score to accept (default: REFLECTION_CONFIDENCE_THRESHOLD)
    
    Returns:
        The final docstring after reflection
    """
    docstring = ""
    previous_feedback = ""
    
    for iteration in range(1, max_iterations + 1):
        # Generate docstring
        if iteration == 1:
            prompt = original_prompt
            generation_name = f"{doc_type}_doc"
        else:
            # Extract suggestions from previous feedback
            suggestions = []
            if previous_feedback:
                lines = previous_feedback.split("\n")
                current_section = None
                for line in lines:
                    if "Suggestions:" in line or "suggestions:" in line.lower():
                        current_section = "suggestions"
                        continue
                    elif line.strip().startswith("-"):
                        if current_section == "suggestions":
                            suggestions.append(line.strip()[1:].strip())
            
            prompt = get_docstring_regeneration_prompt(
                original_prompt=original_prompt,
                previous_docstring=docstring,
                evaluation_feedback=previous_feedback,
                suggestions=suggestions,
                context=context
            )
            generation_name = f"{doc_type}_doc_iteration_{iteration}"
        
        result = call_llm_structured(
            prompt,
            Docstring,
            generation_name=generation_name,
            metadata={**metadata, "iteration": iteration},
        )
        docstring = result.docstring.strip()
        if not docstring:
            docstring = f"# TODO: Document this {doc_type}"
        
        # Evaluate the docstring
        evaluation_prompt = get_docstring_evaluation_prompt(
            docstring=docstring,
            doc_type=doc_type,
            context=context,
            original_prompt=original_prompt,
            iteration=iteration,
            previous_feedback=previous_feedback
        )
        
        evaluation = call_llm_structured(
            evaluation_prompt,
            DocstringEvaluation,
            generation_name=f"{doc_type}_doc_evaluation_iteration_{iteration}",
            metadata={**metadata, "phase": f"{doc_type}_doc_evaluation", "iteration": iteration},
        )

        overall_score = evaluation.overall_score

        # Build feedback text for next iteration
        feedback_parts = []
        feedback_parts.append("## Evaluation Results\n")
        feedback_parts.append(f"Overall Score: {overall_score}/100\n")
        feedback_parts.append("## Rubric Scores (D1-D6)\n")
        feedback_parts.append(f"- D1 Clarity: {evaluation.clarity.score}/100 - {evaluation.clarity.feedback}")
        feedback_parts.append(f"- D2 Actuality: {evaluation.actuality.score}/100 - {evaluation.actuality.feedback}")
        feedback_parts.append(f"- D3 Structure: {evaluation.structure.score}/100 - {evaluation.structure.feedback}")
        feedback_parts.append(f"- D4 Conciseness: {evaluation.conciseness.score}/100 - {evaluation.conciseness.feedback}")
        feedback_parts.append(f"- D5 Precision: {evaluation.precision.score}/100 - {evaluation.precision.feedback}")
        feedback_parts.append(f"- D6 Consistency: {evaluation.consistency.score}/100 - {evaluation.consistency.feedback}")
        
        if evaluation.suggestions:
            feedback_parts.append("\n## Suggestions:\n")
            for suggestion in evaluation.suggestions:
                feedback_parts.append(f"- {suggestion}")
        
        previous_feedback = "\n".join(feedback_parts)
        
        # Check if acceptable
        if overall_score >= confidence_threshold:
            if iteration > 1:
                dim(f"    ✓ Docstring improved (score: {overall_score}/100)")
            break
        
        # If not acceptable and not last iteration, continue
        if iteration < max_iterations:
            dim(f"    ~ Docstring score {overall_score}/100, regenerating (iteration {iteration + 1}/{max_iterations})")
        else:
            dim(f"    ~ Docstring score {overall_score}/100 (max iterations reached)")
    
    return docstring


def _generate_synthesis_with_reflection(
    original_prompt: str,
    repo_analysis: str,
    module_docs: list[dict],
    file_tree: str,
    existing_docs: str,
    repo_name: str,
    *,
    max_iterations: int = MAX_REFLECTION_ITERATIONS,
    confidence_threshold: int = REFLECTION_CONFIDENCE_THRESHOLD
) -> SynthesisDoc:
    """Generate synthesis documentation with reflection loop (evaluate and improve).
    
    Args:
        original_prompt: The base prompt used for generation
        repo_analysis: Repository analysis YAML
        module_docs: List of module documentation dicts
        file_tree: File tree listing
        existing_docs: Existing markdown documentation
        repo_name: Repository name for metadata
        max_iterations: Maximum number of reflection iterations
        confidence_threshold: Minimum score to accept (default: REFLECTION_CONFIDENCE_THRESHOLD)
    
    Returns:
        The final synthesis documentation after reflection
    """
    synthesis = None
    previous_feedback = ""
    
    for iteration in range(1, max_iterations + 1):
        # Generate synthesis
        if iteration == 1:
            prompt = original_prompt
            generation_name = "synthesis"
        else:
            # Extract suggestions from previous feedback
            suggestions = []
            if previous_feedback:
                lines = previous_feedback.split("\n")
                current_section = None
                for line in lines:
                    if "Suggestions:" in line or "suggestions:" in line.lower():
                        current_section = "suggestions"
                        continue
                    elif line.strip().startswith("-"):
                        if current_section == "suggestions":
                            suggestions.append(line.strip()[1:].strip())
            
            prompt = get_synthesis_regeneration_prompt(
                original_prompt=original_prompt,
                previous_synthesis=synthesis,
                evaluation_feedback=previous_feedback,
                suggestions=suggestions,
                repo_analysis=repo_analysis,
                module_docs=module_docs,
                file_tree=file_tree,
                existing_docs=existing_docs
            )
            generation_name = f"synthesis_iteration_{iteration}"
        
        synthesis = call_llm_structured(
            prompt,
            SynthesisDoc,
            generation_name=generation_name,
            metadata={"repo_name": repo_name, "phase": "synthesis", "iteration": iteration},
        )
        
        # Evaluate the synthesis
        evaluation_prompt = get_synthesis_evaluation_prompt(
            synthesis=synthesis,
            repo_analysis=repo_analysis,
            module_docs=module_docs,
            file_tree=file_tree,
            original_prompt=original_prompt,
            iteration=iteration,
            previous_feedback=previous_feedback
        )
        
        evaluation = call_llm_structured(
            evaluation_prompt,
            SynthesisEvaluation,
            generation_name=f"synthesis_evaluation_iteration_{iteration}",
            metadata={"repo_name": repo_name, "phase": "synthesis_evaluation", "iteration": iteration},
        )

        overall_score = evaluation.overall_score

        # Build feedback text for next iteration
        feedback_parts = []
        feedback_parts.append("## Evaluation Results\n")
        feedback_parts.append(f"Overall Score: {overall_score}/100\n")
        feedback_parts.append("## Rubric Scores (S1-S6)\n")
        feedback_parts.append(f"- S1 Clarity: {evaluation.clarity.score}/100 - {evaluation.clarity.feedback}")
        feedback_parts.append(f"- S2 Actuality: {evaluation.actuality.score}/100 - {evaluation.actuality.feedback}")
        feedback_parts.append(f"- S3 Findability: {evaluation.findability.score}/100 - {evaluation.findability.feedback}")
        feedback_parts.append(f"- S4 Usefulness: {evaluation.usefulness.score}/100 - {evaluation.usefulness.feedback}")
        feedback_parts.append(f"- S5 Precision: {evaluation.precision.score}/100 - {evaluation.precision.feedback}")
        feedback_parts.append(f"- S6 Consistency: {evaluation.consistency.score}/100 - {evaluation.consistency.feedback}")
        
        if evaluation.suggestions:
            feedback_parts.append("\n## Suggestions:\n")
            for suggestion in evaluation.suggestions:
                feedback_parts.append(f"- {suggestion}")
        
        previous_feedback = "\n".join(feedback_parts)
        
        # Display evaluation results
        if iteration == 1:
            info(f"  Synthesis evaluation (iteration {iteration}): {overall_score}/100")
        else:
            info(f"  Synthesis evaluation (iteration {iteration}): {overall_score}/100")
        
        # Check if acceptable
        if overall_score >= confidence_threshold:
            if iteration > 1:
                success(f"Synthesis improved (score: {overall_score}/100)")
            break
        
        # If not acceptable and not last iteration, continue
        if iteration < max_iterations:
            dim(f"  ~ Synthesis score {overall_score}/100, regenerating (iteration {iteration + 1}/{max_iterations})")
        else:
            dim(f"  ~ Synthesis score {overall_score}/100 (max iterations reached)")
    
    return synthesis


def _validate_files_exist(analysis: RepoAnalysis, repo_path: str) -> list[str]:
    """Validate that all files mentioned in the analysis actually exist.
    
    Args:
        analysis: The repository analysis to validate
        repo_path: Path to the repository root
    
    Returns:
        List of missing file paths
    """
    if not repo_path:
        return []
    
    repo_path_obj = Path(repo_path)
    missing_files = []
    
    # Check files in modules
    for module in analysis.modules:
        for file_path in module.files:
            # Normalize path (remove leading repo name if present)
            normalized_path = file_path
            if "/" in file_path:
                parts = file_path.split("/", 1)
                if len(parts) > 1:
                    normalized_path = parts[1]
            
            full_path = repo_path_obj / normalized_path
            if not full_path.exists():
                missing_files.append(file_path)
    
    return missing_files


def _repo_analysis_to_yaml(analysis: RepoAnalysis) -> str:
    """Convert RepoAnalysis Pydantic model to YAML string for file storage."""
    summary_text = f"""Repository Purpose: {analysis.summary.purpose}
Tech Stack: {', '.join(analysis.summary.tech_stack.languages + analysis.summary.tech_stack.frameworks)}"""
    
    data = {
        "summary": summary_text,
        "modules": [
            {
                "name": m.name,
                "description": m.description,
                "files": m.files,
            }
            for m in analysis.modules
        ],
    }
    return yaml.dump(data, default_flow_style=False, allow_unicode=True, sort_keys=False)


def generate_repo_analysis_node(state: DocGenState) -> dict:
    """Generate or regenerate repository analysis from file tree using structured output.
    
    On first iteration: generates fresh analysis.
    On subsequent iterations: regenerates based on evaluation feedback.
    
    Saves: 4_llm_summary.yaml (only on final accepted result)
    """
    repo_name = state["repo_name"]
    repo_path = state.get("repo_path", "")
    iteration = state.get("reflection_iteration", 0) + 1  # Increment iteration
    previous_feedback = state.get("reflection_feedback", "")
    
    llm_summary_path = Path(".docs") / repo_name / "4_llm_summary.yaml"
    reflection_history = state.get("reflection_history", [])
    force = state.get("force", False)
    
    # Only check cache on very first run (no reflection history) and if not forcing
    if not force and iteration == 1 and not reflection_history and llm_summary_path.exists():
        cached = llm_summary_path.read_text(encoding="utf-8")
        ok, errors, _ = validate_repo_analysis_yaml(cached)
        if ok:
            dim("  Repository analysis (cached)")
            # Still need to evaluate it, so continue to evaluation node
            return {"reflection_iteration": iteration}
        else:
            dim("  Cached repo analysis invalid; regenerating")
    
    try:
        file_tree_path = Path(".docs") / repo_name / "1_file_tree.yaml"
        file_tree = file_tree_path.read_text(encoding="utf-8")
        
        # Load existing markdown documentation for context
        existing_docs = ""
        if repo_path:
            md_finder = MarkdownFinder(repo_path)
            existing_docs = md_finder.get_markdown_summary()
            if existing_docs:
                dim(f"  Including {len(md_finder.find_markdown_files())} markdown file(s) as context")
        
        # Determine if this is a regeneration or initial generation
        if iteration == 1:
            step(f"Generating repository analysis (iteration {iteration}/{MAX_REFLECTION_ITERATIONS})")
            prompt = get_repo_analysis_prompt(file_tree=file_tree, existing_docs=existing_docs)
            generation_name = "repo_analysis"
        else:
            step(f"Regenerating repository analysis (iteration {iteration}/{MAX_REFLECTION_ITERATIONS})")
            # Load previous analysis for regeneration
            previous_analysis = ""
            if llm_summary_path.exists():
                previous_analysis = llm_summary_path.read_text(encoding="utf-8")
            
            # Extract suggestions from previous feedback
            # Parse from reflection_feedback (stored as formatted text)
            suggestions = []
            if previous_feedback:
                # Simple parsing - look for "Suggestions:" section
                lines = previous_feedback.split("\n")
                current_section = None
                for line in lines:
                    if "Suggestions:" in line or "suggestions:" in line.lower():
                        current_section = "suggestions"
                        continue
                    elif line.strip().startswith("-"):
                        if current_section == "suggestions":
                            suggestions.append(line.strip()[1:].strip())
            
            prompt = get_reflection_regeneration_prompt(
                file_tree=file_tree,
                previous_analysis=previous_analysis,
                evaluation_feedback=previous_feedback,
                suggestions=suggestions,
                existing_docs=existing_docs
            )
            generation_name = f"repo_analysis_iteration_{iteration}"
        
        # Use structured output - no YAML parsing or repair needed
        analysis = call_llm_structured(
            prompt,
            RepoAnalysis,
            generation_name=generation_name,
            metadata={"repo_name": repo_name, "phase": "repo_analysis", "iteration": iteration},
        )
        
        # Validate files exist
        missing_files = _validate_files_exist(analysis, repo_path)
        if missing_files:
            warning(f"  Warning: {len(missing_files)} file(s) mentioned in analysis do not exist:")
            for missing_file in missing_files[:5]:  # Show first 5
                dim(f"    - {missing_file}")
            if len(missing_files) > 5:
                dim(f"    ... and {len(missing_files) - 5} more")
        
        # Convert to YAML for temporary storage (will be saved permanently only if accepted)
        repo_analysis = _repo_analysis_to_yaml(analysis)
        
        # Save this iteration to a separate file for reference
        iteration_file = Path(".docs") / repo_name / f"4_llm_summary_iter{iteration}.yaml"
        save_yaml(repo_name, f"4_llm_summary_iter{iteration}.yaml", [repo_analysis], plain_text=True)
        
        # Also save to main file (will be kept if evaluation passes)
        save_yaml(repo_name, "4_llm_summary.yaml", [repo_analysis], plain_text=True)
        
        # Display the analysis for this iteration
        info("")
        info(f"Repository Analysis (Iteration {iteration}):")
        print("=" * 80)
        print(repo_analysis)
        print("=" * 80)
        info("")
        
        if iteration == 1:
            success("Repository analysis generated")
        else:
            success(f"Repository analysis regenerated (iteration {iteration})")
        
        return {
            "reflection_iteration": iteration
        }
        
    except Exception as e:
        error(f"  Repository analysis failed: {e}")
        return {
            "errors": [f"Repo analysis failed: {e}"],
            "confidence_score": 0,
        }


def evaluate_repo_analysis_node(state: DocGenState) -> dict:
    """Evaluate repository analysis against rubric using structured output.
    
    Returns evaluation with scores, feedback, and whether to continue iterating.
    """
    repo_name = state["repo_name"]
    iteration = state.get("reflection_iteration", 1)
    previous_feedback = state.get("reflection_feedback", "")
    
    llm_summary_path = Path(".docs") / repo_name / "4_llm_summary.yaml"
    
    if not llm_summary_path.exists():
        error("  No repository analysis to evaluate")
        return {
            "errors": ["No repository analysis found"],
            "confidence_score": 0,
        }
    
    try:
        repo_analysis = llm_summary_path.read_text(encoding="utf-8")
        file_tree_path = Path(".docs") / repo_name / "1_file_tree.yaml"
        file_tree = file_tree_path.read_text(encoding="utf-8")
        
        # Validate files exist (check YAML directly)
        repo_path = state.get("repo_path", "")
        if repo_path:
            try:
                analysis_data = yaml.safe_load(repo_analysis)
                repo_path_obj = Path(repo_path)
                missing_files = []
                
                # Check files in modules
                for module in analysis_data.get("modules", []):
                    for file_path in module.get("files", []):
                        # Normalize path (remove leading repo name if present)
                        normalized_path = file_path
                        if "/" in file_path:
                            parts = file_path.split("/", 1)
                            if len(parts) > 1:
                                normalized_path = parts[1]
                        
                        full_path = repo_path_obj / normalized_path
                        if not full_path.exists():
                            missing_files.append(file_path)
                
                # Check summary for infrastructure files (parse from summary text)
                summary_text = analysis_data.get("summary", "")
                if "Infrastructure:" in summary_text:
                    # Extract infrastructure files from summary
                    infra_section = summary_text.split("Infrastructure:")[1].split("\n")[0].strip()
                    for infra_file in infra_section.split(","):
                        infra_file = infra_file.strip()
                        if infra_file:
                            normalized_path = infra_file
                            if "/" in infra_file:
                                parts = infra_file.split("/", 1)
                                if len(parts) > 1:
                                    normalized_path = parts[1]
                            full_path = repo_path_obj / normalized_path
                            if not full_path.exists():
                                missing_files.append(infra_file)
                
                if missing_files:
                    warning(f"  Warning: {len(missing_files)} file(s) in analysis do not exist:")
                    for missing_file in missing_files[:5]:  # Show first 5
                        dim(f"    - {missing_file}")
                    if len(missing_files) > 5:
                        dim(f"    ... and {len(missing_files) - 5} more")
            except Exception as e:
                dim(f"  Could not validate file existence: {e}")
        
        step("Evaluating analysis...")
        
        evaluation_prompt = get_reflection_evaluation_prompt(
            repo_analysis=repo_analysis,
            file_tree=file_tree,
            iteration=iteration,
            previous_feedback=previous_feedback
        )
        
        evaluation = call_llm_structured(
            evaluation_prompt,
            RepoAnalysisEvaluation,
            generation_name=f"repo_analysis_evaluation_iteration_{iteration}",
            metadata={"repo_name": repo_name, "phase": "repo_analysis_evaluation", "iteration": iteration},
        )
        
        # Display rubric scores
        info(f"  Readability:          {evaluation.readability.score}/100 {'✓' if evaluation.readability.score >= 70 else '✗'}")
        info(f"  Component Allocation: {evaluation.component_allocation.score}/100 {'✓' if evaluation.component_allocation.score >= 70 else '✗'}")
        info(f"  No Duplicates:        {evaluation.no_duplicates.score}/100 {'✓' if evaluation.no_duplicates.score >= 70 else '✗'}")
        info(f"  Completeness:         {evaluation.completeness.score}/100 {'✓' if evaluation.completeness.score >= 70 else '~'}")
        info(f"  File Coverage:         {evaluation.file_coverage.score}/100 {'✓' if evaluation.file_coverage.score >= 70 else '✗'}")
        info("")
        
        overall_score = evaluation.overall_score
        
        # Build feedback text for next iteration
        feedback_parts = []
        feedback_parts.append("## Evaluation Results\n")
        feedback_parts.append(f"Overall Score: {overall_score}/100\n")
        feedback_parts.append("## Rubric Scores\n")
        feedback_parts.append(f"- Readability: {evaluation.readability.score}/100 - {evaluation.readability.feedback}")
        feedback_parts.append(f"- Component Allocation: {evaluation.component_allocation.score}/100 - {evaluation.component_allocation.feedback}")
        feedback_parts.append(f"- No Duplicates: {evaluation.no_duplicates.score}/100 - {evaluation.no_duplicates.feedback}")
        feedback_parts.append(f"- Completeness: {evaluation.completeness.score}/100 - {evaluation.completeness.feedback}")
        feedback_parts.append(f"- File Coverage: {evaluation.file_coverage.score}/100 - {evaluation.file_coverage.feedback}")
        
        if evaluation.suggestions:
            feedback_parts.append("\n## Suggestions:\n")
            for suggestion in evaluation.suggestions:
                feedback_parts.append(f"- {suggestion}")
        
        feedback_text = "\n".join(feedback_parts)
        
        # Display detailed feedback in console
        info("")
        info("Evaluation Feedback:")
        print("=" * 80)
        print(feedback_text)
        print("=" * 80)
        info("")
        
        # Determine if acceptable based on overall_score
        is_acceptable = overall_score >= REFLECTION_CONFIDENCE_THRESHOLD
        
        if is_acceptable:
            success(f"Overall Score: {overall_score}/100 ✓")
            info("  Repository analysis acceptable")
        else:
            if overall_score >= REFLECTION_CONFIDENCE_THRESHOLD:
                dim(f"Overall Score: {overall_score}/100 (above threshold {REFLECTION_CONFIDENCE_THRESHOLD})")
            else:
                warning(f"Overall Score: {overall_score}/100 (below threshold {REFLECTION_CONFIDENCE_THRESHOLD})")
            
            if iteration < MAX_REFLECTION_ITERATIONS:
                info(f"  Will regenerate (iteration {iteration + 1}/{MAX_REFLECTION_ITERATIONS})")
            else:
                info("  Maximum iterations reached")
        
        # Update reflection history
        history_entry = {
            "iteration": iteration,
            "overall_score": overall_score,
            "is_acceptable": is_acceptable,
            "rubric_scores": {
                "readability": evaluation.readability.score,
                "component_allocation": evaluation.component_allocation.score,
                "no_duplicates": evaluation.no_duplicates.score,
                "completeness": evaluation.completeness.score,
                "file_coverage": evaluation.file_coverage.score,
            },
            "suggestions": evaluation.suggestions,
        }
        reflection_history = state.get("reflection_history", [])
        reflection_history.append(history_entry)
        
        return {
            "confidence_score": overall_score,
            "reflection_feedback": feedback_text,
            "reflection_history": reflection_history,
        }
        
    except Exception as e:
        error(f"  Error evaluating analysis: {e}")
        return {
            "errors": [f"Evaluation failed: {e}"],
            "confidence_score": 0,
        }


def hitl_feedback_node(state: DocGenState) -> dict:
    """Prompt user for feedback when confidence score is below threshold.
    
    Displays the repository analysis and asks for feedback to improve it.
    Uses structured output with previous analysis as context.
    """
    repo_name = state["repo_name"]
    confidence_score = state.get("confidence_score", 0)
    repo_path = state.get("repo_path", "")
    
    step("Human-in-the-Loop: Repository Analysis Review")
    info(f"Confidence Score: {confidence_score}/100 (below threshold)")
    info("")
    
    # Load and display current repo analysis
    llm_summary_path = Path(".docs") / repo_name / "4_llm_summary.yaml"
    previous_analysis = ""
    if llm_summary_path.exists():
        previous_analysis = llm_summary_path.read_text(encoding="utf-8")
        info("Current Repository Analysis:")
        print("=" * 80)
        print(previous_analysis)
        print("=" * 80)
        info("")
    
    info("Please review the analysis above. You can:")
    info("  1. Press Enter to proceed with the current analysis")
    info("  2. Provide feedback to improve the analysis")
    info("")
    
    try:
        user_input = input("Enter your feedback (or press Enter to proceed): ").strip()
    except (EOFError, KeyboardInterrupt):
        warning("  No user input available (non-interactive environment)")
        warning("  Proceeding with current analysis")
        user_input = ""
    
    user_feedback = user_input if user_input else ""
    
    # If user provided feedback, regenerate analysis with structured output
    if user_feedback:
        info("  Regenerating analysis with your feedback...")
        try:
            file_tree_path = Path(".docs") / repo_name / "1_file_tree.yaml"
            file_tree = file_tree_path.read_text(encoding="utf-8")
            
            # Build prompt with previous analysis and feedback
            prompt = _build_hitl_prompt(
                file_tree=file_tree,
                previous_analysis=previous_analysis,
                user_feedback=user_feedback,
            )
            
            # Use structured output
            analysis = call_llm_structured(
                prompt,
                RepoAnalysis,
                generation_name="repo_analysis_with_feedback",
                metadata={"repo_name": repo_name, "phase": "repo_analysis_hitl"},
            )
            
            # Convert to YAML and save
            repo_analysis = _repo_analysis_to_yaml(analysis)
            save_yaml(repo_name, "4_llm_summary.yaml", [repo_analysis], plain_text=True)
            success("Repository analysis updated with user feedback")
            
            # Display the new analysis
            info("")
            info("Updated Repository Analysis:")
            print("=" * 80)
            print(repo_analysis)
            print("=" * 80)
            
            return {
                "user_feedback": user_feedback,
            }
            
        except Exception as e:
            warning(f"  Error regenerating analysis: {e}, keeping original")
    
    return {
        "user_feedback": user_feedback,
    }


def _build_hitl_prompt(
    file_tree: str,
    previous_analysis: str,
    user_feedback: str,
) -> str:
    """Build prompt for HITL regeneration with previous analysis and feedback."""
    return f"""You are improving a repository analysis based on user feedback.

## User Feedback (MUST be addressed):
{user_feedback}

## File Tree:
{file_tree}

## Previous Analysis:
{previous_analysis}

Instructions:
- Address the user's feedback - this is the primary goal
- Keep accurate parts from the previous analysis
- Each file should belong to exactly one module
- Group files into 3-8 logical modules"""


def _generate_code_example(
    function_name: str,
    function_signature: str,
    function_docstring: str,
    function_code: str,
    test_file_path: str | None,
    repo_path: Path,
    repo_name: str,
    usage_snippets: list[str] = None,
) -> tuple[str | None, str]:
    """Generate and validate a code example for a function.
    
    Uses test file if available, otherwise generates from function code.
    Includes real usage snippets from the codebase for context.
    """
    max_retries = CODE_EXAMPLE_MAX_RETRIES
    
    # Determine source and build initial prompt
    test_content = None
    if test_file_path:
        full_path = repo_path / test_file_path
        if full_path.exists():
            try:
                test_content = full_path.read_text(encoding="utf-8")
                if len(test_content) > 8000:
                    test_content = test_content[:8000] + "\n# ... (truncated)"
            except Exception:
                test_content = None
    
    if test_content:
        prompt = get_code_example_prompt_with_tests(
            function_name=function_name,
            function_signature=function_signature,
            function_docstring=function_docstring,
            test_content=test_content,
            test_file_path=test_file_path,
            usage_snippets=usage_snippets,
        )
        source = "test"
    else:
        prompt = get_code_example_prompt_from_code(
            function_name=function_name,
            function_signature=function_signature,
            function_docstring=function_docstring,
            function_code=function_code,
            usage_snippets=usage_snippets,
        )
        source = "inferred"
    
    # Generation with validation loop
    previous_code = None
    previous_issues = []
    
    for attempt in range(max_retries):
        # Build prompt (with retry feedback if needed)
        if attempt > 0 and previous_code and previous_issues:
            current_prompt = get_code_example_retry_prompt(
                original_prompt=prompt,
                previous_code=previous_code,
                issues=previous_issues,
            )
        else:
            current_prompt = prompt
        
        # Generate example
        try:
            result = call_llm_structured(
                current_prompt,
                CodeExample,
                generation_name=f"code_example_{source}",
                metadata={
                    "repo_name": repo_name,
                    "function": function_name,
                    "attempt": attempt + 1,
                    "source": source,
                },
            )
        except Exception as e:
            dim(f"    LLM call failed: {e}")
            continue
        
        if not result or not result.code:
            continue
        
        code = result.code.strip()
        previous_code = code
        
        # Stage 1: Syntax validation (AST)
        is_valid_syntax, syntax_issues = validate_code_example_syntax(code)
        if not is_valid_syntax:
            dim(f"    Syntax error (attempt {attempt + 1}): {syntax_issues}")
            previous_issues = syntax_issues
            continue
        
        # Basic checks (function name, no test artifacts)
        is_valid_basic, basic_issues = validate_code_example_basic(code, function_name)
        if not is_valid_basic:
            dim(f"    Basic validation failed (attempt {attempt + 1}): {basic_issues}")
            previous_issues = basic_issues
            continue
        
        # Stage 2: LLM reflection validation
        try:
            validation_prompt = get_code_example_validation_prompt(
                code=code,
                function_name=function_name,
                function_signature=function_signature,
            )
            
            validation_result = call_llm_structured(
                validation_prompt,
                CodeExampleValidation,
                generation_name="code_example_validation",
                metadata={
                    "repo_name": repo_name,
                    "function": function_name,
                    "attempt": attempt + 1,
                },
            )
            
            if validation_result and not validation_result.is_valid:
                dim(f"    LLM validation failed (attempt {attempt + 1}): {validation_result.issues}")
                previous_issues = validation_result.issues
                continue
                
        except Exception as e:
            # If validation call fails, accept the example (don't block)
            dim(f"    LLM validation call failed, accepting example: {e}")
        
        # Passed all validations
        return code, source
    
    # All retries failed
    return None, source


def document_functions_node(state: DocGenState) -> dict:
    """Document all functions sequentially in topological order (quality-first)."""
    repo_name = state["repo_name"]
    repo_path = Path(state["repo_path"])

    extracted_code_elements_file = Path(".docs") / repo_name / "2_node_extraction.yaml"
    doc_order_file = Path(".docs") / repo_name / "3_doc_order.yaml"

    if not extracted_code_elements_file.exists() or not doc_order_file.exists():
        return {"errors": ["Missing node extraction or doc order files"]}

    with open(extracted_code_elements_file, "r") as f:
        extracted_code_elements = yaml.safe_load(f) or []
    with open(doc_order_file, "r") as f:
        doc_order = yaml.safe_load(f) or []

    if not doc_order:
        dim("  No functions to document")
        return {}

    # Load repo analysis (already generated earlier in graph)
    try:
        repo_analysis = load_repo_analysis(repo_name)
        if not repo_analysis or not repo_analysis.strip():
            repo_analysis = ""  # OK for functions to proceed without analysis
    except Exception:
        repo_analysis = ""  # OK for functions to proceed without analysis

    func_lookup = _build_function_lookup(extracted_code_elements)

    # Initialize ChromaDB & ensure embeddings exist (if enabled)
    collection = None
    if ENABLE_EMBEDDINGS:
        collection = init_chroma(repo_name)
        embed_functions(extracted_code_elements, collection)
    else:
        dim("  Embeddings disabled (ENABLE_EMBEDDINGS=false)")

    # Load test mapping for code example generation
    test_mapping: dict[str, list[str]] = {}
    if ENABLE_CODE_EXAMPLES:
        test_mapping = load_test_mapping(repo_name)
        if test_mapping:
            dim(f"  Loaded test mapping: {len(test_mapping)} functions have tests")
    else:
        dim("  Code examples disabled (ENABLE_CODE_EXAMPLES=false)")

    # Load existing docs (resume support) - skip if force is enabled
    force = state.get("force", False)
    docs_file = Path(".docs") / repo_name / "5_function_docs.yaml"
    existing_docs: list[dict] = []
    generated_docs: dict[str, dict] = {}
    if not force and docs_file.exists():
        with open(docs_file, "r") as f:
            existing_docs = yaml.safe_load(f) or []
        generated_docs = {doc["node_id"]: doc for doc in existing_docs if isinstance(doc, dict) and doc.get("node_id")}

    # Cleanup removed functions
    current_node_ids = {entry["node_id"] for entry in doc_order if isinstance(entry, dict) and entry.get("node_id")}
    if existing_docs:
        existing_docs = [doc for doc in existing_docs if doc.get("node_id") in current_node_ids]
        generated_docs = {doc["node_id"]: doc for doc in existing_docs}
        save_yaml(repo_name, "5_function_docs.yaml", existing_docs)

    if existing_docs:
        dim(f"  Resuming: {len(existing_docs)}/{len(doc_order)} already documented")

    to_generate = [e for e in doc_order if e.get("node_id") not in generated_docs]
    if to_generate:
        step(f"Documenting {len(to_generate)} functions (sequential, topo-order)")

    errors_out: list[str] = []
    documented_count = 0
    skipped_count = 0

    for i, doc_entry in enumerate(doc_order):
        node_id = doc_entry.get("node_id")
        if not node_id:
            continue

        if node_id in generated_docs:
            skipped_count += 1
            continue

        if node_id not in func_lookup:
            errors_out.append(f"Function missing from lookup: {node_id}")
            continue

        function = func_lookup[node_id]
        file_name = function.get("file_name", "")

        dim(f"  [{i+1}/{len(doc_order)}] {node_id}")

        try:
            # Similar functions via RAG (style reference)
            similar_functions = get_similar(node_id, collection, k=3, max_distance=0.3)
            similar_docs = _get_similar_function_docs(similar_functions, generated_docs)

            # Called-by and dependency docs (now reliable thanks to topo-order)
            called_by_list = function.get("called_by", [])
            called_by_str = _format_called_by(called_by_list)
            dependency_docs = _get_dependency_docs(node_id, function, generated_docs, extracted_code_elements)

            # Extract real usage snippets from callers
            usage_snippets = _extract_usage_snippets(
                function.get("name", ""), called_by_list, func_lookup
            )

            # Targeted file context (imports + constants + nearby lines)
            file_source = ""
            full_file_path = repo_path / file_name
            if full_file_path.exists():
                file_source = full_file_path.read_text(encoding="utf-8")

            imports_str = _format_imports(_get_file_imports(extracted_code_elements, file_name))
            nearby = extract_relevant_file_context(
                file_source,
                function.get("start_line"),
                function.get("end_line"),
            )
            file_context = "\n\n".join([p for p in [imports_str, nearby] if p]).strip()

            # Get new metadata from parser
            signature = function.get("signature", "") or _extract_signature_from_code(function.get("code", ""))
            decorators = function.get("decorators", [])
            raises = function.get("raises", [])
            visibility = function.get("visibility", "public")

            prompt = get_function_doc_prompt(
                repo_analysis=repo_analysis,
                function_code=function.get("code", ""),
                function_name=function.get("name", ""),
                file_name=file_name,
                file_context=file_context,
                dependency_docs=dependency_docs,
                called_by=called_by_str,
                similar_functions=similar_docs,
                signature=signature,
                decorators=decorators,
                raises=raises,
                visibility=visibility,
                usage_snippets=usage_snippets,
            )

            # Build context for reflection
            function_context = f"""Function Code:
{function.get("code", "")}

File: {file_name}
Function Name: {function.get("name", "")}
"""
            if file_context:
                function_context += f"\nFile Context:\n{file_context}"
            if dependency_docs:
                function_context += f"\nDependencies: {', '.join(d.get('name', '') for d in dependency_docs)}"
            if called_by_str:
                function_context += f"\nCalled By: {called_by_str}"

            # Generate docstring with reflection
            docstring = _generate_docstring_with_reflection(
                original_prompt=prompt,
                context=function_context,
                doc_type="function",
                repo_name=repo_name,
                metadata={
                    "repo_name": repo_name,
                    "phase": "function_doc",
                    "node_id": node_id,
                    "file": file_name,
                    "function_name": function.get("name", ""),
                },
            )

            ok, issues = validate_docstring(docstring, signature)
            if not ok:
                repaired = _repair_docstring_with_llm(docstring, issues, repo_name=repo_name, node_id=node_id)
                if repaired:
                    docstring = repaired

            # Generate code example (if enabled)
            code_example = None
            example_source = None
            if ENABLE_CODE_EXAMPLES:
                test_files = test_mapping.get(node_id, [])
                test_file_path = test_files[0] if test_files else None
                
                if test_file_path:
                    dim(f"    Generating example from test: {test_file_path}")
                else:
                    dim(f"    Generating example from function code")
                
                code_example, example_source = _generate_code_example(
                    function_name=function.get("name", ""),
                    function_signature=signature,
                    function_docstring=docstring,
                    function_code=function.get("code", ""),
                    test_file_path=test_file_path,
                    repo_path=repo_path,
                    repo_name=repo_name,
                    usage_snippets=usage_snippets,
                )
                
                if code_example:
                    dim(f"    ✓ Code example generated ({example_source})")
                else:
                    dim(f"    ✗ Code example generation failed")

            function_doc = {
                "node_id": node_id,
                "file": file_name,
                "name": function.get("name", ""),
                "signature": signature,
                "decorators": decorators,
                "raises": raises,
                "visibility": visibility,
                "docstring": docstring,
                "code_example": code_example,
                "example_source": example_source,
                "line_start": function.get("start_line"),
                "line_end": function.get("end_line"),
                "dependencies": doc_entry.get("dependencies", []),
                "called_by": [c.get("source") for c in function.get("called_by", []) if isinstance(c, dict)],
            }

            generated_docs[node_id] = function_doc
            existing_docs.append(function_doc)
            save_yaml(repo_name, "5_function_docs.yaml", existing_docs)
            documented_count += 1

        except Exception as e:
            msg = f"Function {node_id}: {e}"
            errors_out.append(msg)
            dim(f"    ✗ Error: {e}")

    if documented_count > 0 or skipped_count > 0:
        success(f"{documented_count} documented, {skipped_count} skipped")

    return {"errors": errors_out} if errors_out else {}


def group_classes_node(state: DocGenState) -> dict:
    """Group functions by class (no LLM).
    
    Wraps: main.py step 6 (lines 244-283)
    Saves: 6_class_groups.yaml
    """
    repo_name = state["repo_name"]
    
    func_docs_file = Path(".docs") / repo_name / "5_function_docs.yaml"
    if not func_docs_file.exists():
        return {}
    
    with open(func_docs_file, "r") as f:
        function_docs = yaml.safe_load(f) or []
    
    classes = _group_functions_by_class(function_docs)
    
    if classes:
        step(f"Grouping into {len(classes)} classes")
        
        class_groups = []
        for class_id, methods in classes.items():
            parts = class_id.split("::")
            file_name = parts[0] if len(parts) > 0 else ""
            class_name = parts[1] if len(parts) > 1 else class_id
            
            class_groups.append({
                "class_id": class_id,
                "file": file_name,
                "name": class_name,
                "methods": [
                    {
                        "node_id": m["node_id"],
                        "name": m["name"],
                        "signature": m.get("signature", ""),
                        "docstring": m.get("docstring", "")
                    }
                    for m in methods
                ]
            })
        
        save_yaml(repo_name, "6_class_groups.yaml", class_groups)
        success(f"{len(class_groups)} classes grouped")
    
    return {}


def document_classes_node(state: DocGenState) -> dict:
    """Document all classes.
    
    Wraps: main.py step 7 (lines 285-386)
    Saves: 7_class_docs.yaml (incrementally)
    """
    repo_name = state["repo_name"]
    repo_path = Path(state["repo_path"])
    
    class_groups_file = Path(".docs") / repo_name / "6_class_groups.yaml"
    if not class_groups_file.exists():
        return {}
    
    with open(class_groups_file, "r") as f:
        class_groups = yaml.safe_load(f) or []
    
    if not class_groups:
        return {}
    
    step(f"Documenting {len(class_groups)} classes")

    # Load repo analysis (with retry)
    repo_analysis, err = _load_repo_analysis_with_retry(repo_name)
    if err:
        return {"errors": [err]}

    # Load extracted code elements (for imports context)
    extracted_code_elements = []
    extracted_code_elements_file = Path(".docs") / repo_name / "2_node_extraction.yaml"
    if extracted_code_elements_file.exists():
        with open(extracted_code_elements_file, "r") as f:
            extracted_code_elements = yaml.safe_load(f) or []
    
    # Load existing (for resume) - skip if force is enabled
    force = state.get("force", False)
    class_docs_file = Path(".docs") / repo_name / "7_class_docs.yaml"
    existing_docs = []
    documented_ids = set()
    
    if not force and class_docs_file.exists():
        with open(class_docs_file, "r") as f:
            existing_docs = yaml.safe_load(f) or []
        for doc in existing_docs:
            documented_ids.add(doc["class_id"])
        logger.debug(f"  Resuming: {len(existing_docs)}/{len(class_groups)} already documented")
    
    # Cleanup: Remove docs for classes that no longer exist
    current_class_ids = {cg["class_id"] for cg in class_groups}
    original_count = len(existing_docs)
    existing_docs = [doc for doc in existing_docs if doc["class_id"] in current_class_ids]
    removed_count = original_count - len(existing_docs)
    if removed_count > 0:
        documented_ids = {doc["class_id"] for doc in existing_docs}
        logger.debug(f"  Cleaned up {removed_count} removed class(es)")
        save_yaml(repo_name, "7_class_docs.yaml", existing_docs)
    
    documented_count = 0
    skipped_count = 0
    new_docs = []
    
    for i, class_group in enumerate(class_groups):
        class_id = class_group["class_id"]
        
        if class_id in documented_ids:
            skipped_count += 1
            continue
        
        file_name = class_group["file"]
        class_name = class_group["name"]
        methods = class_group["methods"]
        
        dim(f"  [{i+1}/{len(class_groups)}] {class_id}")
        
        try:
            file_source = ""
            full_file_path = repo_path / file_name
            if full_file_path.exists():
                file_source = full_file_path.read_text(encoding="utf-8")

            imports_str = _format_imports(_get_file_imports(extracted_code_elements, file_name)) if extracted_code_elements else ""
            file_context = "\n\n".join([p for p in [imports_str, extract_relevant_file_context(file_source)] if p]).strip()
            
            prompt = get_class_doc_prompt(
                repo_analysis=repo_analysis,
                class_name=class_name,
                file_name=file_name,
                file_context=file_context,
                methods=methods
            )
            
            # Build context for reflection
            class_context = f"""Class Name: {class_name}
File: {file_name}
"""
            if file_context:
                class_context += f"\nFile Context:\n{file_context}"
            if methods:
                class_context += f"\nMethods: {', '.join(m.get('name', '') for m in methods)}"

            # Generate docstring with reflection
            docstring = _generate_docstring_with_reflection(
                original_prompt=prompt,
                context=class_context,
                doc_type="class",
                repo_name=repo_name,
                metadata={"repo_name": repo_name, "phase": "class_doc", "class_id": class_id, "file": file_name},
            )
            
            class_doc = {
                "class_id": class_id,
                "file": file_name,
                "name": class_name,
                "docstring": docstring,
                "methods": [{"name": m["name"], "signature": m.get("signature", "")} for m in methods]
            }
            
            documented_ids.add(class_id)
            existing_docs.append(class_doc)
            new_docs.append(class_doc)
            
            save_yaml(repo_name, "7_class_docs.yaml", existing_docs)
            
            documented_count += 1
            
        except Exception as e:
            dim(f"    ✗ Error: {e}")
    
    if documented_count > 0 or skipped_count > 0:
        logger.info(f"  ✓ {documented_count} documented, {skipped_count} skipped")
    
    return {}


def group_files_node(state: DocGenState) -> dict:
    """Group documentation by file (no LLM).
    
    Wraps: main.py step 8 (lines 388-449)
    Saves: 8_file_groups.yaml
    """
    repo_name = state["repo_name"]
    
    func_docs_file = Path(".docs") / repo_name / "5_function_docs.yaml"
    class_docs_file = Path(".docs") / repo_name / "7_class_docs.yaml"
    
    if not func_docs_file.exists():
        return {}
    
    with open(func_docs_file, "r") as f:
        function_docs = yaml.safe_load(f) or []
    
    class_docs = []
    if class_docs_file.exists():
        with open(class_docs_file, "r") as f:
            class_docs = yaml.safe_load(f) or []
    
    all_files = set()
    for func in function_docs:
        all_files.add(func.get("file", ""))
    for cls in class_docs:
        all_files.add(cls.get("file", ""))
    all_files.discard("")
    
    if all_files:
        step(f"Grouping into {len(all_files)} files")
        
        file_groups = []
        for file_name in sorted(all_files):
            standalone_funcs = [
                f for f in function_docs
                if f.get("file") == file_name and "." not in f.get("name", "")
            ]
            file_classes = [c for c in class_docs if c.get("file") == file_name]
            
            file_groups.append({
                "file": file_name,
                "functions": [
                    {
                        "node_id": f["node_id"],
                        "name": f["name"],
                        "signature": f.get("signature", ""),
                        "docstring": f.get("docstring", "")
                    }
                    for f in standalone_funcs
                ],
                "classes": [
                    {
                        "class_id": c["class_id"],
                        "name": c["name"],
                        "docstring": c.get("docstring", ""),
                        "methods": c.get("methods", [])
                    }
                    for c in file_classes
                ]
            })
        
        save_yaml(repo_name, "8_file_groups.yaml", file_groups)
        success(f"{len(file_groups)} files grouped")
    
    return {}


def document_files_node(state: DocGenState) -> dict:
    """Document all files.
    
    Wraps: main.py step 9 (lines 451-547)
    Saves: 9_file_docs.yaml (incrementally)
    """
    repo_name = state["repo_name"]
    repo_path = Path(state["repo_path"])
    
    file_groups_file = Path(".docs") / repo_name / "8_file_groups.yaml"
    if not file_groups_file.exists():
        return {}
    
    with open(file_groups_file, "r") as f:
        file_groups = yaml.safe_load(f) or []
    
    if not file_groups:
        return {}
    
    step(f"Documenting {len(file_groups)} files")
    
    # Load repo analysis (with retry)
    repo_analysis, err = _load_repo_analysis_with_retry(repo_name)
    if err:
        return {"errors": [err]}

    extracted_code_elements = []
    extracted_code_elements_file = Path(".docs") / repo_name / "2_node_extraction.yaml"
    if extracted_code_elements_file.exists():
        with open(extracted_code_elements_file, "r") as f:
            extracted_code_elements = yaml.safe_load(f) or []
    
    file_docs_file = Path(".docs") / repo_name / "9_file_docs.yaml"
    # Load existing (for resume) - skip if force is enabled
    force = state.get("force", False)
    existing_docs = []
    documented_files = set()
    
    if not force and file_docs_file.exists():
        with open(file_docs_file, "r") as f:
            existing_docs = yaml.safe_load(f) or []
        for doc in existing_docs:
            documented_files.add(doc["file"])
        logger.debug(f"  Resuming: {len(existing_docs)}/{len(file_groups)} already documented")
    
    # Cleanup: Remove docs for files that no longer exist
    current_files = {fg["file"] for fg in file_groups}
    original_count = len(existing_docs)
    existing_docs = [doc for doc in existing_docs if doc["file"] in current_files]
    removed_count = original_count - len(existing_docs)
    if removed_count > 0:
        documented_files = {doc["file"] for doc in existing_docs}
        logger.debug(f"  Cleaned up {removed_count} removed file(s)")
        save_yaml(repo_name, "9_file_docs.yaml", existing_docs)
    
    documented_count = 0
    skipped_count = 0
    new_docs = []
    
    for i, file_group in enumerate(file_groups):
        file_name = file_group["file"]
        
        if file_name in documented_files:
            skipped_count += 1
            continue
        
        dim(f"  [{i+1}/{len(file_groups)}] {file_name}")
        
        try:
            file_source = ""
            full_file_path = repo_path / file_name
            if full_file_path.exists():
                file_source = full_file_path.read_text(encoding="utf-8")

            imports_str = _format_imports(_get_file_imports(extracted_code_elements, file_name)) if extracted_code_elements else ""
            file_context = "\n\n".join([p for p in [imports_str, extract_relevant_file_context(file_source)] if p]).strip()
            
            prompt = get_file_doc_prompt(
                repo_analysis=repo_analysis,
                file_name=file_name,
                file_context=file_context,
                functions=file_group.get("functions", []),
                classes=file_group.get("classes", [])
            )
            
            # Build context for reflection
            file_context_str = f"""File Name: {file_name}
"""
            if file_context:
                file_context_str += f"\nFile Context:\n{file_context}"
            if file_group.get("functions"):
                file_context_str += f"\nFunctions: {', '.join(f.get('name', '') for f in file_group.get('functions', []))}"
            if file_group.get("classes"):
                file_context_str += f"\nClasses: {', '.join(c.get('name', '') for c in file_group.get('classes', []))}"

            # Generate docstring with reflection
            docstring = _generate_docstring_with_reflection(
                original_prompt=prompt,
                context=file_context_str,
                doc_type="file",
                repo_name=repo_name,
                metadata={"repo_name": repo_name, "phase": "file_doc", "file": file_name},
            )
            
            file_doc = {
                "file": file_name,
                "docstring": docstring,
                "functions": [f["name"] for f in file_group.get("functions", [])],
                "classes": [c["name"] for c in file_group.get("classes", [])]
            }
            
            documented_files.add(file_name)
            existing_docs.append(file_doc)
            new_docs.append(file_doc)
            
            save_yaml(repo_name, "9_file_docs.yaml", existing_docs)
            
            documented_count += 1
            
        except Exception as e:
            dim(f"    ✗ Error: {e}")
    
    if documented_count > 0 or skipped_count > 0:
        logger.info(f"  ✓ {documented_count} documented, {skipped_count} skipped")
    
    return {}


def group_modules_node(state: DocGenState) -> dict:
    """Group files by module (no LLM).
    
    Wraps: main.py step 10 (lines 549-611)
    Saves: 10_module_groups.yaml
    """
    repo_name = state["repo_name"]
    
    repo_analysis_file = Path(".docs") / repo_name / "4_llm_summary.yaml"
    file_docs_file = Path(".docs") / repo_name / "9_file_docs.yaml"
    
    if not repo_analysis_file.exists() or not file_docs_file.exists():
        return {}
    
    repo_analysis_text = repo_analysis_file.read_text(encoding="utf-8")
    try:
        repo_analysis_data = yaml.safe_load(repo_analysis_text) or {}
    except Exception:
        repo_analysis_data = {}
    modules_def = repo_analysis_data.get("modules", [])
    
    with open(file_docs_file, "r") as f:
        file_docs = yaml.safe_load(f) or []
    
    file_docs_lookup = {f["file"]: f for f in file_docs}
    
    if modules_def:
        step(f"Grouping into {len(modules_def)} modules")
        
        module_groups = []
        for module_def in modules_def:
            module_name = module_def.get("name", "Unknown")
            module_description = module_def.get("description", "")
            module_files = module_def.get("files", [])
            
            # Normalize file paths
            normalized_files = []
            for f in module_files:
                if "/" in f:
                    parts = f.split("/", 1)
                    if parts[0].lower() == repo_name.lower():
                        f = parts[1]
                normalized_files.append(f)
            
            module_file_docs = []
            for file_path in normalized_files:
                if file_path in file_docs_lookup:
                    module_file_docs.append(file_docs_lookup[file_path])
                else:
                    module_file_docs.append({
                        "file": file_path,
                        "docstring": "",
                        "functions": [],
                        "classes": []
                    })
            
            module_groups.append({
                "module": module_name,
                "description": module_description,
                "files": module_file_docs
            })
        
        save_yaml(repo_name, "10_module_groups.yaml", module_groups)
        success(f"{len(module_groups)} modules grouped")
    
    return {}


def document_modules_node(state: DocGenState) -> dict:
    """Document all modules.
    
    Wraps: main.py step 11 (lines 613-699)
    Saves: 11_module_docs.yaml (incrementally)
    """
    repo_name = state["repo_name"]
    
    module_groups_file = Path(".docs") / repo_name / "10_module_groups.yaml"
    if not module_groups_file.exists():
        return {}
    
    with open(module_groups_file, "r") as f:
        module_groups = yaml.safe_load(f) or []
    
    if not module_groups:
        return {}
    
    step(f"Documenting {len(module_groups)} modules")
    
    # Load repo analysis (with retry)
    repo_analysis, err = _load_repo_analysis_with_retry(repo_name)
    if err:
        return {"errors": [err]}

    # Load existing (for resume) - skip if force is enabled
    force = state.get("force", False)
    module_docs_file = Path(".docs") / repo_name / "11_module_docs.yaml"
    existing_docs = []
    documented_modules = set()
    
    if not force and module_docs_file.exists():
        with open(module_docs_file, "r") as f:
            existing_docs = yaml.safe_load(f) or []
        for doc in existing_docs:
            documented_modules.add(doc["module"])
        logger.debug(f"  Resuming: {len(existing_docs)}/{len(module_groups)} already documented")
    
    # Cleanup: Remove docs for modules that no longer exist
    current_modules = {mg["module"] for mg in module_groups}
    original_count = len(existing_docs)
    existing_docs = [doc for doc in existing_docs if doc["module"] in current_modules]
    removed_count = original_count - len(existing_docs)
    if removed_count > 0:
        documented_modules = {doc["module"] for doc in existing_docs}
        logger.debug(f"  Cleaned up {removed_count} removed module(s)")
        save_yaml(repo_name, "11_module_docs.yaml", existing_docs)
    
    documented_count = 0
    skipped_count = 0
    new_docs = []
    
    for i, module_group in enumerate(module_groups):
        module_name = module_group["module"]
        
        if module_name in documented_modules:
            skipped_count += 1
            continue
        
        dim(f"  [{i+1}/{len(module_groups)}] {module_name}")
        
        try:
            prompt = get_module_doc_prompt(
                repo_analysis=repo_analysis,
                module_name=module_name,
                module_description=module_group.get("description", ""),
                files=module_group.get("files", [])
            )
            
            # Build context for reflection
            module_context = f"""Module Name: {module_name}
Description: {module_group.get("description", "")}
"""
            if module_group.get("files"):
                module_context += f"\nFiles: {', '.join(f.get('file', '') for f in module_group.get('files', []))}"

            # Generate docstring with reflection
            docstring = _generate_docstring_with_reflection(
                original_prompt=prompt,
                context=module_context,
                doc_type="module",
                repo_name=repo_name,
                metadata={"repo_name": repo_name, "phase": "module_doc", "module": module_name},
            )
            
            module_doc = {
                "module": module_name,
                "description": module_group.get("description", ""),
                "docstring": docstring,
                "files": [f["file"] for f in module_group.get("files", [])]
            }
            
            documented_modules.add(module_name)
            existing_docs.append(module_doc)
            new_docs.append(module_doc)
            
            save_yaml(repo_name, "11_module_docs.yaml", existing_docs)
            
            documented_count += 1
            
        except Exception as e:
            dim(f"    ✗ Error: {e}")
    
    if documented_count > 0 or skipped_count > 0:
        logger.info(f"  ✓ {documented_count} documented, {skipped_count} skipped")
    
    return {}


def _architecture_diagram_to_yaml(diagram: ArchitectureDiagram) -> str:
    """Convert ArchitectureDiagram Pydantic model to YAML string for file storage."""
    data = {
        "mermaid": diagram.mermaid,
        "components": [
            {
                "id": c.id,
                "name": c.name,
                "description": c.description,
            }
            for c in diagram.components
        ],
    }
    return yaml.dump(data, default_flow_style=False, allow_unicode=True, sort_keys=False)


def generate_architecture_diagram_node(state: DocGenState) -> dict:
    """Generate architecture diagram in Mermaid format with component explanations.
    
    Saves: 12_architecture_diagram.yaml
    """
    repo_name = state["repo_name"]
    
    force = state.get("force", False)
    diagram_file = Path(".docs") / repo_name / "12_architecture_diagram.yaml"
    
    # Check cache (unless force mode)
    if not force and diagram_file.exists():
        dim("  Architecture diagram (cached)")
        return {}
    
    step("Generating architecture diagram")
    
    try:
        # Load required data
        file_tree_path = Path(".docs") / repo_name / "1_file_tree.yaml"
        repo_analysis_path = Path(".docs") / repo_name / "4_llm_summary.yaml"
        module_docs_path = Path(".docs") / repo_name / "11_module_docs.yaml"
        
        file_tree = ""
        if file_tree_path.exists():
            file_tree = file_tree_path.read_text(encoding="utf-8")
        
        repo_analysis = ""
        if repo_analysis_path.exists():
            repo_analysis = repo_analysis_path.read_text(encoding="utf-8")
        
        module_docs = []
        if module_docs_path.exists():
            with open(module_docs_path, "r") as f:
                module_docs = yaml.safe_load(f) or []
        
        # Generate architecture diagram
        prompt = get_architecture_diagram_prompt(
            repo_name=repo_name,
            repo_analysis=repo_analysis,
            module_docs=module_docs,
            file_tree=file_tree,
        )
        
        diagram = call_llm_structured(
            prompt,
            ArchitectureDiagram,
            generation_name="architecture_diagram",
            metadata={"repo_name": repo_name, "phase": "architecture_diagram"},
        )
        
        # Save diagram
        diagram_yaml = _architecture_diagram_to_yaml(diagram)
        save_yaml(repo_name, "12_architecture_diagram.yaml", [diagram_yaml], plain_text=True)
        
        # Display summary
        success(f"Architecture diagram generated ({len(diagram.components)} components)")
        info("")
        info("Mermaid Diagram:")
        print("=" * 60)
        print(diagram.mermaid)
        print("=" * 60)
        info("")
        info("Components:")
        for comp in diagram.components:
            dim(f"  • {comp.name}: {comp.description}")
        info("")
        
        return {}
        
    except Exception as e:
        error(f"  Architecture diagram failed: {e}")
        return {"errors": [f"Architecture diagram failed: {e}"]}


def _proposed_toc_to_yaml(toc: ProposedTOC) -> str:
    """Convert ProposedTOC Pydantic model to YAML string for file storage."""
    sections_data = []
    for s in toc.sections:
        section_dict = {
            "slug": s.slug,
            "title": s.title,
            "description": s.description,
            "is_core": s.is_core,
        }
        if s.subsections:
            section_dict["subsections"] = [
                {"slug": sub.slug, "title": sub.title, "description": sub.description}
                for sub in s.subsections
            ]
        sections_data.append(section_dict)
    
    data = {"sections": sections_data, "reasoning": toc.reasoning}
    return yaml.dump(data, default_flow_style=False, allow_unicode=True, sort_keys=False)


def _format_toc_for_display(sections: list[dict]) -> str:
    """Format TOC sections with subsections for display to user."""
    lines = []
    for i, section in enumerate(sections):
        core_marker = " [CORE]" if section.get("is_core") else ""
        lines.append(f"  {i+1}. {section.get('title', '')} ({section.get('slug', '')}){core_marker}")
        if section.get("description"):
            lines.append(f"     └─ {section.get('description', '')}")
        # Display subsections
        for j, sub in enumerate(section.get("subsections", [])):
            lines.append(f"     {i+1}.{j+1}. {sub.get('title', '')} ({sub.get('slug', '')})")
    return "\n".join(lines)


def propose_toc_node(state: DocGenState) -> dict:
    """Propose a table of contents structure for documentation.
    
    Analyzes the codebase and existing docs to propose an appropriate TOC.
    Saves: 13_proposed_toc.yaml, 14_confirmed_toc.yaml (after HITL)
    """
    repo_name = state["repo_name"]
    repo_path = state.get("repo_path", "")
    
    force = state.get("force", False)
    toc_file = Path(".docs") / repo_name / "13_proposed_toc.yaml"
    
    # Check cache (unless force mode)
    if not force and toc_file.exists():
        try:
            with open(toc_file, "r") as f:
                cached_data = yaml.safe_load(f)
            if cached_data and cached_data.get("sections"):
                dim("  TOC proposal (cached)")
                return {
                    "proposed_toc": cached_data["sections"],
                }
        except Exception:
            pass  # Regenerate if cache is invalid
    
    step("Proposing documentation structure (TOC)")
    
    try:
        # Load required data
        file_tree_path = Path(".docs") / repo_name / "1_file_tree.yaml"
        repo_analysis_path = Path(".docs") / repo_name / "4_llm_summary.yaml"
        module_docs_path = Path(".docs") / repo_name / "11_module_docs.yaml"
        
        file_tree = ""
        if file_tree_path.exists():
            file_tree = file_tree_path.read_text(encoding="utf-8")
        
        repo_analysis = ""
        if repo_analysis_path.exists():
            repo_analysis = repo_analysis_path.read_text(encoding="utf-8")
        
        module_docs = []
        if module_docs_path.exists():
            with open(module_docs_path, "r") as f:
                module_docs = yaml.safe_load(f) or []
        
        # Load existing markdown documentation for context
        existing_docs = ""
        if repo_path:
            md_finder = MarkdownFinder(repo_path)
            existing_docs = md_finder.get_markdown_summary()
            if existing_docs:
                dim(f"  Including {len(md_finder.find_markdown_files())} markdown file(s) as context")
        
        # Generate TOC proposal
        prompt = get_toc_proposal_prompt(
            repo_name=repo_name,
            repo_analysis=repo_analysis,
            module_docs=module_docs,
            file_tree=file_tree,
            existing_docs=existing_docs
        )
        
        toc_proposal = call_llm_structured(
            prompt,
            ProposedTOC,
            generation_name="toc_proposal",
            metadata={"repo_name": repo_name, "phase": "toc_proposal"},
        )
        
        # Save proposal
        toc_yaml = _proposed_toc_to_yaml(toc_proposal)
        save_yaml(repo_name, "13_proposed_toc.yaml", [toc_yaml], plain_text=True)
        
        # Convert to dict list for state (including subsections)
        sections = []
        for s in toc_proposal.sections:
            section_dict = {
                "slug": s.slug,
                "title": s.title,
                "description": s.description,
                "is_core": s.is_core,
            }
            if s.subsections:
                section_dict["subsections"] = [
                    {"slug": sub.slug, "title": sub.title, "description": sub.description}
                    for sub in s.subsections
                ]
            sections.append(section_dict)
        
        success(f"Proposed {len(sections)} documentation sections")
        
        # Display the proposal
        info("")
        info("Proposed Documentation Structure:")
        print("=" * 60)
        print(_format_toc_for_display(sections))
        print("=" * 60)
        info(f"\nReasoning: {toc_proposal.reasoning}")
        info("")
        
        return {
            "proposed_toc": sections,
        }
        
    except Exception as e:
        error(f"  TOC proposal failed: {e}")
        # Fall back to default TOC
        default_toc = [
            {"slug": "introduction", "title": "Introduction", "description": "Project overview and purpose", "is_core": True},
            {"slug": "quick-start", "title": "Quick Start", "description": "Get started in minutes", "is_core": True},
            {"slug": "architecture", "title": "Architecture", "description": "System design and components", "is_core": True},
            {"slug": "key-concepts", "title": "Key Concepts", "description": "Core terminology and patterns", "is_core": False},
            {"slug": "how-to-guides", "title": "How-To Guides", "description": "Step-by-step tutorials", "is_core": False},
        ]
        return {
            "proposed_toc": default_toc,
            "errors": [f"TOC proposal failed, using defaults: {e}"],
        }


def hitl_toc_node(state: DocGenState) -> dict:
    """Human-in-the-loop confirmation of documentation TOC.
    
    Shows proposed TOC to user and allows modifications.
    Loops until user confirms (empty input = accept).
    """
    repo_name = state["repo_name"]
    proposed_toc = state.get("proposed_toc", [])
    repo_path = state.get("repo_path", "")
    
    if not proposed_toc:
        warning("  No TOC proposal available")
        return {"toc_confirmed": True, "confirmed_toc": []}
    
    current_toc = proposed_toc.copy()
    iteration = 0
    max_iterations = 10  # Safety limit
    
    while iteration < max_iterations:
        iteration += 1
        
        step(f"TOC Review (iteration {iteration})")
        info("")
        info("Current Documentation Structure:")
        print("=" * 60)
        print(_format_toc_for_display(current_toc))
        print("=" * 60)
        info("")
        
        info("Options:")
        info("  • Press Enter to ACCEPT this structure")
        info("  • Type feedback to modify (e.g., 'add Deployment section', 'remove FAQ')")
        info("  • Type 'add: Section Name' to add a new section")
        info("  • Type 'remove: N' to remove section N")
        info("  • Type 'reorder: N1,N2,N3...' to reorder sections")
        info("")
        
        try:
            user_input = input("Your feedback (or Enter to accept): ").strip()
        except (EOFError, KeyboardInterrupt):
            warning("  Non-interactive environment, accepting proposed TOC")
            user_input = ""
        
        # Empty input = accept
        if not user_input:
            success("TOC confirmed by user")
            break
        
        # Handle simple commands
        if user_input.lower().startswith("remove:"):
            try:
                idx = int(user_input.split(":")[1].strip()) - 1
                if 0 <= idx < len(current_toc):
                    removed = current_toc.pop(idx)
                    info(f"  Removed: {removed.get('title', '')}")
                else:
                    warning(f"  Invalid index: {idx + 1}")
            except ValueError:
                warning("  Invalid remove command. Use 'remove: N' where N is the section number")
            continue
        
        if user_input.lower().startswith("add:"):
            title = user_input.split(":", 1)[1].strip()
            if title:
                slug = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
                new_section = {
                    "slug": slug,
                    "title": title,
                    "description": f"Documentation for {title}",
                    "is_core": False,
                }
                current_toc.append(new_section)
                info(f"  Added: {title} (slug: {slug})")
            continue
        
        if user_input.lower().startswith("reorder:"):
            try:
                order_str = user_input.split(":")[1].strip()
                new_order = [int(x.strip()) - 1 for x in order_str.split(",")]
                if len(new_order) == len(current_toc) and all(0 <= i < len(current_toc) for i in new_order):
                    current_toc = [current_toc[i] for i in new_order]
                    info("  Sections reordered")
                else:
                    warning("  Invalid reorder. Provide all section numbers comma-separated")
            except ValueError:
                warning("  Invalid reorder command. Use 'reorder: 1,3,2,4...'")
            continue
        
        # Otherwise, use LLM to refine based on feedback
        info("  Refining TOC based on your feedback...")
        
        try:
            # Load repo analysis for context
            repo_analysis = ""
            repo_analysis_path = Path(".docs") / repo_name / "4_llm_summary.yaml"
            if repo_analysis_path.exists():
                repo_analysis = repo_analysis_path.read_text(encoding="utf-8")
            
            prompt = get_toc_refinement_prompt(
                previous_toc=current_toc,
                user_feedback=user_input,
                repo_name=repo_name,
                repo_analysis=repo_analysis
            )
            
            refined_toc = call_llm_structured(
                prompt,
                ProposedTOC,
                generation_name=f"toc_refinement_{iteration}",
                metadata={"repo_name": repo_name, "phase": "toc_refinement", "iteration": iteration},
            )
            
            # Update current TOC
            current_toc = [
                {
                    "slug": s.slug,
                    "title": s.title,
                    "description": s.description,
                    "is_core": s.is_core,
                }
                for s in refined_toc.sections
            ]
            
            success(f"TOC updated ({len(current_toc)} sections)")
            
        except Exception as e:
            warning(f"  Could not refine TOC: {e}")
            info("  Please try again with different feedback or use commands (add:/remove:/reorder:)")
    
    # Save confirmed TOC
    confirmed_data = {
        "sections": current_toc,
        "confirmed": True,
    }
    save_yaml(repo_name, "14_confirmed_toc.yaml", [yaml.dump(confirmed_data, default_flow_style=False)], plain_text=True)
    
    return {
        "confirmed_toc": current_toc,
        "toc_confirmed": True,
    }


def _dynamic_synthesis_to_yaml(synthesis: DynamicSynthesisDoc) -> str:
    """Convert DynamicSynthesisDoc Pydantic model to YAML string for file storage."""
    data = {
        "sections": [
            {
                "slug": s.slug,
                "title": s.title,
                "content": s.content,
            }
            for s in synthesis.sections
        ],
        "is_dynamic": True,
    }
    return yaml.dump(data, default_flow_style=False, allow_unicode=True, sort_keys=False)


def _generate_dynamic_synthesis_with_reflection(
    original_prompt: str,
    confirmed_toc: list[dict],
    repo_analysis: str,
    module_docs: list[dict],
    file_tree: str,
    existing_docs: str,
    repo_name: str,
    *,
    max_iterations: int = MAX_REFLECTION_ITERATIONS,
    confidence_threshold: int = REFLECTION_CONFIDENCE_THRESHOLD
) -> DynamicSynthesisDoc:
    """Generate dynamic synthesis documentation with basic validation.
    
    Note: Uses simpler validation than fixed synthesis since sections are dynamic.
    """
    prompt = original_prompt
    
    synthesis = call_llm_structured(
        prompt,
        DynamicSynthesisDoc,
        generation_name="dynamic_synthesis",
        metadata={"repo_name": repo_name, "phase": "dynamic_synthesis"},
    )
    
    # Basic validation: ensure all TOC sections have content
    toc_slugs = {s.get("slug") for s in confirmed_toc}
    generated_slugs = {s.slug for s in synthesis.sections}
    
    missing_slugs = toc_slugs - generated_slugs
    if missing_slugs:
        warning(f"  Missing sections in synthesis: {missing_slugs}")
        # Add placeholder sections for missing ones
        for slug in missing_slugs:
            toc_item = next((s for s in confirmed_toc if s.get("slug") == slug), None)
            if toc_item:
                from llm.schemas import DynamicSection
                synthesis.sections.append(DynamicSection(
                    slug=slug,
                    title=toc_item.get("title", slug.replace("-", " ").title()),
                    content=f"*Content for {toc_item.get('title', slug)} to be added.*"
                ))
    
    return synthesis


def synthesize_node(state: DocGenState) -> dict:
    """Generate synthesis documentation based on confirmed TOC or fallback to fixed structure.
    
    If confirmed_toc is available, generates dynamic documentation matching the TOC.
    Otherwise, falls back to the fixed structure (introduction, why, quick_start, etc.).
    
    Saves: 15_synthesis_doc.yaml
    """
    repo_name = state["repo_name"]
    repo_path = state.get("repo_path", "")
    confirmed_toc = state.get("confirmed_toc") or state.get("proposed_toc")
    
    force = state.get("force", False)
    synthesis_doc_file = Path(".docs") / repo_name / "15_synthesis_doc.yaml"
    if not force and synthesis_doc_file.exists():
        dim("  Synthesis documentation (cached)")
        return {}
    
    file_tree_path = Path(".docs") / repo_name / "1_file_tree.yaml"
    repo_analysis_path = Path(".docs") / repo_name / "4_llm_summary.yaml"
    module_docs_path = Path(".docs") / repo_name / "11_module_docs.yaml"
    
    if not file_tree_path.exists() or not repo_analysis_path.exists():
        return {}
    
    step("Generating synthesis documentation")
    
    try:
        file_tree = file_tree_path.read_text(encoding="utf-8")
        repo_analysis_text = repo_analysis_path.read_text(encoding="utf-8")
        
        module_docs = []
        if module_docs_path.exists():
            with open(module_docs_path, "r") as f:
                module_docs = yaml.safe_load(f) or []
        
        # Load existing markdown documentation for context
        existing_docs = ""
        if repo_path:
            md_finder = MarkdownFinder(repo_path)
            existing_docs = md_finder.get_markdown_summary()
            if existing_docs:
                dim(f"  Including {len(md_finder.find_markdown_files())} markdown file(s) as context")
        
        # Check if we have a confirmed/proposed TOC (dynamic mode)
        if confirmed_toc:
            info(f"  Using dynamic TOC with {len(confirmed_toc)} sections")
            
            prompt = get_dynamic_synthesis_prompt(
                repo_name=repo_name,
                confirmed_toc=confirmed_toc,
                repo_analysis=repo_analysis_text,
                module_docs=module_docs,
                file_tree=file_tree,
                existing_docs=existing_docs
            )
            
            # Generate dynamic synthesis
            synthesis = _generate_dynamic_synthesis_with_reflection(
                original_prompt=prompt,
                confirmed_toc=confirmed_toc,
                repo_analysis=repo_analysis_text,
                module_docs=module_docs,
                file_tree=file_tree,
                existing_docs=existing_docs,
                repo_name=repo_name,
            )
            
            # Convert to YAML for storage
            synthesis_result = _dynamic_synthesis_to_yaml(synthesis)
            
        else:
            # Fallback to fixed structure (backward compatibility)
            info("  Using fixed TOC structure (no dynamic TOC available)")
            
            prompt = get_synthesis_doc_prompt(
                repo_name=repo_name,
                repo_analysis=repo_analysis_text,
                module_docs=module_docs,
                file_tree=file_tree,
                existing_docs=existing_docs
            )
            
            # Generate synthesis with reflection
            synthesis = _generate_synthesis_with_reflection(
                original_prompt=prompt,
                repo_analysis=repo_analysis_text,
                module_docs=module_docs,
                file_tree=file_tree,
                existing_docs=existing_docs,
                repo_name=repo_name,
            )
            
            # Convert to YAML for storage
            synthesis_result = _synthesis_doc_to_yaml(synthesis)
        
        if synthesis_result:
            save_yaml(repo_name, "15_synthesis_doc.yaml", [synthesis_result], plain_text=True)
            success("Synthesis documentation generated")
            return {}
        else:
            dim("  LLM returned empty synthesis")
            return {"errors": ["Synthesis LLM returned empty"]}
            
    except Exception as e:
        dim(f"  Error: {e}")
        return {"errors": [f"Synthesis error: {e}"]}
