---
sidebar_position: 516
---

# test_run_strategy_arr_str

**File:** `tests/unit/indexing/operations/chunk_text/test_chunk_text.py` (lines 79-98)

## Signature

```python
def test_run_strategy_arr_str()
```

## Description

Run the given chunking strategy on the input data and return the produced chunks.

Args:
    strategy_exec: ChunkStrategy
        The strategy function to execute to generate TextChunk objects. It should accept
        (input, config, tick) and return a list of TextChunk-like objects that expose a
        text_chunk attribute.
    input: ChunkInput
        The input data to chunk. May be a string or a list of strings, or a list of tuples
        of (document_id, text content).
    config: ChunkingConfig
        Configuration for chunking, including size, overlap, and encoding model.
    tick: ProgressTicker
        Progress ticker used during execution.

Returns:
    list[str | tuple[list[str] | None, str, int]]
    The produced chunks. Each element is either a string (for string-based input) or a tuple
    of the form (list[str] | None, str, int) representing the chunked content, a representative
    text, and the token count for that chunk.

## Dependencies

This function calls:

- `graphrag/index/operations/chunk_text/chunk_text.py::run_strategy`
- `graphrag/index/operations/chunk_text/typing.py::TextChunk`

