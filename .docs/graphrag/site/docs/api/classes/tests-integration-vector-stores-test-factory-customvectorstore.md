---
sidebar_position: 25
---

# CustomVectorStore

**File:** `tests/integration/vector_stores/test_factory.py`

## Overview

Test utility vector store used in tests that forwards initialization to the base vector store.

This class provides a minimal implementation of the vector store interface to support tests by forwarding keyword arguments to BaseVectorStore.__init__.

Args:
  kwargs: dict of keyword arguments forwarded to BaseVectorStore.__init__

Returns:
  None

Raises:
  Propagates exceptions raised by BaseVectorStore.__init__

## Methods

### `similarity_search_by_text`

```python
def similarity_search_by_text(self, text, text_embedder, k=10, **kwargs)
```

### `filter_by_id`

```python
def filter_by_id(self, include_ids)
```

### `connect`

```python
def connect(self, **kwargs)
```

### `similarity_search_by_vector`

```python
def similarity_search_by_vector(self, query_embedding, k=10, **kwargs)
```

### `__init__`

```python
def __init__(self, **kwargs)
```

### `load_documents`

```python
def load_documents(self, documents, overwrite=True)
```

### `search_by_id`

```python
def search_by_id(self, id)
```

