---
sidebar_position: 507
---

# test_json_loader_one_file_with_title

**File:** `tests/unit/indexing/input/test_json_loader.py` (lines 40-52)

## Signature

```python
def test_json_loader_one_file_with_title()
```

## Description

Test loading a single JSON file with an explicit title column ('title') and verify that the resulting DataFrame has shape (1, 4) and the title value equals 'Hello'.

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

