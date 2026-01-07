---
sidebar_position: 101
---

# _get_splitter

**File:** `graphrag/index/operations/embed_text/strategies/openai.py` (lines 79-85)

## Signature

```python
def _get_splitter(
    config: LanguageModelConfig, batch_max_tokens: int
) -> TokenTextSplitter
```

## Description

Get a TokenTextSplitter configured for the given language model configuration.

Args:
    config: LanguageModelConfig describing the model configuration used to select the tokenizer.
    batch_max_tokens: int representing the maximum number of tokens per chunk.

Returns:
    TokenTextSplitter: A text splitter initialized with a tokenizer built from the provided config and chunk_size equal to batch_max_tokens.

Raises:
    None

## Dependencies

This function calls:

- `graphrag/index/text_splitting/text_splitting.py::TokenTextSplitter`
- `graphrag/tokenizer/get_tokenizer.py::get_tokenizer`

## Called By

This function is called by:

- `graphrag/index/operations/embed_text/strategies/openai.py::run`

