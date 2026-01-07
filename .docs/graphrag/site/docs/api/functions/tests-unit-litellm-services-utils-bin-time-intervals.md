---
sidebar_position: 554
---

# bin_time_intervals

**File:** `tests/unit/litellm_services/utils.py` (lines 7-23)

## Signature

```python
def bin_time_intervals(
    time_values: list[float], time_interval: int
) -> list[list[float]]
```

## Description

Bin time values into consecutive time-based intervals.

Args:
    time_values: list[float] - Input time values to bin.
    time_interval: int - Size of each time interval.

Returns:
    list[list[float]] - A list of bins, where each inner list contains the values that fall into the corresponding time interval. The i-th bin contains values in the interval [i * time_interval, (i + 1) * time_interval).

Raises:
    None

## Called By

This function is called by:

- `tests/unit/litellm_services/test_rate_limiter.py::test_binning`
- `tests/unit/litellm_services/test_rate_limiter.py::test_rpm`
- `tests/unit/litellm_services/test_rate_limiter.py::test_tpm`
- `tests/unit/litellm_services/test_rate_limiter.py::test_token_in_request_exceeds_tpm`
- `tests/unit/litellm_services/test_rate_limiter.py::test_rpm_and_tpm_with_rpm_as_limiting_factor`
- `tests/unit/litellm_services/test_rate_limiter.py::test_rpm_and_tpm_with_tpm_as_limiting_factor`
- `tests/unit/litellm_services/test_rate_limiter.py::test_rpm_threaded`
- `tests/unit/litellm_services/test_rate_limiter.py::test_tpm_threaded`

