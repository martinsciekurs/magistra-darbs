---
sidebar_position: 44
---

# BlobWorkflowLogger

**File:** `graphrag/logger/blob_workflow_logger.py`

## Overview

Blob-based workflow logger that persists log records to Azure Blob storage as JSON lines.

Summary:
The BlobWorkflowLogger is a logging handler that formats records into JSON payloads and appends them as lines to a blob in an Azure Storage container. It supports categorizing log entries by type (log, warning, error) and reinitializes its internal client when the accumulation reaches a configured maximum.

Args:
    connection_string: Connection string for the blob storage, or None
    container_name: Name of the blob container
    blob_name: Name of the blob to create; if empty, a timestamped default will be used
    base_dir: Base directory to prepend to the blob name, or None
    storage_account_blob_url: URL of the storage account blob service, or None
    level: Logging level threshold (default NOTSET)

Returns:
    None

Raises:
    OSError: If an I/O error occurs during blob operations or persistence

## Methods

### `_write_log`

```python
def _write_log(self, log: dict[str, Any])
```

### `_get_log_type`

```python
def _get_log_type(self, level: int) -> str
```

### `__init__`

```python
def __init__(
        self,
        connection_string: str | None,
        container_name: str | None,
        blob_name: str = "",
        base_dir: str | None = None,
        storage_account_blob_url: str | None = None,
        level: int = logging.NOTSET,
    )
```

### `emit`

```python
def emit(self, record) -> None
```

