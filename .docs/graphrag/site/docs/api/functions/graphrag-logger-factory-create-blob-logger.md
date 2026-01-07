---
sidebar_position: 305
---

# create_blob_logger

**File:** `graphrag/logger/factory.py` (lines 99-108)

## Signature

```python
def create_blob_logger(**kwargs) -> logging.Handler
```

## Description

Create a blob storage-based logger.

Args:
    kwargs: The keyword arguments for configuring the blob logger.
        connection_string: The Azure Blob Storage connection string.
        container_name: The name of the blob container.
        base_dir: The base directory inside the container where logs should be stored.
        storage_account_blob_url: The URL of the blob storage account used by the logger.

Returns:
    logging.Handler: A configured BlobWorkflowLogger instance.

Raises:
    KeyError: If required keys (connection_string, container_name, base_dir, storage_account_blob_url) are missing from kwargs.

## Dependencies

This function calls:

- `graphrag/logger/blob_workflow_logger.py::BlobWorkflowLogger`

