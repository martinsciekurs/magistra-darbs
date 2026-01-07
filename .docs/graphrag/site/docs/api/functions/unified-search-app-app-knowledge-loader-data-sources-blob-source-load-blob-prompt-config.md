---
sidebar_position: 608
---

# load_blob_prompt_config

**File:** `unified-search-app/app/knowledge_loader/data_sources/blob_source.py` (lines 38-57)

## Signature

```python
def load_blob_prompt_config(
    dataset: str,
    account_name: str | None = blob_account_name,
    container_name: str | None = blob_container_name,
) -> dict[str, str]
```

## Description

Load blob prompt configuration for a dataset from Azure Blob Storage.

Args:
    dataset: The dataset name to load prompts for.
    account_name: The Azure storage account name. If None, no prompts are loaded.
    container_name: The blob container name. If None, no prompts are loaded.

Returns:
    dict[str, str]: A mapping from prompt map name to its content loaded from the blob storage.

Raises:
    Exception: Propagated exceptions from underlying Azure Blob Storage operations.

## Dependencies

This function calls:

- `unified-search-app/app/knowledge_loader/data_sources/blob_source.py::_get_container`

