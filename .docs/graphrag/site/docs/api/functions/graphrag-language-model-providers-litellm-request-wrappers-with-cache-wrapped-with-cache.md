---
sidebar_position: 293
---

# _wrapped_with_cache

**File:** `graphrag/language_model/providers/litellm/request_wrappers/with_cache.py` (lines 48-76)

## Signature

```python
def _wrapped_with_cache(**kwargs: Any) -> Any
```

## Description

Synchronous cache wrapper for Litellm requests.

Args
----
kwargs: Any
    The keyword arguments forwarded to the wrapped synchronous function. This
    includes the streaming flag ('stream') and other inputs used to build the
    cache key. When streaming is requested, caching is bypassed and the
    underlying function is called directly.

Returns
-------
Any
    The response produced by the wrapped function. If a valid cached response is
    found, a corresponding ModelResponse or EmbeddingResponse is returned
    instead of calling the wrapped function.

Raises
------
Propagates exceptions raised by the wrapped function or by the cache
operations.

## Dependencies

This function calls:

- `graphrag/language_model/providers/litellm/get_cache_key.py::get_cache_key`

