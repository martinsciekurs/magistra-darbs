---
sidebar_position: 100
---

# embed

**File:** `graphrag/index/operations/embed_text/strategies/openai.py` (lines 94-99)

## Signature

```python
def embed(chunk: list[str])
```

## Description

Async helper to embed a batch of text chunks using the embedding model with a concurrency guard.

Args:
  chunk: A batch of text chunks to embed.

Returns:
  numpy.ndarray: The embeddings for the input chunks as a 2D NumPy array.

Raises:
  Exceptions raised by the embedding model (via model.aembed_batch) may be propagated to the caller.

## Called By

This function is called by:

- `graphrag/index/operations/embed_text/strategies/openai.py::_execute`

