---
sidebar_position: 109
---

# NativeRetry

**File:** `graphrag/language_model/providers/litellm/services/retry/native_wait_retry.py`

## Overview

NativeRetry provides retry logic for both asynchronous and synchronous callables with a configurable maximum number of retries.

Args:
    max_retries: The maximum number of retry attempts. Must be greater than 0.
    kwargs: Additional keyword arguments accepted by the initializer.

Attributes:
    max_retries: The maximum number of retry attempts.

Summary:
    The class is initialized with max_retries (default 5) and exposes two methods:
    aretry(func, **kwargs): Retry an asynchronous function until it succeeds or the maximum number of retries is reached. Returns the result of the awaited function.
    retry(func, **kwargs): Retry a synchronous function until it succeeds or the maximum number of retries is reached. Returns the value returned by the function on success.

Notes:
    Both aretry and retry return the wrapped function's result (not None) when successful. They retry on exceptions raised by the wrapped function. If the maximum number of retries is exceeded, the last exception raised by the wrapped function is propagated.

Returns:
    None

Raises:
    ValueError: max_retries must be greater than 0.
    Exception: If the wrapped function keeps raising and the maximum number of retries is exceeded.

## Methods

### `aretry`

```python
def aretry(
        self,
        func: Callable[..., Awaitable[Any]],
        **kwargs: Any,
    ) -> Any
```

### `retry`

```python
def retry(self, func: Callable[..., Any], **kwargs: Any) -> Any
```

### `__init__`

```python
def __init__(
        self,
        *,
        max_retries: int = 5,
        **kwargs: Any,
    )
```

