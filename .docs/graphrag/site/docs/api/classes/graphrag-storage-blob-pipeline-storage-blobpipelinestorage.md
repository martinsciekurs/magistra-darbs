---
sidebar_position: 19
---

# BlobPipelineStorage

**File:** `graphrag/storage/blob_pipeline_storage.py`

## Overview

BlobPipelineStorage is an Azure Blob Storage backed implementation of the PipelineStorage interface for caching pipeline data.

Summary:
This class provides a blob-based storage backend for caching results and data used by the GraphRag pipeline. It stores dataframe exports as JSON or Parquet, supports retrieving values, finding blobs by pattern, and basic cache management. Initialization selects between using a connection string or a storage account URL with DefaultAzureCredential to create the BlobServiceClient, and requires a container name.

Attributes:
  _blob_service_client (BlobServiceClient): Client used to interact with Azure Blob Storage.
  _container_name (str): Name of the container in which blobs are stored.
  _path_prefix (str): Path prefix used to scope blob names within the container.

Args:
  connection_string: Optional Azure Blob Storage connection string. If provided, the BlobServiceClient is created from this string.
  storage_account_blob_url: Optional URL to the storage account. If provided (and connection_string is not), the BlobServiceClient is created using DefaultAzureCredential.
  container_name: Name of the blob container to use. The container will be created if it does not exist.

Raises:
  ValueError: If neither connection_string nor storage_account_blob_url is provided.

## Methods

### `_abfs_url`

```python
def _abfs_url(self, key: str) -> str
```

### `keys`

```python
def keys(self) -> list[str]
```

### `_set_df_json`

```python
def _set_df_json(self, key: str, dataframe: Any) -> None
```

### `_set_df_parquet`

```python
def _set_df_parquet(self, key: str, dataframe: Any) -> None
```

### `find`

```python
def find(
        self,
        file_pattern: re.Pattern[str],
        base_dir: str | None = None,
        file_filter: dict[str, Any] | None = None,
        max_count=-1,
    ) -> Iterator[tuple[str, dict[str, Any]]]
```

### `clear`

```python
def clear(self) -> None
```

### `get`

```python
def get(
        self, key: str, as_bytes: bool | None = False, encoding: str | None = None
    ) -> Any
```

### `_create_container`

```python
def _create_container(self) -> None
```

### `delete`

```python
def delete(self, key: str) -> None
```

### `_container_exists`

```python
def _container_exists(self) -> bool
```

### `set`

```python
def set(self, key: str, value: Any, encoding: str | None = None) -> None
```

### `_keyname`

```python
def _keyname(self, key: str) -> str
```

### `__init__`

```python
def __init__(self, **kwargs: Any) -> None
```

### `has`

```python
def has(self, key: str) -> bool
```

### `item_filter`

```python
def item_filter(item: dict[str, Any]) -> bool
```

### `_delete_container`

```python
def _delete_container(self) -> None
```

### `child`

```python
def child(self, name: str | None) -> "PipelineStorage"
```

### `_blobname`

```python
def _blobname(blob_name: str) -> str
```

### `get_creation_date`

```python
def get_creation_date(self, key: str) -> str
```

