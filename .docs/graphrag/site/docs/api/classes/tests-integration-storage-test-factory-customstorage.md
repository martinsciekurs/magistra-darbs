---
sidebar_position: 1
---

# CustomStorage

**File:** `tests/integration/storage/test_factory.py`

## Overview

CustomStorage: Test double implementing the PipelineStorage interface for integration tests.

This class provides a minimal storage backend used in tests to validate StorageFactory behavior by implementing the methods defined in PipelineStorage: get, get_creation_date, delete, find, keys, child, has, clear, and set. The constructor accepts arbitrary keyword arguments which are ignored.

Args:
    kwargs (dict[str, Any]): Keyword arguments passed to the initializer. They are ignored.

Returns:
    None

Raises:
    None

## Methods

### `get`

```python
def get(
            self, key: str, as_bytes: bool | None = None, encoding: str | None = None
        ) -> Any
```

### `get_creation_date`

```python
def get_creation_date(self, key: str) -> str
```

### `delete`

```python
def delete(self, key: str) -> None
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

### `keys`

```python
def keys(self) -> list[str]
```

### `child`

```python
def child(self, name: str | None) -> "PipelineStorage"
```

### `has`

```python
def has(self, key: str) -> bool
```

### `clear`

```python
def clear(self) -> None
```

### `set`

```python
def set(self, key: str, value: Any, encoding: str | None = None) -> None
```

### `__init__`

```python
def __init__(self, **kwargs)
```

