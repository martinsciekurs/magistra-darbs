---
sidebar_position: 515
---

# test_run_strategy_str

**File:** `tests/unit/indexing/operations/chunk_text/test_chunk_text.py` (lines 62-76)

## Signature

```python
def test_run_strategy_str()
```

## Description

Run the given chunking strategy on the input data and return the produced text chunks as strings.

Args:
- strategy_exec (Callable): The strategy function to execute to generate TextChunk objects. It should accept (input, config, tick) and return a list of TextChunk-like objects that expose a text_chunk attribute.
- input: str | list[str] | list[tuple[str, str]]: The input data to chunk. May be a single string, a list of strings, or a list of (document_id, text) tuples depending on the strategy.
- config: Any: Configuration for chunking, including size, overlap, and encoding model. This can be a real configuration object or a mock used in tests.
- tick: Any: Progress ticker used to report progress.

Returns:
- list[str]: The produced text chunks, extracted from each TextChunk as text_chunk, in the same order as produced by the strategy.

Raises:
- Propagates any exception raised by strategy_exec. If a produced chunk lacks a text_chunk attribute, an AttributeError may be raised.

Examples:
- run_strategy(my_strategy, "text", cfg, tick) -&gt; ["text"]

## Dependencies

This function calls:

- `graphrag/index/operations/chunk_text/chunk_text.py::run_strategy`
- `graphrag/index/operations/chunk_text/typing.py::TextChunk`

