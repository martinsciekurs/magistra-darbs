---
sidebar_position: 504
---

# test_csv_loader_multiple_files

**File:** `tests/unit/indexing/input/test_csv_loader.py` (lines 56-66)

## Signature

```python
def test_csv_loader_multiple_files()
```

## Description

Test loading multiple CSV files and verify the resulting DataFrame shape.

Configures an InputConfig to load CSV files from tests/unit/indexing/input/data/multiple-csvs, using file_type csv and a pattern that matches CSV files, creates storage from the config, loads the documents, and asserts the DataFrame shape is (4, 4).

Returns:
  None

## Dependencies

This function calls:

- `graphrag/config/models/input_config.py::InputConfig`
- `graphrag/config/models/storage_config.py::StorageConfig`
- `graphrag/index/input/factory.py::create_input`
- `graphrag/utils/api.py::create_storage_from_config`

