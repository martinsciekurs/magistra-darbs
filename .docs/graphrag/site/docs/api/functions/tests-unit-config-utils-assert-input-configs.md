---
sidebar_position: 486
---

# assert_input_configs

**File:** `tests/unit/config/utils.py` (lines 168-183)

## Signature

```python
def assert_input_configs(actual: InputConfig, expected: InputConfig) -> None
```

## Description

Assert that two InputConfig objects have identical field values.

Args:
    actual: The actual InputConfig to validate.
    expected: The expected InputConfig to compare against.

Returns:
    None

Raises:
    AssertionError: If any of the fields differ: storage.type, file_type, storage.base_dir, storage.connection_string, storage.storage_account_blob_url, storage.container_name, encoding, file_pattern, file_filter, text_column, title_column, metadata.

## Called By

This function is called by:

- `tests/unit/config/utils.py::assert_graphrag_configs`

