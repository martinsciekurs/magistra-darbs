---
sidebar_position: 531
---

# test_token_text_splitter

**File:** `tests/unit/indexing/text_splitting/test_text_splitting.py` (lines 68-80)

## Signature

```python
def test_token_text_splitter(mock_tokenizer, mock_split_text)
```

## Description

Test that TokenTextSplitter.split_text delegates to split_single_text_on_tokens with the given text and tokenizer.

Parameters:
    mock_tokenizer (MagicMock): Patch object that mocks the tokenizer factory; its return_value is the mocked tokenizer used as the tokenizer argument to split_text.
    mock_split_text (MagicMock): Patch object for split_single_text_on_tokens; its return value is the expected list of chunks.

Returns:
    None: This test does not return a value.

Raises:
    AssertionError: If the expected call to split_single_text_on_tokens is not made with the correct arguments.

## Dependencies

This function calls:

- `graphrag/index/text_splitting/text_splitting.py::TokenTextSplitter`

