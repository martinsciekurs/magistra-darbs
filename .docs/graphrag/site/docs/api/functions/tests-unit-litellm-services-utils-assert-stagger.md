---
sidebar_position: 553
---

# assert_stagger

**File:** `tests/unit/litellm_services/utils.py` (lines 34-37)

## Signature

```python
def assert_stagger(time_values: list[float], stagger: float)
```

## Description

Assert that consecutive time values are at least the specified stagger apart.

Args:
    time_values (list[float]): Sequence of time values.
    stagger (float): Minimum allowed difference between consecutive values.

Returns:
    None: This function does not return a value.

Raises:
    AssertionError: If any consecutive pair of time values is closer than stagger.

## Called By

This function is called by:

- `tests/unit/litellm_services/test_rate_limiter.py::test_rpm`
- `tests/unit/litellm_services/test_rate_limiter.py::test_rpm_and_tpm_with_rpm_as_limiting_factor`
- `tests/unit/litellm_services/test_rate_limiter.py::test_rpm_and_tpm_with_tpm_as_limiting_factor`
- `tests/unit/litellm_services/test_rate_limiter.py::test_rpm_threaded`
- `tests/unit/litellm_services/test_rate_limiter.py::test_tpm_threaded`

