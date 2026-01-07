"""MarkdownFinder - Find and load markdown files for LLM context."""

from pathlib import Path

from docgen.utils.config import (
    MAX_MD_FILE_CHARS,
    MAX_TOTAL_MD_CONTEXT_CHARS,
    EXCLUDED_MD_FILES,
    EXCLUDED_MD_DIRS,
)

# Directories to always skip for markdown (dependencies, caches, version control)
# NOTE: We intentionally DON'T use DEFAULT_EXCLUDED_DIRS here because that list
# excludes docs/ and _docs/ which are valid sources of markdown documentation.
_ALWAYS_EXCLUDED_MD_DIRS = [
    # Dependencies (never contain useful docs)
    ".venv", "venv", "env", "virtualenv",
    "node_modules", "bower_components", "jspm_packages", "vendor",
    # Config directories (tooling config, not project content)
    ".config",
    # Version control
    ".git", ".svn", ".hg", ".bzr",
    # Cache directories
    "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache",
    # IDE directories
    ".idea", ".vscode", ".vs",
]


class MarkdownFinder:
    """Finds and loads markdown files from a repository for LLM context."""

    def __init__(self, repo_path: str):
        """
        Initialize the MarkdownFinder.

        Args:
            repo_path: Path to the repository.
        """
        self.repo_path = Path(repo_path)
        self._excluded_dirs = set(
            d.lower() for d in (_ALWAYS_EXCLUDED_MD_DIRS + EXCLUDED_MD_DIRS)
        )
        self._excluded_files = set(f.lower() for f in EXCLUDED_MD_FILES)

    def find_markdown_files(self) -> list[Path]:
        """
        Find all markdown files in the repository, excluding unwanted files/dirs.

        Returns:
            List of Path objects for markdown files, sorted by path.
        """
        md_files = []

        for md_file in self.repo_path.rglob("*.md"):
            # Check if any parent directory is excluded
            relative_path = md_file.relative_to(self.repo_path)
            parts_lower = [p.lower() for p in relative_path.parts]

            # Skip if in excluded directory
            if any(part in self._excluded_dirs for part in parts_lower[:-1]):
                continue

            # Skip if filename is excluded (case-insensitive)
            if md_file.name.lower() in self._excluded_files:
                continue

            md_files.append(md_file)

        # Sort by path for consistent ordering, prioritize root-level files
        return sorted(md_files, key=lambda p: (len(p.relative_to(self.repo_path).parts), str(p)))

    def load_markdown_context(self) -> list[dict]:
        """
        Load markdown files as context for LLM.

        Returns:
            List of dicts with 'file' (relative path) and 'content' keys.
            Respects MAX_MD_FILE_CHARS per file and MAX_TOTAL_MD_CONTEXT_CHARS total.
        """
        md_files = self.find_markdown_files()
        context = []
        total_chars = 0

        for md_file in md_files:
            if total_chars >= MAX_TOTAL_MD_CONTEXT_CHARS:
                break

            try:
                content = md_file.read_text(encoding="utf-8")
            except (UnicodeDecodeError, OSError):
                continue

            # Truncate individual file if too large
            if len(content) > MAX_MD_FILE_CHARS:
                content = content[:MAX_MD_FILE_CHARS] + "\n\n[... truncated ...]"

            # Check if adding this file would exceed total budget
            remaining = MAX_TOTAL_MD_CONTEXT_CHARS - total_chars
            if len(content) > remaining:
                content = content[:remaining] + "\n\n[... truncated ...]"

            relative_path = str(md_file.relative_to(self.repo_path))
            context.append({
                "file": relative_path,
                "content": content,
            })
            total_chars += len(content)

        return context

    def get_markdown_summary(self) -> str:
        """
        Get a formatted string of all markdown content for LLM context.

        Returns:
            Formatted string with file headers and content.
        """
        context = self.load_markdown_context()
        if not context:
            return ""

        parts = ["## Existing Documentation\n"]
        for doc in context:
            parts.append(f"### {doc['file']}\n")
            parts.append(doc["content"])
            parts.append("\n---\n")

        return "\n".join(parts)

