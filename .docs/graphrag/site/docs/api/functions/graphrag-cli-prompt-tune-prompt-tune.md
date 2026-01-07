---
sidebar_position: 31
---

# prompt_tune

**File:** `graphrag/cli/prompt_tune.py` (lines 25-117)

## Signature

```python
def prompt_tune(
    root: Path,
    config: Path | None,
    domain: str | None,
    verbose: bool,
    selection_method: api.DocSelectionType,
    limit: int,
    max_tokens: int,
    chunk_size: int,
    overlap: int,
    language: str | None,
    discover_entity_types: bool,
    output: Path,
    n_subset_max: int,
    k: int,
    min_examples_required: int,
)
```

## Description

Prompt tune the model asynchronously.

Note: This coroutine must be awaited. It loads the configuration, applies any chunking overrides, initializes the root logger according to the verbose flag, and generates indexing prompts. It writes the resulting prompts to the specified output directory if an output path is provided; otherwise it logs an error and skips writing. Returns None upon successful completion.

Args:
    root: Path — The root directory to resolve relative paths from.
    config: Path | None — Optional path to the configuration file.
    domain: str | None — The domain to map the input documents to.
    verbose: bool — Enable verbose logging.
    selection_method: api.DocSelectionType — The chunk selection method.
    limit: int — The limit of chunks to load.
    max_tokens: int — The maximum number of tokens to use on entity extraction prompts.
    chunk_size: int — The chunk token size to use.
    overlap: int — The number of tokens to overlap between consecutive chunks.
    language: str | None — The language to use for the prompts.
    discover_entity_types: bool — Generate entity types.
    output: Path — The output folder to store the prompts.
    n_subset_max: int — The number of text chunks to embed when using auto selection method.
    k: int — The number of documents to select when using auto selection method.
    min_examples_required: int — The minimum number of examples required for entity extraction prompts.

Returns:
    None

Raises:
    Exceptions raised by underlying IO or configuration loading may propagate.

## Dependencies

This function calls:

- `graphrag.api::generate_indexing_prompts`
- `graphrag/config/load_config.py::load_config`
- `graphrag/logger/standard_logging.py::init_loggers`
- `graphrag/utils/cli.py::redact`

## Called By

This function is called by:

- `graphrag/cli/main.py::_prompt_tune_cli`

