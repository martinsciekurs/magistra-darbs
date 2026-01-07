---
sidebar_position: 501
---

# test_csv_loader_one_file

**File:** `tests/unit/indexing/input/test_csv_loader.py` (lines 11-22)

## Signature

```python
def test_csv_loader_one_file()
```

## Description

Test loading a single CSV file using the input loader and verify the resulting DataFrame.

This test constructs an InputConfig configured for CSV files in a single directory, creates storage via create_storage_from_config, loads documents with create_input, and asserts:
- the resulting DataFrame has shape (2, 4)
- the first row in the title column is "input.csv"

Returns:
  None. This test does not return a value.

Raises:
  ValueError: If the storage type is not registered in create_storage_from_config.

## Dependencies

This function calls:

- `graphrag/config/models/input_config.py::InputConfig`
- `graphrag/config/models/storage_config.py::StorageConfig`
- `graphrag/index/input/factory.py::create_input`
- `graphrag/utils/api.py::create_storage_from_config`

