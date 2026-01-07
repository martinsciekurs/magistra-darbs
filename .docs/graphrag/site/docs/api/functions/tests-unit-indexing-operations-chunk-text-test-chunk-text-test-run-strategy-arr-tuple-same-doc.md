---
sidebar_position: 518
---

# test_run_strategy_arr_tuple_same_doc

**File:** `tests/unit/indexing/operations/chunk_text/test_chunk_text.py` (lines 131-158)

## Signature

```python
def test_run_strategy_arr_tuple_same_doc()
```

## Description

Run the given chunking strategy on the input data and return the produced chunks.

Args:
    strategy_exec (ChunkStrategy): The strategy function to execute to generate TextChunk-like objects. It should accept (input, config, tick) and return a list of objects exposing a text_chunk attribute.
    input (ChunkInput): The input data to chunk. May be a string or a list of strings, or a list of tuples (text, token) as used in tests.
    config (ChunkingConfig): Configuration for chunking, including size, overlap, and encoding model.
    tick (ProgressTicker): Progress ticker used to report progress.

Returns:
    list[str | tuple[list[str] | None, str, int]]: A list of produced chunks. Each item is either a string or a tuple where
        the first element is a list of source texts (or None), the second element is the text chunk content, and the
        third element is the number of tokens.

Raises:
    Propagates exceptions raised by strategy_exec or invalid input processing.

## Dependencies

This function calls:

- `graphrag/index/operations/chunk_text/chunk_text.py::run_strategy`
- `graphrag/index/operations/chunk_text/typing.py::TextChunk`

