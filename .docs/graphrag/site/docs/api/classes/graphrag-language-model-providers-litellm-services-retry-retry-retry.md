---
sidebar_position: 121
---

# Retry

**File:** `graphrag/language_model/providers/litellm/services/retry/retry.py`

## Overview

Retry is an abstract base class that defines the interface for applying a configurable retry policy to operations.

Purpose
  Provide a pluggable retry mechanism by specifying concrete strategies for retrying both synchronous and asynchronous callables.

Attributes
  This base class does not define concrete state. Subclasses may store configuration (e.g., max_retries, backoff, or jitter) in their own __init__.

Abstract interface
  Concrete subclasses must implement:
    - retry(func: Callable[..., Any], **kwargs: Any) -&gt; Any
      Retry a synchronous function and return the final result of the successful invocation.
    - aretry(func: Callable[..., Awaitable[Any]], **kwargs: Any) -&gt; Any
      Retry an asynchronous function and return the final awaited result.

Initialization
  __init__(self, /, **kwargs: Any)
    Initialize a Retry subclass with arbitrary keyword arguments used to configure the strategy.

Notes
  This class is abstract. Attempting to instantiate it directly or instantiate a subclass that leaves abstract methods unimplemented will raise TypeError (not NotImplementedError).

Args
  kwargs: Arbitrary keyword arguments for subclass initialization.

Raises
  TypeError: If attempting to instantiate this abstract class or a subclass with unimplemented abstract methods.

## Methods

### `retry`

```python
def retry(self, func: Callable[..., Any], **kwargs: Any) -> Any
```

### `__init__`

```python
def __init__(self, /, **kwargs: Any)
```

### `aretry`

```python
def aretry(
        self,
        func: Callable[..., Awaitable[Any]],
        **kwargs: Any,
    ) -> Any
```

