---
sidebar_position: 98
---

# _prepare_embed_texts

**File:** `graphrag/index/operations/embed_text/strategies/openai.py` (lines 139-155)

## Signature

```python
def _prepare_embed_texts(
    input: list[str], splitter: TokenTextSplitter
) -> tuple[list[str], list[int]]
```

## Description

Prepare a flat list of text snippets to embed and their per-input sizes by splitting each input text.

Args:
    input: The list of input strings to process.
    splitter: The TokenTextSplitter used to split each input string into chunks.

Returns:
    tuple[list[str], list[int]]: A tuple (snippets, sizes) where:
        snippets: The concatenated list of non-empty split_texts produced from all inputs.
        sizes: A list containing, for each input string, the number of split_texts produced.

Raises:
    Propagates exceptions raised by splitter.split_text.

## Called By

This function is called by:

- `graphrag/index/operations/embed_text/strategies/openai.py::run`

