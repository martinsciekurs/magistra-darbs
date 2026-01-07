---
sidebar_position: 530
---

# test_split_text_large_input

**File:** `tests/unit/indexing/text_splitting/test_text_splitting.py` (lines 55-63)

## Signature

```python
def test_split_text_large_input(mock_split)
```

## Description

Tests that TokenTextSplitter.split_text handles a large input by delegating to split_single_text_on_tokens and returning the expected number of chunks.

Args:
    mock_split: The patched mock for split_single_text_on_tokens used to simulate splitting behavior.

Returns:
    None

Raises:
    AssertionError: If the resulting number of chunks is not 2000 or if the patched function was not called exactly once. No exceptions are expected under normal execution.

## Dependencies

This function calls:

- `graphrag/index/text_splitting/text_splitting.py::TokenTextSplitter`

