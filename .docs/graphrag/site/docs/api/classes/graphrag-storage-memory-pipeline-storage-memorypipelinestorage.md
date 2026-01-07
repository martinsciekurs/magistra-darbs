---
sidebar_position: 30
---

# MemoryPipelineStorage

**File:** `graphrag/storage/memory_pipeline_storage.py`

## Overview

Memory-based storage backend for pipeline data.

This class implements an in-memory storage backend that stores key-value pairs in a
Python dictionary in memory and conforms to the PipelineStorage interface. It provides
fast, non-persistent storage for pipeline data and supports creating child storages for
isolated namespaces.

Attributes:
- _storage: dict[str, Any] storing the in-memory mapping of keys to values.

Args:
  self (MemoryPipelineStorage): The instance being initialized. No additional parameters.

Returns:
  None

## Methods

### `clear`

```python
def clear(self) -> None
```

### `keys`

```python
def keys(self) -> list[str]
```

### `delete`

```python
def delete(self, key: str) -> None
```

### `has`

```python
def has(self, key: str) -> bool
```

### `set`

```python
def set(self, key: str, value: Any, encoding: str | None = None) -> None
```

### `__init__`

```python
def __init__(self)
```

### `get`

```python
def get(
        self, key: str, as_bytes: bool | None = None, encoding: str | None = None
    ) -> Any
```

### `child`

```python
def child(self, name: str | None) -> "PipelineStorage"
```

