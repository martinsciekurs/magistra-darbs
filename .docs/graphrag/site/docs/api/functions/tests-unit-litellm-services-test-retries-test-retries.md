---
sidebar_position: 551
---

# test_retries

**File:** `tests/unit/litellm_services/test_retries.py` (lines 46-81)

## Signature

```python
def test_retries(
    strategy: str, max_retries: int, max_retry_wait: int, expected_time: float
) -> None
```

## Description

Test various retry strategies by exercising a mock function that raises an exception to verify retry behavior and timing.

Args
    strategy: The retry strategy to use.
    max_retries: The maximum number of retry attempts.
    max_retry_wait: The maximum wait time between retries.
    expected_time: The minimum elapsed time expected for the retries to complete.

Returns
    None

Raises
    ValueError: Raised by the mock function to simulate a failed operation.

