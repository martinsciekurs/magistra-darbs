---
sidebar_position: 533
---

# decode

**File:** `tests/unit/indexing/text_splitting/test_text_splitting.py` (lines 141-142)

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

