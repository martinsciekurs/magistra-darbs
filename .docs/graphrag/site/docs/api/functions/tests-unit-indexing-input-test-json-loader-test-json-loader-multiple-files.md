---
sidebar_position: 509
---

# test_json_loader_multiple_files

**File:** `tests/unit/indexing/input/test_json_loader.py` (lines 71-81)

## Signature

```python
def test_json_loader_multiple_files()
```

## Description

Test loading multiple JSON files from tests/unit/indexing/input/data/multiple-jsons and verifying the loaded DataFrame shape (4, 4).

The test builds an InputConfig for JSON input using a file pattern that matches JSON files, creates a storage object from the config, loads documents via create_input, and asserts that the resulting DataFrame has shape (4, 4). This is a test function and does not return any data.

Args:
    None: This test function does not accept any parameters.

Returns:
    None: The test does not return a value.

Raises:
    AssertionError: If the loaded data does not have the expected shape (4, 4).
    ValueError: If storage creation from the config fails.

## Dependencies

This function calls:

- `graphrag/config/models/input_config.py::InputConfig`
- `graphrag/config/models/storage_config.py::StorageConfig`
- `graphrag/index/input/factory.py::create_input`
- `graphrag/utils/api.py::create_storage_from_config`

