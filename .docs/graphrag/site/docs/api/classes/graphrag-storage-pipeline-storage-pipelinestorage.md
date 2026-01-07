---
sidebar_position: 49
---

# PipelineStorage

**File:** `graphrag/storage/pipeline_storage.py`

## Overview

Abstract base class for storage backends used by the pipeline.

Defines the interface for a key-value style storage with support for existence checks,
pattern-based file discovery, retrieval with optional byte/encoding handling, listing
keys, creation date retrieval, and deletion. Implementations may back the storage with
in-memory structures, filesystem, database, or remote services.

Attributes:
  Not defined at this level. Concrete implementations may define internal state and
  configuration.

## Methods

### `has`

```python
def has(self, key: str) -> bool
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

### `get_creation_date`

```python
def get_creation_date(self, key: str) -> str
```

### `clear`

```python
def clear(self) -> None
```

### `set`

```python
def set(self, key: str, value: Any, encoding: str | None = None) -> None
```

### `keys`

```python
def keys(self) -> list[str]
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

### `delete`

```python
def delete(self, key: str) -> None
```

