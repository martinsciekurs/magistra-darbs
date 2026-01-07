---
sidebar_position: 41
---

# FilePipelineStorage

**File:** `graphrag/storage/file_pipeline_storage.py`

## Overview

File-based storage backend for a pipeline that stores items as individual files under a root directory. This class implements the PipelineStorage interface and provides filesystem-backed operations to read, write, delete, list keys, clear storage, and find files by pattern.

Attributes:
- _root_dir: str - Root directory for storage; created if missing.
- _encoding: str - Text encoding used for file I/O.

Args:
- base_dir: Directory path where files are stored. Defaults to the empty string (uses the current working directory).
- encoding: Text encoding for file operations. Defaults to "utf-8".

Returns:
- None

Raises:
- OSError: If a filesystem operation fails during initialization or storage operations.
- FileNotFoundError: If a file is not found when querying creation date or reading a specific item.

## Methods

### `clear`

```python
def clear(self) -> None
```

### `keys`

```python
def keys(self) -> list[str]
```

### `child`

```python
def child(self, name: str | None) -> "PipelineStorage"
```

### `item_filter`

```python
def item_filter(item: dict[str, Any]) -> bool
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

### `__init__`

```python
def __init__(self, **kwargs: Any) -> None
```

### `_read_file`

```python
def _read_file(
        self,
        path: str | Path,
        as_bytes: bool | None = False,
        encoding: str | None = None,
    ) -> Any
```

### `get`

```python
def get(
        self, key: str, as_bytes: bool | None = False, encoding: str | None = None
    ) -> Any
```

### `set`

```python
def set(self, key: str, value: Any, encoding: str | None = None) -> None
```

### `has`

```python
def has(self, key: str) -> bool
```

### `delete`

```python
def delete(self, key: str) -> None
```

### `get_creation_date`

```python
def get_creation_date(self, key: str) -> str
```

