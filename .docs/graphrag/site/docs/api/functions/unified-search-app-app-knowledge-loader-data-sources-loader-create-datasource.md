---
sidebar_position: 611
---

# create_datasource

**File:** `unified-search-app/app/knowledge_loader/data_sources/loader.py` (lines 43-49)

## Signature

```python
def create_datasource(dataset_folder: str) -> Datasource
```

## Description

Return a datasource that reads from a local or blob storage parquet file.

Args:
    dataset_folder: Path to the dataset folder to load data from.

Returns:
    Datasource: A datasource instance. If blob_account_name is set, a BlobDatasource is returned;
        otherwise, a LocalDatasource configured with the base path derived from dataset_folder and local_data_root.

Raises:
    Exceptions that may be raised by the underlying BlobDatasource or LocalDatasource constructors.

## Dependencies

This function calls:

- `unified-search-app/app/knowledge_loader/data_sources/loader.py::_get_base_path`

