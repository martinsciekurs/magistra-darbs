---
sidebar_position: 401
---

# create_cache_from_config

**File:** `graphrag/utils/api.py` (lines 273-280)

## Signature

```python
def create_cache_from_config(cache: CacheConfig, root_dir: str) -> PipelineCache
```

## Description

Create a cache object from the given CacheConfig by delegating to CacheFactory.

Args:
  cache: CacheConfig The cache configuration to create the cache object from. The configuration is dumped to a dict via model_dump(); the dictionary must include a "type" key used to determine the concrete cache implementation.
  root_dir: str The root directory to merge into the cache creation kwargs.

Returns:
  PipelineCache: The created cache object.

Raises:
  Exception: May raise any exception raised by the underlying CacheFactory during cache creation.

Notes:
  This function uses cache.model_dump() to obtain the configuration, reads the "type" field for the cache_type, and merges root_dir into the kwargs before invoking CacheFactory.

## Dependencies

This function calls:

- `graphrag.cache.factory::CacheFactory`

## Called By

This function is called by:

- `graphrag/index/run/run_pipeline.py::run_pipeline`

