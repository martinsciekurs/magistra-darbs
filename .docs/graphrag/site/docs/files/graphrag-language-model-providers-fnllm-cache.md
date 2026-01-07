---
sidebar_position: 145
---

# graphrag/language_model/providers/fnllm/cache.py

## Overview

FNLLM cache provider that adapts a PipelineCache to the FNLLM cache interface by delegating all operations to the underlying cache.

Purpose
- Expose a FNLLM-compatible caching interface backed by a Graphrag PipelineCache, enabling reuse of the existing cache backend.

Key exports
- FNLLMCacheProvider: Adapts a PipelineCache to the FNLLM cache interface by delegating all operations to the underlying cache instance.

Classes
- FNLLMCacheProvider
  Adapts a PipelineCache to the FNLLM cache interface by delegating all cache operations to the underlying cache instance.
  Args:
    cache: The underlying PipelineCache instance used by this provider.
  Returns:
    None
  Raises:
    Exceptions may propagate from the underlying cache.

Brief summary
- The module defines FNLLMCacheProvider which wraps a PipelineCache and exposes the cache methods clear, get, has, remove, set, and child, delegating to the underlying cache and propagating exceptions as needed.

## Classes

- [`FNLLMCacheProvider`](../api/classes/graphrag-language-model-providers-fnllm-cache-fnllmcacheprovider)

## Functions

- [`clear`](../api/functions/graphrag-language-model-providers-fnllm-cache-clear)
- [`get`](../api/functions/graphrag-language-model-providers-fnllm-cache-get)
- [`has`](../api/functions/graphrag-language-model-providers-fnllm-cache-has)
- [`remove`](../api/functions/graphrag-language-model-providers-fnllm-cache-remove)
- [`__init__`](../api/functions/graphrag-language-model-providers-fnllm-cache-init)
- [`set`](../api/functions/graphrag-language-model-providers-fnllm-cache-set)
- [`child`](../api/functions/graphrag-language-model-providers-fnllm-cache-child)

