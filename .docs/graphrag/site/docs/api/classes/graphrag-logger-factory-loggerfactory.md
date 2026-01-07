---
sidebar_position: 63
---

# LoggerFactory

**File:** `graphrag/logger/factory.py`

## Overview

LoggerFactory is a registry-based factory for creating logging.Handler instances for various reporting types.

Purpose:
- Maintain an internal registry mapping reporting_type identifiers to creator callables.
- Provide a classmethod-based interface to register new loggers, check supported types, create loggers for a given type, and retrieve the set of available types.

Attributes:
- _registry: ClassVar[dict[str, Callable[..., logging.Handler]]]
    Internal registry that maps a reporting_type string to a creator callable that returns a logging.Handler instance when invoked with appropriate keyword arguments.

Summary:
The class acts as a centralized factory and registry for logger handlers. Client code can register new logger implementations, query supported types, and request a handler for a specific reporting type. All operations are performed at the class level.

## Methods

### `create_logger`

```python
def create_logger(cls, reporting_type: str, kwargs: dict) -> logging.Handler
```

### `is_supported_type`

```python
def is_supported_type(cls, reporting_type: str) -> bool
```

### `register`

```python
def register(
        cls, reporting_type: str, creator: Callable[..., logging.Handler]
    ) -> None
```

### `get_logger_types`

```python
def get_logger_types(cls) -> list[str]
```

