---
sidebar_position: 612
---

# load_dataset_listing

**File:** `unified-search-app/app/knowledge_loader/data_sources/loader.py` (lines 52-69)

## Signature

```python
def load_dataset_listing() -> list[DatasetConfig]
```

## Description

Load dataset listing file from blob storage or local data.

This function takes no parameters and returns a list of DatasetConfig instances parsed from the listing file. When blob storage is configured (blob_account_name is set), the function loads the listing from blob storage and, on error, prints the issue and returns an empty list (no exception is raised).

When blob storage is not configured, the function loads the listing from the local filesystem using the path derived from local_data_root and LISTING_FILE, parses the JSON content, and converts each listing item into a DatasetConfig instance. Errors during local loading may propagate to the caller.

Returns:
    list[DatasetConfig]: A list of DatasetConfig instances created from the listing entries. May be empty if loading from blob storage fails or no data is found.

Raises:
    FileNotFoundError: If the local listing file cannot be found when blob storage is not used.
    json.JSONDecodeError: If the listing JSON content is invalid when loaded from local path.
    TypeError: If a listing item does not provide the required fields for DatasetConfig.

## Dependencies

This function calls:

- `unified-search-app/app/knowledge_loader/data_sources/loader.py::_get_base_path`

