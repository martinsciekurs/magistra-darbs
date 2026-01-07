---
sidebar_position: 72
---

# ExponentialRetry

**File:** `graphrag/language_model/providers/litellm/services/retry/exponential_retry.py`

## Overview

ExponentialRetry provides exponential backoff retry logic for both synchronous and asynchronous callables, with optional jitter.

Args:
  max_retries: int. Maximum number of retry attempts. Must be greater than 0. Default: 5.
  base_delay: float. Base delay between retries in seconds. Must be greater than 0.0. Default: 2.0.
  jitter: bool. If True, apply a small random jitter to each delay. Default: True.
  kwargs: Any. Additional keyword arguments accepted for forward compatibility; not used by the retry logic.

Attributes:
  max_retries: int
  base_delay: float
  jitter: bool
  _logger: logging.Logger (internal). Diagnostic logger for retry events.

Notes:
  - Jitter, when enabled, adds randomness to delays to reduce thundering herd problems and applies to both retry and aretry paths.
  - The retry behavior is determined by the configured max_retries, base_delay, and jitter; delays are computed according to an exponential backoff scheme.
  - This class is intended to be instantiated with the given configuration and used to invoke retry on synchronous functions or aretry on asynchronous functions.

Raises:
  ValueError: If max_retries &lt;= 0 or base_delay &lt;= 0.0.

## Methods

### `__init__`

```python
def __init__(
        self,
        *,
        max_retries: int = 5,
        base_delay: float = 2.0,
        jitter: bool = True,
        **kwargs: Any,
    )
```

### `retry`

```python
def retry(self, func: Callable[..., Any], **kwargs: Any) -> Any
```

### `aretry`

```python
def aretry(
        self,
        func: Callable[..., Awaitable[Any]],
        **kwargs: Any,
    ) -> Any
```

