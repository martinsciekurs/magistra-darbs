---
sidebar_position: 523
---

# test_get_encoding_fn_encode

**File:** `tests/unit/indexing/operations/chunk_text/test_strategies.py` (lines 94-109)

## Signature

```python
def test_get_encoding_fn_encode(mock_get_encoding)
```

## Description

Get encoding functions for a given encoding model.

Args:
- encoding_name: str - The name of the encoding model to retrieve via tiktoken.get_encoding.

Returns:
- encode, decode: tuple of callables
  - encode: Callable[[str], list[int]] - Encodes input text into token ids using the selected encoding; if input is not a string, it is converted to string.
  - decode: Callable[[list[int]], str] - Decodes a list of token ids back into a string using the selected encoding.

## Dependencies

This function calls:

- `graphrag/index/operations/chunk_text/strategies.py::get_encoding_fn`

