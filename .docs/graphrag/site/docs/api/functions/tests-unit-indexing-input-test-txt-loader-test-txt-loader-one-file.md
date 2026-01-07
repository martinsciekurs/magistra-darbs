---
sidebar_position: 510
---

# test_txt_loader_one_file

**File:** `tests/unit/indexing/input/test_txt_loader.py` (lines 11-22)

## Signature

```python
def test_txt_loader_one_file()
```

## Description

Test loading a single TXT file using the input loader and verify the resulting DataFrame shape and title.

Args:
    None: This test function does not accept any parameters.

Returns:
    None: This test does not return a value.

Raises:
    None: This test does not raise exceptions under normal operation.

## Dependencies

This function calls:

- `graphrag/config/models/input_config.py::InputConfig`
- `graphrag/config/models/storage_config.py::StorageConfig`
- `graphrag/index/input/factory.py::create_input`
- `graphrag/utils/api.py::create_storage_from_config`

