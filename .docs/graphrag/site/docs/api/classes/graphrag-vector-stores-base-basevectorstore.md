---
sidebar_position: 20
---

# BaseVectorStore

**File:** `graphrag/vector_stores/base.py`

## Overview

Abstract base class for vector stores used by GraphRAG.

This class defines the core interface and common lifecycle for vector-based storage and retrieval of documents. Subclasses must implement the storage backend and search logic for both vector and text queries, while this class provides a consistent initialization surface and shared attributes.

Args:
    vector_store_schema_config (VectorStoreSchemaConfig): The schema configuration for this vector store, including vector dimensions and field mappings.
    db_connection (Any, optional): Optional database or resource handle used to connect to the underlying storage. Defaults to None.
    document_collection (Any, optional): Optional existing collection of documents within the store. Defaults to None.
    query_filter (Any, optional): Optional default filter applied when retrieving documents. Defaults to None.
    **kwargs (Any): Additional keyword arguments for subclass-specific behavior.

Attributes:
    vector_store_schema_config: The configuration used to configure this store's schema and vector properties.
    db_connection: Optional store connection/resource.
    document_collection: Optional stored document collection.
    query_filter: Optional default query filter.

Abstract methods (must be implemented by subclasses):
    connect(self, **kwargs): Establish a connection to the vector store.
    load_documents(self, documents, overwrite=True): Load documents into the store.
    similarity_search_by_vector(self, query_embedding, k=10, **kwargs): ANN search by vector.
    similarity_search_by_text(self, text, text_embedder, k=10, **kwargs): ANN search by text.
    search_by_id(self, id): Retrieve a document by its identifier.
    filter_by_id(self, include_ids): Build a filter to limit results by IDs.

Notes:
    This base class is not intended to be instantiated directly. Concrete implementations should provide the specifics of the storage backend and search mechanics.

## Methods

### `similarity_search_by_vector`

```python
def similarity_search_by_vector(
        self, query_embedding: list[float], k: int = 10, **kwargs: Any
    ) -> list[VectorStoreSearchResult]
```

### `connect`

```python
def connect(self, **kwargs: Any) -> None
```

### `filter_by_id`

```python
def filter_by_id(self, include_ids: list[str] | list[int]) -> Any
```

### `load_documents`

```python
def load_documents(
        self, documents: list[VectorStoreDocument], overwrite: bool = True
    ) -> None
```

### `__init__`

```python
def __init__(
        self,
        vector_store_schema_config: VectorStoreSchemaConfig,
        db_connection: Any | None = None,
        document_collection: Any | None = None,
        query_filter: Any | None = None,
        **kwargs: Any,
    )
```

### `search_by_id`

```python
def search_by_id(self, id: str) -> VectorStoreDocument
```

### `similarity_search_by_text`

```python
def similarity_search_by_text(
        self, text: str, text_embedder: TextEmbedder, k: int = 10, **kwargs: Any
    ) -> list[VectorStoreSearchResult]
```

