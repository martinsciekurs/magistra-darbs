---
sidebar_position: 505
---

# test_json_loader_one_file_one_object

**File:** `tests/unit/indexing/input/test_json_loader.py` (lines 11-22)

## Signature

```python
def test_json_loader_one_file_one_object()
```

## Description

Test loading a single JSON file containing one object and validating the loaded data.

This test builds an InputConfig using json input, loads documents via create_input, and asserts that the resulting DataFrame has shape (1, 4) and that the title field equals "input.json".

Returns:
    None

Raises:
    AssertionError: If the loaded data does not match the expected shape or values.

## Dependencies

This function calls:

- `graphrag/config/models/input_config.py::InputConfig`
- `graphrag/config/models/storage_config.py::StorageConfig`
- `graphrag/index/input/factory.py::create_input`
- `graphrag/utils/api.py::create_storage_from_config`

