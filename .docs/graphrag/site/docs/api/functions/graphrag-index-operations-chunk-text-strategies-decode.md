---
sidebar_position: 76
---

# decode

**File:** `graphrag/index/operations/chunk_text/strategies.py` (lines 29-30)

## Signature

```python
def decode(tokens: list[int]) -> str
```

## Description

Decode a list of tokens back into a string.

Args:
    tokens (list[int]): A list of tokens to decode.

Returns:
    str: The decoded string from the list of tokens.

Raises:
    Exception: If decoding fails due to an underlying error in the encoding.

