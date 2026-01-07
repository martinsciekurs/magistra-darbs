---
sidebar_position: 54
---

# MockBaseVectorStore

**File:** `tests/unit/query/context_builder/test_entity_extraction.py`

## Overview

MockBaseVectorStore is a test helper that provides a lightweight, in-memory vector store for unit tests. It is designed to mirror essential aspects of a real vector store without performing real embeddings or persisting data, offering deterministic, mock search and retrieval behavior.

Args:
    documents (list[VectorStoreDocument]): Documents to initialize the mock vector store with for testing.

Attributes:
    documents (list[VectorStoreDocument]): Documents stored in the mock vector store used for retrieval and search in tests.

Notes:
    - Deterministic results: search and retrieval behavior is fixed and repeatable across runs.
    - No persistence: data exists only for the lifetime of the test process.
    - This class provides a test-facing implementation that mirrors the BaseVectorStore interface as needed by tests, without embedding calculations.

Methods:
    connect(**kwargs: Any) -&gt; None
        No-op connection helper used in tests. Accepts arbitrary keyword arguments and performs no action.

    __init__(self, documents: list[VectorStoreDocument]) -&gt; None
        Initialize the mock vector store with the provided documents for testing.

    filter_by_id(include_ids: list[str] | list[int]) -&gt; list[VectorStoreDocument]
        Return the documents whose id is in include_ids.

    similarity_search_by_text(
        self, text: str, text_embedder: TextEmbedder, k: int = 10, **kwargs: Any
    ) -&gt; list[VectorStoreSearchResult]
        Perform a deterministic, length-based search ignoring embeddings. Returns up to k results based on stored documents with a fixed score.

    load_documents(
        self, documents: list[VectorStoreDocument], overwrite: bool = True
    ) -&gt; None
        Load documents into the vector store; if overwrite is True, replace existing data; otherwise, append.

    similarity_search_by_vector(
        self, query_embedding: list[float], k: int = 10, **kwargs: Any
    ) -&gt; list[VectorStoreSearchResult]
        Return the top-k documents using a deterministic mock search that ignores the query embedding; returns the first k documents with a fixed score of 1.

    search_by_id(self, id: str) -&gt; VectorStoreDocument
        Return the first stored document with its id set to the provided id.

## Methods

### `connect`

```python
def connect(self, **kwargs: Any) -> None
```

### `__init__`

```python
def __init__(self, documents: list[VectorStoreDocument]) -> None
```

### `filter_by_id`

```python
def filter_by_id(self, include_ids: list[str] | list[int]) -> Any
```

### `similarity_search_by_text`

```python
def similarity_search_by_text(
        self, text: str, text_embedder: TextEmbedder, k: int = 10, **kwargs: Any
    ) -> list[VectorStoreSearchResult]
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
        self, query_embedding: list[float], k: int = 10, **kwargs: Any
    ) -> list[VectorStoreSearchResult]
```

### `search_by_id`

```python
def search_by_id(self, id: str) -> VectorStoreDocument
```

