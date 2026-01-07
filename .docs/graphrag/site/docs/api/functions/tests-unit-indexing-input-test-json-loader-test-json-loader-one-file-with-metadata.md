---
sidebar_position: 508
---

# test_json_loader_one_file_with_metadata

**File:** `tests/unit/indexing/input/test_json_loader.py` (lines 55-68)

## Signature

```python
def test_json_loader_one_file_with_metadata()
```

## Description

Test loading a single JSON file with metadata and validating that the metadata is included in the resulting DataFrame.

Args:
    None

Returns:
    None

Raises:
    AssertionError: If the loaded data does not match the expected shape or metadata values.

## Dependencies

This function calls:

- `graphrag/config/models/input_config.py::InputConfig`
- `graphrag/config/models/storage_config.py::StorageConfig`
- `graphrag/index/input/factory.py::create_input`
- `graphrag/utils/api.py::create_storage_from_config`

