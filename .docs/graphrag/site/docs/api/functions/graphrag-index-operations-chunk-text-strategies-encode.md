---
sidebar_position: 75
---

# encode

**File:** `graphrag/index/operations/chunk_text/strategies.py` (lines 24-27)

## Signature

```python
def encode(text: str) -> list[int]
```

## Description

Encode the input text into token IDs using the configured encoding model.

Args:
    text (str): The input to encode. If not a string, it will be converted to a string.

Returns:
    list[int]: The encoded token IDs produced by the encoding model.

Raises:
    Exception: If encoding fails with the configured encoding model.

