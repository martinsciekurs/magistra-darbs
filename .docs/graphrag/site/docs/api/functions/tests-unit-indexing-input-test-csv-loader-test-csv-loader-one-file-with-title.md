---
sidebar_position: 502
---

# test_csv_loader_one_file_with_title

**File:** `tests/unit/indexing/input/test_csv_loader.py` (lines 25-37)

## Signature

```python
def test_csv_loader_one_file_with_title()
```

## Description

Asynchronous test that loads a single CSV file with a title column using the input loader.

Configures InputConfig to read CSV files from tests/unit/indexing/input/data/one-csv with a file_pattern that matches CSVs and sets title_column to "title". It loads documents via create_input and asserts that the resulting DataFrame has shape (2, 4) and that the first row in the title column is "Hello".

Returns:
    None

## Dependencies

This function calls:

- `graphrag/config/models/input_config.py::InputConfig`
- `graphrag/config/models/storage_config.py::StorageConfig`
- `graphrag/index/input/factory.py::create_input`
- `graphrag/utils/api.py::create_storage_from_config`

