import os

# --- LLM Context Limits ---
MAX_FILE_TREE_CONTENT_CHARS = 200000  # ~50k tokens, leaves room for prompt/response
MAX_MD_FILE_CHARS = 10000             # Truncate large markdown files
MAX_TOTAL_MD_CONTEXT_CHARS = 50000    # Prevents context overflow with many MD files

# --- Runtime Settings ---
DEBUG = os.getenv("DEBUG", "false").lower() == "true"
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()  # DEBUG, INFO, WARNING, ERROR
ENABLE_EMBEDDINGS = os.getenv("ENABLE_EMBEDDINGS", "true").lower() == "true"
ENABLE_CODE_EXAMPLES = os.getenv("ENABLE_CODE_EXAMPLES", "true").lower() == "true"
CODE_EXAMPLE_MAX_RETRIES = int(os.getenv("CODE_EXAMPLE_MAX_RETRIES", "2"))

# --- HITL & Reflection Thresholds ---
HITL_CONFIDENCE_THRESHOLD = int(os.getenv("HITL_CONFIDENCE_THRESHOLD", "50"))
REFLECTION_CONFIDENCE_THRESHOLD = int(os.getenv("REFLECTION_CONFIDENCE_THRESHOLD", "70"))
MAX_REFLECTION_ITERATIONS = int(os.getenv("MAX_REFLECTION_ITERATIONS", "3"))
ENABLE_TOC_HITL = os.getenv("ENABLE_TOC_HITL", "true").lower() == "true"

# --- Markdown Exclusions ---
EXCLUDED_MD_FILES = [
    "CHANGELOG.md", "CHANGELOG", "HISTORY.md", "RELEASES.md", "RELEASE_NOTES.md",
    "LICENSE.md", "LICENSE", "CODE_OF_CONDUCT.md", "SECURITY.md",
    "ISSUE_TEMPLATE.md", "PULL_REQUEST_TEMPLATE.md", "CONTRIBUTING.md",
]

# Build output dirs (not source docs - we keep docs/ intentionally)
EXCLUDED_MD_DIRS = [
    "site", "_site", "public", "out",  # Static site build output
    "api-docs", "apidocs", "reference",  # Auto-generated API docs
    ".github",
]

# --- Default Exclusions ---
DEFAULT_EXCLUDED_DIRS = [
    # Virtual environments & package managers
    ".venv", "venv", "env", "virtualenv",
    "node_modules", "bower_components", "jspm_packages",
    ".config",
    # Version control
    ".git", ".svn", ".hg", ".bzr",
    # Cache & compiled
    "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache", ".coverage",
    # Build output
    "dist", "build", "out", "target", "bin", "obj",
    # Documentation & IDE
    "docs", "_docs", "site-docs", "_site",
    ".idea", ".vscode", ".vs", ".eclipse", ".settings",
    # Logs & temp
    "logs", "log", "tmp", "temp",
]

DEFAULT_EXCLUDED_FILES = [
    # Lock files
    "yarn.lock", "pnpm-lock.yaml", "npm-shrinkwrap.json", "poetry.lock",
    "Pipfile.lock", "requirements.txt.lock", "Cargo.lock", "composer.lock", "*.lock",
    # OS junk
    ".DS_Store", "Thumbs.db", "desktop.ini", "*.lnk",
    # Config & env
    ".env", ".env.*", "*.env", "*.cfg", "*.ini", ".flaskenv",
    ".gitignore", ".gitattributes", ".gitmodules", ".github", ".gitlab-ci.yml",
    ".prettierrc", ".eslintrc", ".eslintignore", ".stylelintrc",
    ".editorconfig", ".jshintrc", ".pylintrc", ".flake8", "mypy.ini",
    "pyproject.toml", "tsconfig.json", "webpack.config.js", "babel.config.js",
    "rollup.config.js", "jest.config.js", "karma.conf.js", "vite.config.js", "next.config.js",
    # Minified & bundled
    "*.min.js", "*.min.css", "*.bundle.js", "*.bundle.css", "*.map",
    # Archives
    "*.gz", "*.zip", "*.tar", "*.tgz", "*.rar", "*.7z", "*.iso", "*.dmg", "*.img",
    # Installers
    "*.msix", "*.appx", "*.appxbundle", "*.xap", "*.ipa", "*.deb", "*.rpm", "*.msi",
    # Binaries & compiled
    "*.exe", "*.dll", "*.so", "*.dylib", "*.o", "*.obj",
    "*.jar", "*.war", "*.ear", "*.jsm", "*.class",
    "*.pyc", "*.pyd", "*.pyo", "__pycache__",
    "*.a", "*.lib", "*.lo", "*.la", "*.slo", "*.dSYM",
    "*.egg", "*.egg-info", "*.dist-info", "*.eggs",
    "node_modules", "bower_components", "jspm_packages",
    # Coverage & build
    "lib-cov", "coverage", "htmlcov", ".nyc_output", ".tox",
    "dist", "build", "bld", "out", "bin", "target",
    "packages/*/dist", "packages/*/build", ".output",
]
