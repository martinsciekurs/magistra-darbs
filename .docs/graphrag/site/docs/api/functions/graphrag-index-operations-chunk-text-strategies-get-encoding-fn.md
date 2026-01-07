---
sidebar_position: 78
---

# get_encoding_fn

**File:** `graphrag/index/operations/chunk_text/strategies.py` (lines 20-32)

## Signature

```python
def get_encoding_fn(encoding_name)
```

## Description

Get encoding functions for a given encoding model.

Args:
- encoding_name: str - The name of the encoding model to retrieve via tiktoken.get_encoding.

Returns:
- encode, decode: tuple of callables
  - encode: Callable[[str], list[int]] - Encodes input text into token ids using the selected encoding; if input is not a string, it is converted to string.
  - decode: Callable[[list[int]], str] - Decodes a list of token ids back into a string using the selected encoding.

Raises:
- Exception: Propagates exceptions raised by tiktoken.get_encoding when an invalid encoding_name is provided.

## Called By

This function is called by:

- `graphrag/index/operations/chunk_text/strategies.py::run_tokens`
- `graphrag/index/workflows/create_base_text_units.py::chunker`
- `tests/unit/indexing/operations/chunk_text/test_strategies.py::test_get_encoding_fn_encode`
- `tests/unit/indexing/operations/chunk_text/test_strategies.py::test_get_encoding_fn_decode`

