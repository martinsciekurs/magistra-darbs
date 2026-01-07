---
sidebar_position: 609
---

# load_blob_file

**File:** `unified-search-app/app/knowledge_loader/data_sources/blob_source.py` (lines 60-78)

## Signature

```python
def load_blob_file(
    dataset: str | None,
    file: str | None,
    account_name: str | None = blob_account_name,
    container_name: str | None = blob_container_name,
) -> BytesIO
```

## Description

Load blob file from container.

Args:
    dataset: The dataset prefix to use when constructing the blob path. If None, only the file name is used.
    file: The blob file name to load. If dataset is provided, the blob path will be "&lt;dataset&gt;/&lt;file&gt;".
    account_name: The Azure storage account name. Defaults to blob_account_name.
    container_name: The Azure Blob container name. Defaults to blob_container_name.

Returns:
    BytesIO: An in-memory binary stream containing the blob data read into the stream. If account_name or container_name is None, an empty BytesIO is returned.

Raises:
    Exception: May raise exceptions from Azure Blob Storage operations (authentication, network, or other errors) during container retrieval or blob download.

## Dependencies

This function calls:

- `unified-search-app/app/knowledge_loader/data_sources/blob_source.py::_get_container`

## Called By

This function is called by:

- `unified-search-app/app/knowledge_loader/data_sources/blob_source.py::BlobDatasource.read`
- `unified-search-app/app/knowledge_loader/data_sources/blob_source.py::BlobDatasource.read_settings`

