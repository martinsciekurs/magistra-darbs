---
sidebar_position: 29
---

# MultiVectorStore

**File:** `graphrag/utils/api.py`

## Overview

Unified interface that combines multiple vector stores into a single multi-store for cross-store search and retrieval.

## Methods

### `similarity_search_by_text`

```python
def similarity_search_by_text(
        self, text: str, text_embedder: TextEmbedder, k: int = 10, **kwargs: Any
    ) -> list[VectorStoreSearchResult]
```

### `similarity_search_by_vector`

```python
def similarity_search_by_vector(
        self, query_embedding: list[float], k: int = 10, **kwargs: Any
    ) -> list[VectorStoreSearchResult]
```

### `search_by_id`

```python
def search_by_id(self, id: str) -> VectorStoreDocument
```

### `__init__`

```python
def __init__(
        self,
        embedding_stores: list[BaseVectorStore],
        index_names: list[str],
    )
```

### `load_documents`

```python
def load_documents(
        self, documents: list[VectorStoreDocument], overwrite: bool = True
    ) -> None
```

### `filter_by_id`

```python
def filter_by_id(self, include_ids: list[str] | list[int]) -> Any
```

### `connect`

```python
def connect(self, **kwargs: Any) -> Any
```

