---
sidebar_position: 294
---

# _wrapped_with_cache_async

**File:** `graphrag/language_model/providers/litellm/request_wrappers/with_cache.py` (lines 78-105)

## Signature

```python
def _wrapped_with_cache_async(
        **kwargs: Any,
    ) -> Any
```

## Description

Asynchronous cache wrapper for Litellm requests.

Args:
    kwargs: Any
        The keyword arguments forwarded to the wrapped asynchronous function. This includes the streaming flag ('stream') and other inputs used to build the cache key. When streaming is requested, caching is bypassed and the underlying function is called directly.

Returns:
    Any
        The response produced by the wrapper. This may be a ModelResponse or EmbeddingResponse constructed from a cached entry, or the result of the wrapped asynchronous function. When streaming is requested, the underlying function is called directly and no caching is performed.

Raises:
    Exception
        Exceptions raised by the underlying asynchronous function or by cache operations.

## Dependencies

This function calls:

- `graphrag/language_model/providers/litellm/get_cache_key.py::get_cache_key`

