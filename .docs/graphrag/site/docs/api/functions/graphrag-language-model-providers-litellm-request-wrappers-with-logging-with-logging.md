---
sidebar_position: 297
---

# with_logging

**File:** `graphrag/language_model/providers/litellm/request_wrappers/with_logging.py` (lines 17-56)

## Signature

```python
def with_logging(
    *,
    sync_fn: LitellmRequestFunc,
    async_fn: AsyncLitellmRequestFunc,
) -> tuple[LitellmRequestFunc, AsyncLitellmRequestFunc]
```

## Description

Wrap the provided synchronous and asynchronous Litellm request functions with logging for exceptions.

Args
----
    sync_fn: LitellmRequestFunc
        The synchronous chat/embedding request function to wrap.
    async_fn: AsyncLitellmRequestFunc
        The asynchronous chat/embedding request function to wrap.

Returns
-------
tuple[LitellmRequestFunc, AsyncLitellmRequestFunc]
        A tuple containing the wrapped synchronous and asynchronous chat/embedding request functions.

Raises
------
Exception
        If either wrapped function raises an exception, the exception is logged via logger.exception and re-raised.

## Called By

This function is called by:

- `graphrag/language_model/providers/litellm/chat_model.py::_create_completions`
- `graphrag/language_model/providers/litellm/embedding_model.py::_create_embeddings`

