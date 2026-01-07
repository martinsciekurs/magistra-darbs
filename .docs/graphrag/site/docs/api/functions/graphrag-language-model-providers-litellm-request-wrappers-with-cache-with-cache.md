---
sidebar_position: 292
---

# with_cache

**File:** `graphrag/language_model/providers/litellm/request_wrappers/with_cache.py` (lines 22-107)

## Signature

```python
def with_cache(
    *,
    sync_fn: LitellmRequestFunc,
    async_fn: AsyncLitellmRequestFunc,
    model_config: "LanguageModelConfig",
    cache: "PipelineCache",
    request_type: Literal["chat", "embedding"],
    cache_key_prefix: str,
) -> tuple[LitellmRequestFunc, AsyncLitellmRequestFunc]
```

## Description

Cache wrapper for Litellm request functions.

Args
----
    sync_fn: The synchronous chat/embedding request function to wrap.
    async_fn: The asynchronous chat/embedding request function to wrap.
    model_config: The configuration for the language model.
    cache: The cache to use for storing responses.
    request_type: The type of request being made, either "chat" or "embedding".
    cache_key_prefix: The prefix to use for cache keys.

Returns
-------
    A tuple containing the wrapped synchronous and asynchronous chat/embedding request functions.

Raises
------
    Exceptions raised by the underlying sync_fn/async_fn or by the cache operations.

## Called By

This function is called by:

- `graphrag/language_model/providers/litellm/chat_model.py::_create_completions`
- `graphrag/language_model/providers/litellm/embedding_model.py::_create_embeddings`

