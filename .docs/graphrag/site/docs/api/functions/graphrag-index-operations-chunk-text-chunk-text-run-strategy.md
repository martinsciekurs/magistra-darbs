---
sidebar_position: 72
---

# run_strategy

**File:** `graphrag/index/operations/chunk_text/chunk_text.py` (lines 82-111)

## Signature

```python
def run_strategy(
    strategy_exec: ChunkStrategy,
    input: ChunkInput,
    config: ChunkingConfig,
    tick: ProgressTicker,
) -> list[str | tuple[list[str] | None, str, int]]
```

## Description

Run the given chunking strategy on the input data and return the produced chunks.

Args:
    strategy_exec: ChunkStrategy
        The strategy function to execute to generate text chunks.
    input: ChunkInput
        The input data to chunk. May be a string or a list of strings, or a list
        of tuples of (document_id, text content).
    config: ChunkingConfig
        Configuration for chunking, including size, overlap, and encoding model.
    tick: ProgressTicker
        Progress ticker used to report progress.

Returns:
    list[str | tuple[list[str] | None, str, int]]
        A list of results. If the input was a simple string, returns a list of
        text_chunk strings. Otherwise each element is either:
        - a text_chunk string, or
        - a tuple (doc_ids, text_chunk, n_tokens) where doc_ids is a list of
          document ids corresponding to the source documents for that chunk,
          text_chunk is the chunk text, and n_tokens is the number of tokens
          in the chunk.

## Called By

This function is called by:

- `graphrag/index/operations/chunk_text/chunk_text.py::chunk_text`
- `tests/unit/indexing/operations/chunk_text/test_chunk_text.py::test_run_strategy_str`
- `tests/unit/indexing/operations/chunk_text/test_chunk_text.py::test_run_strategy_arr_str`
- `tests/unit/indexing/operations/chunk_text/test_chunk_text.py::test_run_strategy_arr_tuple`
- `tests/unit/indexing/operations/chunk_text/test_chunk_text.py::test_run_strategy_arr_tuple_same_doc`

