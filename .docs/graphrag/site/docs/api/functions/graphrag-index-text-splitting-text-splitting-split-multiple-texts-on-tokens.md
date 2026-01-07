---
sidebar_position: 173
---

# split_multiple_texts_on_tokens

**File:** `graphrag/index/text_splitting/text_splitting.py` (lines 142-173)

## Signature

```python
def split_multiple_texts_on_tokens(
    texts: list[str], tokenizer: TokenChunkerOptions, tick: ProgressTicker
) -> list[TextChunk]
```

## Description

Split multiple texts and return chunks with metadata using the tokenizer.

Args:
    texts: list[str] The texts to split into chunks.
    tokenizer: TokenChunkerOptions The tokenizer configuration used to encode texts into tokens and decode chunks.
    tick: ProgressTicker A callback function to track progress. If provided, tick(1) is called for each processed text.

Returns:
    list[TextChunk] A list of TextChunk objects. Each TextChunk contains the chunk_text, the indices of source documents contributing to the chunk, and the number of tokens in the chunk.

## Dependencies

This function calls:

- `graphrag/index/operations/chunk_text/typing.py::TextChunk`

## Called By

This function is called by:

- `graphrag/index/operations/chunk_text/strategies.py::run_tokens`
- `tests/unit/indexing/text_splitting/test_text_splitting.py::test_split_multiple_texts_on_tokens`

