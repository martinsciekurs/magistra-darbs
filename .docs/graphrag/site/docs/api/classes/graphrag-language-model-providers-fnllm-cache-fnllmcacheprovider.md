---
sidebar_position: 10
---

# FNLLMCacheProvider

**File:** `graphrag/language_model/providers/fnllm/cache.py`

## Overview

FNLLMCacheProvider adapts a PipelineCache to the FNLLM cache interface by delegating all cache operations to the underlying cache instance.

Attributes:
- _cache: The underlying cache instance used by this provider to perform cache operations.

Args:
  cache: The underlying PipelineCache instance used by this provider.

Returns:
  None

Raises:
  Exceptions may propagate from the underlying cache operations.

## Methods

### `clear`

```python
def clear(self) -> None
```

### `get`

```python
def get(self, key: str) -> Any | None
```

### `has`

```python
def has(self, key: str) -> bool
```

### `remove`

```python
def remove(self, key: str) -> None
```

### `__init__`

```python
def __init__(self, cache: PipelineCache)
```

### `set`

```python
def set(
        self, key: str, value: Any, metadata: dict[str, Any] | None = None
    ) -> None
```

### `child`

```python
def child(self, key: str) -> "FNLLMCacheProvider"
```

