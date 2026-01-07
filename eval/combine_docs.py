#!/usr/bin/env python3
"""
Combine all documentation files from .docs/<repo>/site/docs into a single structured JSON file.

Usage:
    python eval/combine_docs.py <repo_name>
    python eval/combine_docs.py graphrag
    python eval/combine_docs.py --all  # Process all repos
"""

import argparse
import json
import re
from pathlib import Path


def parse_frontmatter(content: str) -> tuple[dict, str]:
    """Extract YAML frontmatter and body from markdown content."""
    frontmatter = {}
    body = content

    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            fm_text = parts[1].strip()
            body = parts[2].strip()

            # Simple YAML parsing for common frontmatter fields
            for line in fm_text.split("\n"):
                if ":" in line:
                    key, value = line.split(":", 1)
                    key = key.strip()
                    value = value.strip()
                    # Try to parse as int
                    try:
                        value = int(value)
                    except ValueError:
                        pass
                    frontmatter[key] = value

    return frontmatter, body


def extract_title(body: str) -> str | None:
    """Extract the first H1 title from markdown body."""
    match = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
    return match.group(1).strip() if match else None


def get_doc_structure(docs_path: Path) -> dict:
    """Build a structured dictionary from all markdown files in the docs directory."""
    structure = {
        "sections": [],
        "files": []
    }

    if not docs_path.exists():
        return structure

    # Group files by their immediate parent directory
    sections_map = {}
    root_files = []

    # Sections to exclude
    excluded_sections = {"api", "files"}

    for md_file in sorted(docs_path.rglob("*.md")):
        rel_path = md_file.relative_to(docs_path)
        parts = rel_path.parts

        # Skip files in excluded sections
        if len(parts) > 1 and parts[0] in excluded_sections:
            continue

        content = md_file.read_text(encoding="utf-8")
        frontmatter, body = parse_frontmatter(content)
        title = extract_title(body) or md_file.stem

        doc_entry = {
            "path": str(rel_path),
            "title": title,
            "frontmatter": frontmatter,
            "content": body
        }

        # Determine section (parent directory)
        if len(parts) == 1:
            # Root-level file
            root_files.append(doc_entry)
        else:
            section_name = parts[0]
            if section_name not in sections_map:
                sections_map[section_name] = {
                    "name": section_name,
                    "files": []
                }
            sections_map[section_name]["files"].append(doc_entry)

    # Sort sections and their files
    for section in sections_map.values():
        section["files"].sort(
            key=lambda x: (x.get("frontmatter", {}).get("sidebar_position", 999), x["path"])
        )

    structure["sections"] = sorted(sections_map.values(), key=lambda x: x["name"])
    structure["files"] = sorted(
        root_files,
        key=lambda x: (x.get("frontmatter", {}).get("sidebar_position", 999), x["path"])
    )

    return structure


def combine_docs(repo_name: str, base_path: Path) -> dict:
    """Combine all docs for a given repo into a structured dictionary."""
    docs_path = base_path / ".docs" / repo_name / "site" / "docs"

    if not docs_path.exists():
        raise FileNotFoundError(f"Docs path not found: {docs_path}")

    structure = get_doc_structure(docs_path)

    # Calculate stats
    total_files = len(structure["files"])
    for section in structure["sections"]:
        total_files += len(section["files"])

    return {
        "repo": repo_name,
        "docs_path": str(docs_path),
        "total_files": total_files,
        "total_sections": len(structure["sections"]),
        "structure": structure
    }


def get_available_repos(base_path: Path) -> list[str]:
    """Get list of repos that have docs generated."""
    docs_base = base_path / ".docs"
    if not docs_base.exists():
        return []

    repos = []
    for repo_dir in docs_base.iterdir():
        if repo_dir.is_dir() and (repo_dir / "site" / "docs").exists():
            repos.append(repo_dir.name)

    return sorted(repos)


def main():
    parser = argparse.ArgumentParser(
        description="Combine documentation files into a structured JSON file."
    )
    parser.add_argument(
        "repo",
        nargs="?",
        help="Repository name (e.g., 'graphrag') or '--all' to process all repos"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Process all available repos"
    )
    parser.add_argument(
        "--output", "-o",
        help="Output file path (default: .docs/<repo>/combined_docs.json)"
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List available repos and exit"
    )

    args = parser.parse_args()
    base_path = Path(__file__).parent.parent

    # List mode
    if args.list:
        repos = get_available_repos(base_path)
        if repos:
            print("Available repos:")
            for repo in repos:
                print(f"  - {repo}")
        else:
            print("No repos found in .docs/")
        return

    # Determine which repos to process
    if args.all:
        repos = get_available_repos(base_path)
        if not repos:
            print("No repos found in .docs/")
            return
    elif args.repo:
        repos = [args.repo]
    else:
        parser.print_help()
        return

    # Process each repo
    for repo in repos:
        try:
            print(f"Processing {repo}...")
            result = combine_docs(repo, base_path)

            # Determine output path
            if args.output and len(repos) == 1:
                output_path = Path(args.output)
            else:
                output_path = base_path / ".docs" / repo / "combined_docs.json"

            output_path.parent.mkdir(parents=True, exist_ok=True)

            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2, ensure_ascii=False)

            print(f"  -> {output_path}")
            print(f"     {result['total_files']} files in {result['total_sections']} sections")

        except FileNotFoundError as e:
            print(f"  Error: {e}")
        except Exception as e:
            print(f"  Error processing {repo}: {e}")


if __name__ == "__main__":
    main()
