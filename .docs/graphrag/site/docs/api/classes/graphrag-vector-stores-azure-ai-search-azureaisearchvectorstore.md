---
sidebar_position: 7
---

# AzureAISearchVectorStore

**File:** `graphrag/vector_stores/azure_ai_search.py`

## Overview

Azure AI Search vector store integrating Azure Cognitive Search to provide vector-based retrieval.

This class provides vector similarity search, text-based search, and document load/retrieval backed by Azure AI Search. It delegates initialization to the base vector store class and is configured via VectorStoreSchemaConfig.

Args:
  vector_store_schema_config: VectorStoreSchemaConfig - The schema configuration for the vector store.
  **kwargs: Any - Additional keyword arguments forwarded to the base class initializer.

Returns:
  None

Raises:
  Exceptions raised by the base class __init__ are propagated.

## Methods

### `similarity_search_by_vector`

```python
def similarity_search_by_vector(
        self, query_embedding: list[float], k: int = 10, **kwargs: Any
    ) -> list[VectorStoreSearchResult]
```

### `connect`

```python
def connect(self, **kwargs: Any) -> Any
```

### `similarity_search_by_text`

```python
def similarity_search_by_text(
        self, text: str, text_embedder: TextEmbedder, k: int = 10, **kwargs: Any
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

