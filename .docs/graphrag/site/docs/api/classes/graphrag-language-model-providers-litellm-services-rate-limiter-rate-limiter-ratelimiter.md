---
sidebar_position: 47
---

# RateLimiter

**File:** `graphrag/language_model/providers/litellm/services/rate_limiter/rate_limiter.py`

## Overview

RateLimiter is an abstract base class that defines the interface for rate limiting strategies. Concrete subclasses must implement their own initialization logic and provide a concrete acquire method that returns a context manager guarding a request.

Args:
  kwargs: Additional keyword arguments passed to initialization. Subclasses may use them to configure the limiter; the base class does not perform concrete initialization.
Returns:
  None
Notes:
  This class is abstract and cannot be instantiated. Subclasses must implement acquire to provide a concrete rate-limiting context manager.

Acquire:
  token_count (int): The estimated number of tokens for the current request.
  Returns:
    ContextManager[None]: A context manager that yields None and guards the request.

## Methods

### `__init__`

```python
def __init__(
        self,
        /,
        **kwargs: Any,
    ) -> None
```

### `acquire`

```python
def acquire(self, *, token_count: int) -> Iterator[None]
```

