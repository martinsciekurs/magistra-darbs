# DocGen Core

Core documentation generation package using static analysis and LLM.

## Usage

```bash
# Install from project root
pip install -e .

# Run from project root (outputs to .docs/<repo_name>/)
docgen <repo> [options]
```

> **Note:** The `docgen` CLI is defined in `pyproject.toml` under `[project.scripts]`. After `pip install`, it's available globally in your virtualenv. Always run from the project root since output goes to `.docs/` in the current directory.

**Options:**
- `--start-server`: Start Docusaurus dev server after generation
- `--force`: Force regeneration, ignoring caches
- `--commit <ref>`: Checkout specific commit/tag/branch
- `--rerun <stages>`: Re-run specific stages (modules, synthesis, site)

**Examples:**
```bash
docgen https://github.com/user/repo --start-server
docgen ./local-repo --force
docgen myrepo --rerun synthesis site
```

## Architecture

```
docgen/
├── main.py              # CLI entry point
├── analyzer/            # Static code analysis
│   ├── code_parser.py   # Tree-sitter parsing
│   ├── source_finder.py # Language detection (Linguist)
│   ├── call_resolver.py # Function call resolution
│   └── topological_sort.py
├── llm/                 # LLM integration
│   ├── client.py        # Multi-provider LLM client
│   ├── prompts.py       # Prompt templates
│   ├── embeddings.py    # ChromaDB + RAG
│   └── graph/           # LangGraph pipeline
├── utils/               # Shared utilities
│   ├── config.py        # Configuration
│   ├── generate_docs.py # Docusaurus generation
│   └── repo_fetcher.py  # Git operations
└── scripts/             # Helper scripts
```

## How It Works

### Phase 1: Static Analysis

1. **Repository Discovery** - GitHub Linguist identifies source files by language
2. **Code Parsing** - Tree-sitter extracts functions, classes, imports
3. **Call Graph** - Resolves function calls, builds dependency relationships
4. **Topological Sort** - Orders functions so dependencies are documented first

### Phase 2: LangGraph Pipeline

```
START → analyze_repo → evaluate_repo → [hitl_feedback] → document_functions
      → group_classes → doc_classes → group_files → doc_files
      → group_modules → doc_modules → gen_architecture → propose_toc
      → [hitl_toc] → synthesize → END
```

| Node | Description | Output |
|------|-------------|--------|
| `analyze_repo` | High-level repo analysis | `4_llm_summary.yaml` |
| `document_functions` | Document each function (with RAG) | `5_function_docs.yaml` |
| `group_classes` | Group functions by class | `6_class_groups.yaml` |
| `doc_classes` | Document classes | `7_class_docs.yaml` |
| `group_files` | Group by source file | `8_file_groups.yaml` |
| `doc_files` | Document files | `9_file_docs.yaml` |
| `group_modules` | Group by architectural module | `10_module_groups.yaml` |
| `doc_modules` | Document modules | `11_module_docs.yaml` |
| `gen_architecture` | Generate Mermaid diagram | `12_architecture_diagram.yaml` |
| `propose_toc` | Propose documentation structure | `13_proposed_toc.yaml` |
| `synthesize` | Generate final docs | `15_synthesis_doc.yaml` |

### Key Features

**Dependency-Ordered Documentation**
- Functions documented in topological order
- When documenting F, all functions F calls are already documented
- LLM sees documentation of dependencies, not just code

**RAG (Retrieval-Augmented Generation)**
- ChromaDB stores function embeddings
- Similar functions retrieved for style consistency
- Provider-specific embeddings (OpenAI/Ollama)

**Crash Recovery**
- Each node saves results incrementally to YAML
- LangGraph checkpoints state to SQLite
- Re-running resumes from last checkpoint

**Schema Validation**
- YAML outputs validated against schemas
- Invalid outputs trigger automatic LLM repair (up to 3 retries)

## Generated Site Structure

```
.docs/<repo>/site/docs/
├── index.md              # Landing page
├── guide/                # Conceptual docs
│   ├── introduction.md
│   ├── quick-start.md
│   └── architecture.md   # + Mermaid diagram
├── modules/              # Module docs
├── files/                # File docs
└── api/                  # API reference
    ├── classes/
    └── functions/
```

## Configuration

Environment variables (`.env`):
```bash
# LLM Provider
LLM_PROVIDER=openai          # openai, anthropic, ollama
LLM_MODEL=gpt-4o-mini
OPENAI_API_KEY=sk-...

# Optional: Langfuse observability
LANGFUSE_PUBLIC_KEY=pk-...
LANGFUSE_SECRET_KEY=sk-...
```

See `utils/config.py` for all options.

## Observability

Optional Langfuse integration tracks:
- All LLM calls (prompts, responses, tokens)
- Embedding operations
- Performance metrics

Enable by setting Langfuse credentials in `.env`.
