---
sidebar_position: 290
---

# _hash

**File:** `graphrag/language_model/providers/litellm/get_cache_key.py` (lines 138-140)

## Signature

```python
def _hash(input: str) -> str
```

## Description

Generate a SHA-256 hash for the input string.

Args:
    input: str - the input string to hash

Returns:
    str - hexadecimal digest of the SHA-256 hash of the input

Raises:
    AttributeError - if the input object does not support the encode() method

## Called By

This function is called by:

- `graphrag/language_model/providers/litellm/get_cache_key.py::get_cache_key`

