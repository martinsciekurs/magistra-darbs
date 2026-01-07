---
sidebar_position: 483
---

# assert_output_configs

**File:** `tests/unit/config/utils.py` (lines 139-145)

## Signature

```python
def assert_output_configs(actual: StorageConfig, expected: StorageConfig) -> None
```

## Description

Assert that two StorageConfig objects have identical field values.

Args:
    actual: The actual StorageConfig to validate.
    expected: The expected StorageConfig to compare against.

Returns:
    None

Raises:
    AssertionError: If any of the fields differ: type, base_dir, connection_string, container_name, storage_account_blob_url, cosmosdb_account_url.

## Called By

This function is called by:

- `tests/unit/config/utils.py::assert_graphrag_configs`

