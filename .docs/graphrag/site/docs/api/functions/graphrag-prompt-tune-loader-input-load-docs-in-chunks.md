---
sidebar_position: 320
---

# load_docs_in_chunks

**File:** `graphrag/prompt_tune/loader/input.py` (lines 41-108)

## Signature

```python
def load_docs_in_chunks(
    config: GraphRagConfig,
    select_method: DocSelectionType,
    limit: int,
    logger: logging.Logger,
    chunk_size: int,
    overlap: int,
    n_subset_max: int = N_SUBSET_MAX,
    k: int = K,
) -> list[str]
```

## Description

Load documents into chunks for generating prompts.

Load documents from the configured input, convert them into base text units according
to the chunking configuration, and optionally sample or embed chunks to meet the
requested selection method. The function returns a list of chunk texts, with braces
escaped to avoid issues with Python's str.format when parsing LaTeX in markdown.

Args:
    config: GraphRagConfig The overall configuration for the graph-based RAG pipeline, including input sources and chunking options.
    select_method: DocSelectionType The strategy to select chunks: TOP, RANDOM, or AUTO.
    limit: int Maximum number of chunks to return. If out of range, a default is used.
    logger: logging.Logger Logger used to emit warnings and information during processing.
    chunk_size: int The size of each chunk.
    overlap: int The amount of overlap between consecutive chunks.
    n_subset_max: int Maximum number of chunks to sample when using AUTO selection (default N_SUBSET_MAX).
    k: int Number of chunks to select when using AUTO (must be &gt; 0 when AUTO is chosen).

Returns:
    list[str] A list containing the chunk texts. Each text has braces escaped by doubling
    braces to prevent the str.format parser from interpreting LaTeX or other content.

Raises:
    ValueError: If select_method is DocSelectionType.AUTO and k is not a positive integer.

## Dependencies

This function calls:

- `graphrag.cache.noop_pipeline_cache::NoopPipelineCache`
- `graphrag/callbacks/noop_workflow_callbacks.py::NoopWorkflowCallbacks`
- `graphrag/index/input/factory.py::create_input`
- `graphrag/index/workflows/create_base_text_units.py::create_base_text_units`
- `graphrag/prompt_tune/loader/input.py::_sample_chunks_from_embeddings`
- `graphrag/utils/api.py::create_storage_from_config`

## Called By

This function is called by:

- `graphrag/api/prompt_tune.py::generate_indexing_prompts`

