---
sidebar_position: 522
---

# test_chunk_text

**File:** `tests/unit/indexing/operations/chunk_text/test_chunk_text.py` (lines 164-181)

## Signature

```python
def test_chunk_text(mock_progress_ticker, mock_run_strategy, mock_load_strategy)
```

## Description

Chunk a piece of text into smaller pieces.

This function chunks the text contained in the specified DataFrame column into smaller pieces according to the given chunking strategy and encoding model. It loads the configured chunking strategy, processes the input texts, and reports progress via the provided callbacks. The function returns a pandas Series containing the resulting chunks.

Args:
    input (pd.DataFrame): DataFrame containing the data to chunk.
    column (str): The name of the column containing the text to chunk. This can be a column with plain text, or a column with a list/tuple of (doc_id, text).
    size (int): The chunk size in tokens.
    overlap (int): The number of tokens to overlap between adjacent chunks.
    encoding_model (str): The encoding model to use for chunking.
    strategy (ChunkStrategyType): The strategy to use for chunking (e.g., sentence, word). See graphrag.config.enums.ChunkStrategyType for supported values.
    callbacks (WorkflowCallbacks): Object exposing progress reporting callbacks (e.g., a progress attribute or method).

Returns:
    pd.Series: A Series containing the generated chunks. The exact shape depends on the input and strategy.

Raises:
    ValueError: If an unknown or unsupported strategy is provided.

Examples:
    chunk_text(df, "text", size=10, overlap=2, encoding_model="model", strategy=ChunkStrategyType.sentence, callbacks=my_callbacks)

## Dependencies

This function calls:

- `graphrag/index/operations/chunk_text/chunk_text.py::chunk_text`

