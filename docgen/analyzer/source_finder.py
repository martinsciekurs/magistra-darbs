"""SourceFinder - Find source files grouped by language using GitHub Linguist."""

import json
import subprocess
from fnmatch import fnmatch
from pathlib import Path

from docgen.utils.config import DEFAULT_EXCLUDED_DIRS, DEFAULT_EXCLUDED_FILES


class SourceFinder:
    """Finds source files in a Git repository grouped by programming language."""

    def __init__(self, repo_path: str, exclude_patterns: list[str] | None = None, respect_gitignore: bool = True):
        """
        Initialize the SourceFinder.

        Args:
            repo_path: Path to the Git repository.
            exclude_patterns: Optional list of glob patterns to exclude (e.g., ["test/*", "*.min.js"]).
            respect_gitignore: If True, also exclude files matching patterns in .gitignore.
        """
        self.repo_path = Path(repo_path)
        self.respect_gitignore = respect_gitignore
        
        # Build exclusion patterns from defaults + custom patterns
        self.exclude_patterns = self._build_exclude_patterns(exclude_patterns or [])
        self._files_by_language: dict[str, list[str]] | None = None

    def _build_exclude_patterns(self, custom_patterns: list[str]) -> list[str]:
        """Build the complete list of exclusion patterns."""
        patterns = []
        
        # Add directory patterns (match anywhere in path)
        for dir_name in DEFAULT_EXCLUDED_DIRS:
            patterns.append(f"{dir_name}/*")
            patterns.append(f"*/{dir_name}/*")
        
        # Add file patterns
        patterns.extend(DEFAULT_EXCLUDED_FILES)
        
        # Add gitignore patterns if enabled
        if self.respect_gitignore:
            patterns.extend(self._parse_gitignore())
        
        # Add custom patterns
        patterns.extend(custom_patterns)
        
        return patterns
    
    def _parse_gitignore(self) -> list[str]:
        """Parse .gitignore file and return patterns."""
        gitignore_path = self.repo_path / ".gitignore"
        if not gitignore_path.exists():
            return []
        
        patterns = []
        try:
            with open(gitignore_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    # Skip empty lines and comments
                    if not line or line.startswith('#'):
                        continue
                    # Convert gitignore patterns to fnmatch patterns
                    pattern = line.rstrip('/')
                    # Handle directory patterns (ending with /)
                    if line.endswith('/'):
                        patterns.append(f"{pattern}/*")
                        patterns.append(f"*/{pattern}/*")
                    else:
                        # Add pattern as-is and with wildcard prefix for nested matches
                        patterns.append(pattern)
                        if not pattern.startswith('*'):
                            patterns.append(f"*/{pattern}")
        except Exception:
            pass  # Silently ignore gitignore parsing errors
        
        return patterns

    @property
    def files_by_language(self) -> dict[str, list[str]]:
        """
        Returns files grouped by language.

        Returns:
            Dict mapping language name to list of file paths, sorted by file count descending.
            Example: {"Python": ["src/main.py", "src/utils.py"], "JavaScript": ["app.js"]}
        """
        if self._files_by_language is None:
            self._files_by_language = self._find_files()
        return self._files_by_language

    def _find_files(self) -> dict[str, list[str]]:
        """Run github-linguist and parse results."""
        result = subprocess.run(
            ["github-linguist", "--json", "--breakdown", str(self.repo_path)],
            capture_output=True, text=True
        )

        if result.returncode != 0 or not result.stdout:
            return {}

        linguist_data = json.loads(result.stdout)
        results: dict[str, list[str]] = {}

        for language, data in linguist_data.items():
            files = [f for f in data["files"] if not self._excluded(f)]
            if files:
                results[language] = sorted(files)

        # Sort by file count descending
        return dict(sorted(results.items(), key=lambda x: len(x[1]), reverse=True))

    def _excluded(self, path: str) -> bool:
        """Check if a path matches any exclusion pattern."""
        # Check each pattern
        for pattern in self.exclude_patterns:
            if fnmatch(path, pattern):
                return True
            # Also check if any path component matches a directory pattern
            if '/' not in pattern and not pattern.startswith('*'):
                # This is a simple name - check if it appears as a directory component
                parts = path.split('/')
                if pattern in parts[:-1]:  # Check all but filename
                    return True
        return False
