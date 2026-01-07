---
sidebar_position: 537
---

# test_split_single_text_on_tokens_no_overlap

**File:** `tests/unit/indexing/text_splitting/test_text_splitting.py` (lines 132-170)

## Signature

```python
def test_split_single_text_on_tokens_no_overlap()
```

## Description

Split a single text into chunks using the provided tokenizer.

Args:
    text (str): The input text to split into chunks.
    tokenizer (TokenChunkerOptions): The tokenizer configuration used to encode the text into tokens and decode chunks. It must provide encode, decode, tokens_per_chunk, and chunk_overlap.

Returns:
    list[str]: The list of chunked text strings produced.

Raises:
    Exception: If the underlying tokenizer raises an error during encoding or decoding operations.

## Dependencies

This function calls:

- `graphrag/index/text_splitting/text_splitting.py::TokenChunkerOptions`
- `graphrag/index/text_splitting/text_splitting.py::split_single_text_on_tokens`
- `tests/unit/indexing/text_splitting/test_text_splitting.py::encode`

