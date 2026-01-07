---
sidebar_position: 102
---

# _execute

**File:** `graphrag/index/operations/embed_text/strategies/openai.py` (lines 88-104)

## Signature

```python
def _execute(
    model: EmbeddingModel,
    chunks: list[list[str]],
    tick: ProgressTicker,
    semaphore: asyncio.Semaphore,
) -> list[list[float]]
```

## Description

Asynchronously embed batches of text chunks using the provided EmbeddingModel, honoring the concurrency limit with the supplied semaphore and reporting progress through the tick callback after processing each batch. The embeddings from all input chunks are flattened into a single 1D list of floats in batch order and returned.

Args:
  model: EmbeddingModel - The embedding model to use.
  chunks: list[list[str]] - A list of text chunks grouped into batches to embed.
  tick: ProgressTicker - Callback to report progress after each batch is processed.
  semaphore: asyncio.Semaphore - Semaphore controlling concurrent embedding calls.

Returns:
  list[float] - A flat list of embedding floats for all inputs, concatenated in batch order.

Raises:
  Exceptions raised by the embedding model (via model.aembed_batch) may be propagated to the caller.

## Dependencies

This function calls:

- `graphrag/index/operations/embed_text/strategies/openai.py::embed`

## Called By

This function is called by:

- `graphrag/index/operations/embed_text/strategies/openai.py::run`

