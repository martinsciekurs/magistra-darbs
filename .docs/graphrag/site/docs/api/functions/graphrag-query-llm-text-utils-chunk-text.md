---
sidebar_position: 391
---

# chunk_text

**File:** `graphrag/query/llm/text_utils.py` (lines 36-42)

## Signature

```python
def chunk_text(text: str, max_tokens: int, tokenizer: Tokenizer | None = None)
```

## Description

Chunk text by token length.

Args:
    text (str): The input text to chunk.
    max_tokens (int): Maximum number of tokens per chunk.
    tokenizer (Tokenizer | None): Tokenizer to use for encoding/decoding. If None, a default tokenizer is obtained via get_tokenizer(encoding_model=defs.ENCODING_MODEL).

Returns:
    Iterator[str]: An iterator that yields chunk strings, each created by decoding token sequences with at most max_tokens tokens.

Raises:
    ValueError: If max_tokens &lt; 1.

## Dependencies

This function calls:

- `graphrag/query/llm/text_utils.py::batched`
- `graphrag/tokenizer/get_tokenizer.py::get_tokenizer`

