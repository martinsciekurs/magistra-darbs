---
sidebar_position: 95
---

# _embed_text

**File:** `graphrag/index/operations/embed_text/strategies/mock.py` (lines 32-35)

## Signature

```python
def _embed_text(_cache: PipelineCache, _text: str, tick: ProgressTicker) -> list[float]
```

## Description

Embed a single piece of text.

Args:
    _cache: PipelineCache: Cache used for embedding operations.
    _text: str: Text to embed.
    tick: ProgressTicker: Progress ticker to report progress.

Returns:
    list[float]: Embedding vector as a list of three floats.

Raises:
    This function does not raise any exceptions.

## Called By

This function is called by:

- `graphrag/index/operations/embed_text/strategies/mock.py::run`

