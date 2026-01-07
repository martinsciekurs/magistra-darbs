# DocGen

Generate documentation for repositories using static analysis and LLM.

## Project Structure

```
DocGen/
├── docgen/              # Core documentation generation package
├── web/                 # Web interface (FastAPI + React)
├── eval/                # Evaluation & benchmarking tools
└── tests/               # Test suite
```

## Quick Start

```bash
# Requirements: Python 3.12+, Ruby (for GitHub Linguist)
gem install github-linguist
pip install -e .

# Generate documentation (<repo> = GitHub URL, git URL, or local path)
docgen <repo>
docgen <repo> --start-server  # Generate and start dev server
```

## Components

| Component | Description | Documentation |
|-----------|-------------|---------------|
| **docgen/** | Core pipeline: static analysis, LLM integration, Docusaurus generation | [docgen/README.md](docgen/README.md) |
| **web/** | Web UI for monitoring and controlling documentation generation | [web/README.md](web/README.md) |
| **eval/** | Tools for evaluating documentation quality | [eval/README.md](eval/README.md) |

## Development

```bash
pip install -e ".[dev]"
pytest
```

## Output

Generated documentation is saved to `.docs/<repo_name>/`:
- `site/` - Docusaurus site (run `npm start` inside)
- `*.yaml` - Intermediate artifacts for debugging
