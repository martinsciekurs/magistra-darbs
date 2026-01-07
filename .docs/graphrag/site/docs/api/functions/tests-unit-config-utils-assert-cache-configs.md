---
sidebar_position: 477
---

# assert_cache_configs

**File:** `tests/unit/config/utils.py` (lines 159-165)

## Signature

```python
def assert_cache_configs(actual: CacheConfig, expected: CacheConfig) -> None
```

## Description

Assert that two CacheConfig objects have identical field values.

Args:
    actual: The actual CacheConfig to validate.
    expected: The expected CacheConfig to compare against.

Returns:
    None

Raises:
    AssertionError: If any of the fields differ: type, base_dir, connection_string, container_name, storage_account_blob_url, cosmosdb_account_url.

## Called By

This function is called by:

- `tests/unit/config/utils.py::assert_graphrag_configs`

