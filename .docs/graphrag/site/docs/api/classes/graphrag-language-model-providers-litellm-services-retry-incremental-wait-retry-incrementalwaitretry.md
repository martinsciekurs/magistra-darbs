---
sidebar_position: 23
---

# IncrementalWaitRetry

**File:** `graphrag/language_model/providers/litellm/services/retry/incremental_wait_retry.py`

## Overview

IncrementalWaitRetry provides a retry strategy that inserts incremental delays between attempts for both asynchronous and synchronous callables.

Attributes:
  max_retry_wait (float): The maximum delay between retries in seconds.
  max_retries (int): The maximum number of retry attempts.
  base_delay (float, optional): Optional initial delay used in the incremental computation.
  delay_increment (float, optional): Optional per-retry increment for the incremental delay.

Delay calculation:
  The delay before the nth retry is computed as:
  delay_n = min(max_retry_wait, base_delay + (n - 1) * delay_increment)
  where n starts at 1 for the first retry. If base_delay or delay_increment are not provided, the implementation uses sensible defaults.

aretry:
  Retry an asynchronous callable until success or the maximum number of retries is reached. The function is invoked as await func(**kwargs). The computed incremental delay is applied between attempts. Returns the result of the awaited function on success; if all retries fail, the last raised exception is propagated.

retry:
  Retry a synchronous callable until success or the maximum number of retries is reached. The function is invoked as func(**kwargs). The computed incremental delay is applied between attempts. Returns the value returned by the wrapped function on success; if all retries fail, the last raised exception is propagated.

Raises:
  ValueError: max_retries must be greater than 0.
  ValueError: max_retry_wait must be greater than 0.

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

