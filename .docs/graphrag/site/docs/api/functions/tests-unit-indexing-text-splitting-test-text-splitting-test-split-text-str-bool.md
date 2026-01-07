---
sidebar_position: 528
---

# test_split_text_str_bool

**File:** `tests/unit/indexing/text_splitting/test_text_splitting.py` (lines 41-45)

## Signature

```python
def test_split_text_str_bool()
```

## Description

Test that TokenTextSplitter.split_text returns an empty list when the input is None.

This test initializes a TokenTextSplitter with chunk_size=5 and chunk_overlap=2, calls split_text with None, and asserts that the result is [].

Returns:
    None: this test does not return a value.

Raises:
    AssertionError: if the result is not an empty list.

## Dependencies

This function calls:

- `graphrag/index/text_splitting/text_splitting.py::TokenTextSplitter`

