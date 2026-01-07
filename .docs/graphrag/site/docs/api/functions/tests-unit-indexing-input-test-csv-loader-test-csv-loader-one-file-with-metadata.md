---
sidebar_position: 503
---

# test_csv_loader_one_file_with_metadata

**File:** `tests/unit/indexing/input/test_csv_loader.py` (lines 40-53)

## Signature

```python
def test_csv_loader_one_file_with_metadata()
```

## Description

Async test that loads a single CSV file with metadata and validates the loaded DataFrame and metadata content.

Args:
    None: This test does not take any parameters.

Returns:
    None: The test does not return a value; it performs assertions to verify behavior.

Raises:
    AssertionError: If the loaded DataFrame shape or metadata content does not match the expected values.

## Dependencies

This function calls:

- `graphrag/config/models/input_config.py::InputConfig`
- `graphrag/config/models/storage_config.py::StorageConfig`
- `graphrag/index/input/factory.py::create_input`
- `graphrag/utils/api.py::create_storage_from_config`

