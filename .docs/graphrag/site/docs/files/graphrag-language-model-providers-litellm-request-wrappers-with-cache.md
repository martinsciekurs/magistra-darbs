---
sidebar_position: 152
---

# graphrag/language_model/providers/litellm/request_wrappers/with_cache.py

## Overview

Cache wrappers for Litellm request functions.

Purpose
This module provides a cache layer for Litellm chat and embedding requests. It offers a factory function named with_cache that returns wrapped synchronous and asynchronous request callables bound to a PipelineCache. The wrappers compute a cache key via get_cache_key and honor the request_type ('chat' or 'embedding'). When streaming is requested, caching is bypassed and the underlying function is invoked directly.

Key exports
- with_cache: Cache wrapper factory for Litellm request functions. Returns a tuple (sync_fn, async_fn) wrapped to use the provided cache and cache key prefix.
- _wrapped_with_cache: Synchronous cache wrapper. Receives the same inputs as the wrapped function and bypasses the cache when stream is True.
- _wrapped_with_cache_async: Asynchronous cache wrapper. Receives the same inputs as the wrapped function and bypasses the cache when stream is True.

Summary
Provides caching for Litellm requests while preserving streaming behavior and using a PipelineCache keyed by get_cache_key.

## Functions

- [`with_cache`](../api/functions/graphrag-language-model-providers-litellm-request-wrappers-with-cache-with-cache)
- [`_wrapped_with_cache`](../api/functions/graphrag-language-model-providers-litellm-request-wrappers-with-cache-wrapped-with-cache)
- [`_wrapped_with_cache_async`](../api/functions/graphrag-language-model-providers-litellm-request-wrappers-with-cache-wrapped-with-cache-async)

