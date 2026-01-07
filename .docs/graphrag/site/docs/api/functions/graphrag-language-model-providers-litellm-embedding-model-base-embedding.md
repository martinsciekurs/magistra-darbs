---
sidebar_position: 286
---

# _base_embedding

**File:** `graphrag/language_model/providers/litellm/embedding_model.py` (lines 81-87)

## Signature

```python
def _base_embedding(**kwargs: Any) -> EmbeddingResponse
```

## Description

Base synchronous embedding wrapper that forwards to litellm.embedding with merged base arguments.

Args
    kwargs: Any
        Additional keyword arguments to pass to the underlying embedding function. The keys are merged with base_args, and if the resulting dictionary contains the key "name", it will be removed before invocation.

Returns
    EmbeddingResponse
        The embedding response produced by the underlying embedding call.

Raises
    Exception
        Propagates exceptions raised by the underlying embedding function.

