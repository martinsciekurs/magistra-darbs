---
sidebar_position: 563
---

# test_num_tokens_empty_input

**File:** `tests/unit/utils/test_encoding.py` (lines 14-18)

## Signature

```python
def test_num_tokens_empty_input()
```

## Description

Test that the tokenizer returns zero tokens for an empty string.

Returns:
    None

Raises:
    AssertionError: If the token count for empty input is not zero.

## Dependencies

This function calls:

- `graphrag/tokenizer/get_tokenizer.py::get_tokenizer`

