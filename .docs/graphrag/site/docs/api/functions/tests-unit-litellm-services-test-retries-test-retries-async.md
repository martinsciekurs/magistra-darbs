---
sidebar_position: 550
---

# test_retries_async

**File:** `tests/unit/litellm_services/test_retries.py` (lines 113-148)

## Signature

```python
def test_retries_async(
    strategy: str, max_retries: int, max_retry_wait: int, expected_time: float
) -> None
```

## Description

Test various retry strategies asynchronously.

Args:
    strategy: The retry strategy to use.
    max_retries: The maximum number of retry attempts.
    max_retry_wait: The maximum wait time between retries.
    expected_time: The minimum elapsed time expected for the retries to complete.
Returns:
    None
Raises:
    ValueError

