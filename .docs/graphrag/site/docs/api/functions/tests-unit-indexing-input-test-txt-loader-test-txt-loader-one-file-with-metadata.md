---
sidebar_position: 511
---

# test_txt_loader_one_file_with_metadata

**File:** `tests/unit/indexing/input/test_txt_loader.py` (lines 25-38)

## Signature

```python
def test_txt_loader_one_file_with_metadata()
```

## Description

Test loading a single TXT file with metadata and verify the metadata content.

Args:
    None: This test does not accept any parameters.

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

