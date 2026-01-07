---
sidebar_position: 96
---

# run

**File:** `graphrag/index/operations/embed_text/strategies/mock.py` (lines 16-29)

## Signature

```python
def run(  # noqa RUF029 async is required for interface
    input: list[str],
    callbacks: WorkflowCallbacks,
    cache: PipelineCache,
    _args: dict[str, Any],
) -> TextEmbeddingResult
```

## Description

Run the embedding generation for the given texts using a mock strategy. This asynchronous function processes an input collection of texts and returns a TextEmbeddingResult containing embeddings for each input text. It reports progress via a progress ticker and uses the _embed_text helper to generate a 3-dimensional embedding per text.

Parameters
    input: Iterable[str]
        The input texts to embed. Note: strings are Iterable; if a single string is passed, it will be treated as an iterable of characters unless wrapped in a collection of strings.
    callbacks: WorkflowCallbacks
        Callback hooks invoked for progress updates.
    cache: PipelineCache
        Cache used for embedding operations.
    _args: dict[str, Any]
        Additional optional arguments.

Returns
    TextEmbeddingResult: Result containing embeddings for the input texts. Each embedding is a list[float] of length 3.

Raises
    This function may raise exceptions propagated from the progress ticker or the embedding operation. No exceptions are guaranteed.

## Dependencies

This function calls:

- `graphrag/index/operations/embed_text/strategies/mock.py::_embed_text`
- `graphrag/index/operations/embed_text/strategies/typing.py::TextEmbeddingResult`
- `graphrag/logger/progress.py::progress_ticker`

