---
sidebar_position: 74
---

# chunk_text

**File:** `graphrag/index/operations/chunk_text/chunk_text.py` (lines 19-79)

## Signature

```python
def chunk_text(
    input: pd.DataFrame,
    column: str,
    size: int,
    overlap: int,
    encoding_model: str,
    strategy: ChunkStrategyType,
    callbacks: WorkflowCallbacks,
) -> pd.Series
```

## Description

Chunk a piece of text into smaller pieces.

Args:
    input: DataFrame containing the data to chunk.
    column: The name of the column containing the text to chunk, this can either be a column with text, or a column with a list[tuple[doc_id, str]].
    size: The chunk size to use.
    overlap: The chunk overlap to use.
    encoding_model: The encoding model to use for chunking.
    strategy: The strategy to use to chunk the text, see below for more details.
    callbacks: WorkflowCallbacks for progress reporting.

Returns:
    A pandas Series where each element corresponds to the chunked result for the input row. Each element is a list of chunks; for string inputs, each item is a string text chunk. For inputs with document IDs, each item is a tuple of (doc_ids, text_chunk, n_tokens).

Raises:
    ValueError: If an unknown strategy is provided.

## Dependencies

This function calls:

- `graphrag/config/models/chunking_config.py::ChunkingConfig`
- `graphrag/index/operations/chunk_text/chunk_text.py::_get_num_total`
- `graphrag/index/operations/chunk_text/chunk_text.py::load_strategy`
- `graphrag/index/operations/chunk_text/chunk_text.py::run_strategy`
- `graphrag/logger/progress.py::progress_ticker`

## Called By

This function is called by:

- `graphrag/index/workflows/create_base_text_units.py::chunker`
- `tests/unit/indexing/operations/chunk_text/test_chunk_text.py::test_chunk_text`

