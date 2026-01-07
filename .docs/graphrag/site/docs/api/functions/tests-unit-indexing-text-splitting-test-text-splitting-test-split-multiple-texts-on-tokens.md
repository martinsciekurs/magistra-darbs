---
sidebar_position: 538
---

# test_split_multiple_texts_on_tokens

**File:** `tests/unit/indexing/text_splitting/test_text_splitting.py` (lines 113-129)

## Signature

```python
def test_split_multiple_texts_on_tokens()
```

## Description

Test that split_multiple_texts_on_tokens calls the tick callback when processing multiple texts.

This test creates a tokenizer configured with a mock tokenizer, passes two texts to split_multiple_texts_on_tokens, and asserts that the tick callback is invoked.

## Dependencies

This function calls:

- `graphrag/index/text_splitting/text_splitting.py::TokenChunkerOptions`
- `graphrag/index/text_splitting/text_splitting.py::split_multiple_texts_on_tokens`

