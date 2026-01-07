---
sidebar_position: 88
---

# TestLanceDBVectorStore

**File:** `tests/integration/vector_stores/test_lancedb.py`

## Overview

Integration tests for LanceDBVectorStore integration.

Purpose:
Test the LanceDB-backed vector store implementation (LanceDBVectorStore) by exercising common operations such as creating and deleting collections, loading documents, performing vector similarity searches, applying filters, and ensuring basic vector store functionality works as expected in an integration test context.

Summary:
This test class uses sample_documents and sample_documents_categories helpers to generate VectorStoreDocument instances and relies on a simple mock_embedder that returns a fixed embedding [0.1, 0.2, 0.3, 0.4, 0.5]. It includes tests for:
- test_empty_collection
- test_vector_store_customization
- test_filter_search
- test_vector_store_operations

Inferred key attributes:
No explicit instance attributes are documented; the tests rely on the imports of VectorStoreDocument and LanceDBVectorStore, as well as the helper methods.

## Methods

### `sample_documents_categories`

```python
def sample_documents_categories(self)
```

### `sample_documents`

```python
def sample_documents(self)
```

### `test_empty_collection`

```python
def test_empty_collection(self)
```

### `test_vector_store_customization`

```python
def test_vector_store_customization(self, sample_documents)
```

### `test_filter_search`

```python
def test_filter_search(self, sample_documents_categories)
```

### `test_vector_store_operations`

```python
def test_vector_store_operations(self, sample_documents)
```

### `mock_embedder`

```python
def mock_embedder(text: str) -> list[float]
```

