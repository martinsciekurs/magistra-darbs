---
sidebar_position: 174
---

# split_single_text_on_tokens

**File:** `graphrag/index/text_splitting/text_splitting.py` (lines 119-137)

## Signature

```python
def split_single_text_on_tokens(text: str, tokenizer: TokenChunkerOptions) -> list[str]
```

## Description

Split a single text into chunks using the provided tokenizer.

Args:
    text: str The input text to split into chunks.
    tokenizer: TokenChunkerOptions The tokenizer configuration used to encode the text into tokens and decode chunks. It must provide encode, decode, tokens_per_chunk, and chunk_overlap.

Returns:
    list[str] The list of chunked text strings produced.

Raises:
    Exception: If the underlying tokenizer raises an error during encoding or decoding operations.

## Called By

This function is called by:

- `graphrag/index/text_splitting/text_splitting.py::TokenTextSplitter.split_text`
- `tests/unit/indexing/text_splitting/test_text_splitting.py::test_split_single_text_on_tokens`
- `tests/unit/indexing/text_splitting/test_text_splitting.py::test_split_single_text_on_tokens_no_overlap`

