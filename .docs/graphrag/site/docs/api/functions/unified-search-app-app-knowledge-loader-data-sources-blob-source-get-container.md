---
sidebar_position: 607
---

# _get_container

**File:** `unified-search-app/app/knowledge_loader/data_sources/blob_source.py` (lines 29-35)

## Signature

```python
def _get_container(account_name: str, container_name: str) -> ContainerClient
```

## Description

Return a ContainerClient for the specified Azure Blob Storage container.

Args:
    account_name: The Azure storage account name.
    container_name: The name of the blob container.

Returns:
    ContainerClient: The container client for the specified container.

Raises:
    Exception: If authentication, network, or other Azure Blob Storage errors occur.

## Called By

This function is called by:

- `unified-search-app/app/knowledge_loader/data_sources/blob_source.py::load_blob_prompt_config`
- `unified-search-app/app/knowledge_loader/data_sources/blob_source.py::load_blob_file`

