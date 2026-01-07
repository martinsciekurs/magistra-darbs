---
sidebar_position: 18
---

# CosmosDBVectorStore

**File:** `graphrag/vector_stores/cosmosdb.py`

## Overview

CosmosDBVectorStore is a Cosmos DB-backed vector store implementation for GraphRAG. It manages storage, retrieval, and indexing of document vectors and metadata in Azure Cosmos DB and supports text-based and vector-based similarity search.

Args:
  vector_store_schema_config (VectorStoreSchemaConfig): The schema configuration for the vector store, including field mappings for id, vector, text, and attributes, as well as database/container naming.
  **kwargs: Additional keyword arguments forwarded to the base class initializer.

Returns:
  None

Raises:
  CosmosHttpResponseError: If an HTTP error occurs while interacting with Cosmos DB (e.g., during database/container operations or listing resources).

## Methods

### `_database_exists`

```python
def _database_exists(self) -> bool
```

### `similarity_search_by_text`

```python
def similarity_search_by_text(
        self, text: str, text_embedder: TextEmbedder, k: int = 10, **kwargs: Any
    ) -> list[VectorStoreSearchResult]
```

### `_delete_database`

```python
def _delete_database(self) -> None
```

### `filter_by_id`

```python
def filter_by_id(self, include_ids: list[str] | list[int]) -> Any
```

### `__init__`

```python
def __init__(
        self, vector_store_schema_config: VectorStoreSchemaConfig, **kwargs: Any
    ) -> None
```

### `cosine_similarity`

```python
def cosine_similarity(a, b)
```

### `_create_database`

```python
def _create_database(self) -> None
```

### `_create_container`

```python
def _create_container(self) -> None
```

### `connect`

```python
def connect(self, **kwargs: Any) -> Any
```

### `load_documents`

```python
def load_documents(
        self, documents: list[VectorStoreDocument], overwrite: bool = True
    ) -> None
```

### `_container_exists`

```python
def _container_exists(self) -> bool
```

### `search_by_id`

```python
def search_by_id(self, id: str) -> VectorStoreDocument
```

### `_delete_container`

```python
def _delete_container(self) -> None
```

### `clear`

```python
def clear(self) -> None
```

### `similarity_search_by_vector`

```python
def similarity_search_by_vector(
        self, query_embedding: list[float], k: int = 10, **kwargs: Any
    ) -> list[VectorStoreSearchResult]
```

