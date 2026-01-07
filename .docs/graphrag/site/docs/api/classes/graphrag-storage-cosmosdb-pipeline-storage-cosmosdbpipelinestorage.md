---
sidebar_position: 3
---

# CosmosDBPipelineStorage

**File:** `graphrag/storage/cosmosdb_pipeline_storage.py`

## Overview

CosmosDBPipelineStorage is a Cosmos DB-backed storage backend that stores and retrieves data in a Cosmos DB container. It implements the storage interface used by Graphrag to manage databases, containers, and items, including creation/deletion of databases and containers, insertion of file contents, retrieval, and query-based operations. It maintains an internal reference to the active container via _container_client, and this reference is cleared when the database is deleted or when no container exists, reflecting the lifecycle of the underlying Cosmos DB resources.

Summary:
- Provides a persistent storage layer backed by Azure Cosmos DB for file-based data.
- Manages the lifecycle of a database and container and exposes item-level operations consistent with the PipelineStorage API.
- Keeps an internal _container_client to interact with the current container; this is cleared when the database/container is removed.

Args:
- cosmosdb_account_url: The URL of the Cosmos DB account. Used to initialize CosmosClient when a connection string is not provided.
- connection_string: The Cosmos DB connection string. Used to initialize CosmosClient when provided.
- base_dir: The database name to create/use.
- container_name: The container name to create/use.
- encoding: Encoding to use for serialization/deserialization (e.g., utf-8).

Returns:
- None: This constructor does not return a value.

Raises:
- CosmosHttpResponseError: If the Cosmos DB service returns an HTTP error during initialization or resource creation.

## Methods

### `_delete_database`

```python
def _delete_database(self) -> None
```

### `__init__`

```python
def __init__(self, **kwargs: Any) -> None
```

### `clear`

```python
def clear(self) -> None
```

### `keys`

```python
def keys(self) -> list[str]
```

### `_delete_container`

```python
def _delete_container(self) -> None
```

### `child`

```python
def child(self, name: str | None) -> PipelineStorage
```

### `_create_container`

```python
def _create_container(self) -> None
```

### `set`

```python
def set(self, key: str, value: Any, encoding: str | None = None) -> None
```

### `_create_database`

```python
def _create_database(self) -> None
```

### `delete`

```python
def delete(self, key: str) -> None
```

### `get`

```python
def get(
        self, key: str, as_bytes: bool | None = None, encoding: str | None = None
    ) -> Any
```

### `item_filter`

```python
def item_filter(item: dict[str, Any]) -> bool
```

### `_get_prefix`

```python
def _get_prefix(self, key: str) -> str
```

### `has`

```python
def has(self, key: str) -> bool
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

### `get_creation_date`

```python
def get_creation_date(self, key: str) -> str
```

