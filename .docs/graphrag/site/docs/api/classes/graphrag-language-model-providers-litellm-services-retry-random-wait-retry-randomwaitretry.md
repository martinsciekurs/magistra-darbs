---
sidebar_position: 2
---

# RandomWaitRetry

**File:** `graphrag/language_model/providers/litellm/services/retry/random_wait_retry.py`

## Overview

Retry policy that retries both asynchronous and synchronous functions using a random delay between attempts, up to a configurable maximum number of retries.

Args:
    max_retry_wait: The maximum delay, in seconds, between retries. The actual delay is drawn uniformly from [0, max_retry_wait].
    max_retries: The maximum number of retry attempts. Must be greater than 0.
    kwargs: Additional keyword arguments accepted by the constructor (for extensibility).

Returns:
    None

Raises:
    ValueError: If max_retries &lt;= 0 or max_retry_wait &lt;= 0.

Attributes:
    max_retry_wait: float - maximum delay (seconds) between retries.
    max_retries: int - maximum number of retry attempts.
    logger: logging.Logger - internal logger for debug messages (if initialized).

Summary:
    - aretry retries an asynchronous function by awaiting func(**kwargs) until it succeeds or max_retries is reached; returns the result on success.
    - retry retries a synchronous function by invoking func(**kwargs) until it succeeds or max_retries is reached; returns the result on success.
    - The delay before each retry is a random value drawn uniformly from [0, max_retry_wait]. For the async path this is implemented via await asyncio.sleep(delay); for the sync path this uses time.sleep(delay).
    - If all attempts fail, the last raised exception is propagated to the caller.

## Methods

### `__init__`

```python
def __init__(
        self,
        *,
        max_retry_wait: float,
        max_retries: int = 5,
        **kwargs: Any,
    )
```

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

