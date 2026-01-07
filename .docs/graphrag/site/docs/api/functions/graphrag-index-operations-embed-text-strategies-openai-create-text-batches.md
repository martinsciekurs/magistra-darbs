---
sidebar_position: 99
---

# _create_text_batches

**File:** `graphrag/index/operations/embed_text/strategies/openai.py` (lines 107-136)

## Signature

```python
def _create_text_batches(
    texts: list[str],
    max_batch_size: int,
    max_batch_tokens: int,
    splitter: TokenTextSplitter,
) -> list[list[str]]
```

## Description

Create batches of texts to embed.

This function groups input texts into batches that respect the given batch constraints. A batch is closed when adding the next text would exceed the maximum number of texts or the maximum token count for the batch.

Args:
    texts: List of input texts to be batched.
    max_batch_size: Maximum number of texts per batch.
    max_batch_tokens: Maximum total tokens per batch, as measured by the splitter.
    splitter: TokenTextSplitter used to count tokens per text.

Returns:
    A list of batches, where each batch is a list of strings.

## Called By

This function is called by:

- `graphrag/index/operations/embed_text/strategies/openai.py::run`

