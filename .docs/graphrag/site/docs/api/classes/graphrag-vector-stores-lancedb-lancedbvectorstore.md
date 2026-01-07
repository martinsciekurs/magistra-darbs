---
sidebar_position: 12
---

# LanceDBVectorStore

**File:** `graphrag/vector_stores/lancedb.py`

## Overview

LanceDB-backed vector store that uses LanceDB for storing and querying document embeddings.

This class extends BaseVectorStore to provide similarity search by text and by vector, loading documents into LanceDB, filtering by IDs, and connecting to a LanceDB database. Key attributes include vector_store_schema_config, index_name (optional), and document_collection (the LanceDB table handle).

Args:
  vector_store_schema_config: VectorStoreSchemaConfig - The schema configuration for the vector store.
  **kwargs: Any - Additional keyword arguments forwarded to the base class initializer.

Returns:
  None

Raises:
  Exceptions raised by the base class __init__ are propagated.

## Methods

### `similarity_search_by_text`

```python
def similarity_search_by_text(
        self, text: str, text_embedder: TextEmbedder, k: int = 10, **kwargs: Any
    ) -> list[VectorStoreSearchResult]
```

### `search_by_id`

```python
def search_by_id(self, id: str) -> VectorStoreDocument
```

### `load_documents`

```python
def load_documents(
        self, documents: list[VectorStoreDocument], overwrite: bool = True
    ) -> None
```

### `similarity_search_by_vector`

```python
def similarity_search_by_vector(
        self, query_embedding: list[float] | np.ndarray, k: int = 10, **kwargs: Any
    ) -> list[VectorStoreSearchResult]
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

### `connect`

```python
def connect(self, **kwargs: Any) -> Any
```

