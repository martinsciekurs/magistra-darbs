---
sidebar_position: 218
---

# chunker

**File:** `graphrag/index/workflows/create_base_text_units.py` (lines 86-128)

## Signature

```python
def chunker(row: pd.Series) -> Any
```

## Description

Chunk a row into text chunks, optionally prepending metadata to each chunk.

Args:
    row (pd.Series): The input row containing the data to be chunked. It is expected to have the 'texts' column, and may include 'metadata'. This function also relies on outer-scope configuration such as prepend_metadata, size, overlap, encoding_model, strategy, and callbacks.

Returns:
    pd.Series: The input row augmented with a 'chunks' field containing the list of text chunks (with metadata prepended if configured).

Raises:
    ValueError: Metadata tokens exceed the maximum tokens per chunk. Please increase the tokens per chunk.

## Dependencies

This function calls:

- `graphrag/index/operations/chunk_text/chunk_text.py::chunk_text`
- `graphrag/index/operations/chunk_text/strategies.py::get_encoding_fn`

## Called By

This function is called by:

- `graphrag/index/workflows/create_base_text_units.py::chunker_with_logging`

