---
sidebar_position: 529
---

# encode

**File:** `tests/unit/indexing/text_splitting/test_text_splitting.py` (lines 136-139)

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
    Exception: If encoding fails with the configured encoding model....

## Called By

This function is called by:

- `tests/unit/indexing/text_splitting/test_text_splitting.py::test_split_single_text_on_tokens_no_overlap`

