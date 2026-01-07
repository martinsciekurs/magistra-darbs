---
sidebar_position: 172
---

# check_token_limit

**File:** `graphrag/index/text_splitting/check_token_limit.py` (lines 9-15)

## Signature

```python
def check_token_limit(text, max_token)
```

## Description

Check whether the input text fits within the specified token limit.

Args:
    text (str): The input text to check against the token limit.
    max_token (int): The maximum number of tokens allowed for a single chunk.

Returns:
    int: 1 if the text can be represented as a single chunk under the limit, 0 otherwise.

Raises:
    Exception: If an error occurs during tokenization/splitting using TokenTextSplitter.

## Dependencies

This function calls:

- `graphrag/index/text_splitting/text_splitting.py::TokenTextSplitter`

