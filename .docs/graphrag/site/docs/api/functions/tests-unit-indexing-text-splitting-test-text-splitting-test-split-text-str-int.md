---
sidebar_position: 532
---

# test_split_text_str_int

**File:** `tests/unit/indexing/text_splitting/test_text_splitting.py` (lines 48-51)

## Signature

```python
def test_split_text_str_int()
```

## Description

Test that TokenTextSplitter.split_text raises TypeError when the input is an integer (non-string). 

Returns:
    None: this test does not return a value.

Raises:
    TypeError: if the input to split_text is not a string (e.g., an integer).

## Dependencies

This function calls:

- `graphrag/index/text_splitting/text_splitting.py::TokenTextSplitter`

