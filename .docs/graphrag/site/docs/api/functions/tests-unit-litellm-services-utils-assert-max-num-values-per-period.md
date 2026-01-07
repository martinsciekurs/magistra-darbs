---
sidebar_position: 555
---

# assert_max_num_values_per_period

**File:** `tests/unit/litellm_services/utils.py` (lines 26-31)

## Signature

```python
def assert_max_num_values_per_period(
    periods: list[list[float]], max_values_per_period: int
)
```

## Description

Assert the maximum number of values per period.

Args:
    periods: list[list[float]] - a list of periods; each period is a list of time values
    max_values_per_period: int - the maximum number of values allowed per period

Returns:
    None

Raises:
    AssertionError - if any period contains more values than max_values_per_period

## Called By

This function is called by:

- `tests/unit/litellm_services/test_rate_limiter.py::test_rpm`
- `tests/unit/litellm_services/test_rate_limiter.py::test_tpm`
- `tests/unit/litellm_services/test_rate_limiter.py::test_token_in_request_exceeds_tpm`
- `tests/unit/litellm_services/test_rate_limiter.py::test_rpm_and_tpm_with_rpm_as_limiting_factor`
- `tests/unit/litellm_services/test_rate_limiter.py::test_rpm_and_tpm_with_tpm_as_limiting_factor`
- `tests/unit/litellm_services/test_rate_limiter.py::test_rpm_threaded`
- `tests/unit/litellm_services/test_rate_limiter.py::test_tpm_threaded`

