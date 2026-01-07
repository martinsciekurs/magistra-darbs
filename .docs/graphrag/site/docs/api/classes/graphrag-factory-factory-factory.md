---
sidebar_position: 50
---

# Factory

**File:** `graphrag/factory/factory.py`

## Overview

Factory is a generic, per-subclass singleton that registers and creates service instances by strategy name.

The Factory maintains a registry of strategy names to callables that return instances of T. Strategies can be registered with register, queried with __contains__, listed with keys, and used to create instances with create. Each subclass uses its own singleton instance.

Attributes:
    _services: dict[str, Callable[..., T]] — registry mapping strategy names to callables that produce T instances.

## Methods

### `create`

```python
def create(self, *, strategy: str, **kwargs: Any) -> T
```

### `__contains__`

```python
def __contains__(self, strategy: str) -> bool
```

### `__new__`

```python
def __new__(cls, *args: Any, **kwargs: Any) -> "Factory"
```

### `register`

```python
def register(self, *, strategy: str, service_initializer: Callable[..., T]) -> None
```

### `__init__`

```python
def __init__(self)
```

### `keys`

```python
def keys(self) -> list[str]
```

