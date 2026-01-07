---
sidebar_position: 285
---

# _base_aembedding

**File:** `graphrag/language_model/providers/litellm/embedding_model.py` (lines 89-95)

## Signature

```python
def _base_aembedding(**kwargs: Any) -> EmbeddingResponse
```

## Description

Base asynchronous embedding wrapper that forwards to litellm.aembedding with merged base arguments.

Args
    kwargs: Any
        Additional keyword arguments to pass to the underlying aembedding call. The keys are merged with base_args, and the key "name" is removed from the resulting arguments if present before invocation.

Returns
    EmbeddingResponse
        The embedding response produced by aembedding, obtained by awaiting the underlying call with the merged arguments.

Raises
    Exception: Exceptions raised by aembedding may be propagated.

