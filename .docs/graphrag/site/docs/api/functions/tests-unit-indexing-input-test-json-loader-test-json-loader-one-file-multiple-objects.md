---
sidebar_position: 506
---

# test_json_loader_one_file_multiple_objects

**File:** `tests/unit/indexing/input/test_json_loader.py` (lines 25-37)

## Signature

```python
def test_json_loader_one_file_multiple_objects()
```

## Description

Test loading a JSON file containing multiple objects and verify the loaded DataFrame.

Args:
    None: This test function does not accept any parameters.

Returns:
    None: The function does not return a value.

Raises:
    AssertionError: If the loaded data does not match the expected shape or values.

## Dependencies

This function calls:

- `graphrag/config/models/input_config.py::InputConfig`
- `graphrag/config/models/storage_config.py::StorageConfig`
- `graphrag/index/input/factory.py::create_input`
- `graphrag/utils/api.py::create_storage_from_config`

