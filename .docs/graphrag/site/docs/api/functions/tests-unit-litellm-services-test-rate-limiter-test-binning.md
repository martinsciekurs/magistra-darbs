---
sidebar_position: 542
---

# test_binning

**File:** `tests/unit/litellm_services/test_rate_limiter.py` (lines 35-46)

## Signature

```python
def test_binning()
```

## Description

Bin time values into consecutive time-based intervals.

Args:
    time_values: list[float] - Input time values to bin.
    time_interval: int - Size of each time interval.

Returns:
    list[list[float]] - A list of bins, where each inner list contains the values that fall into the corresponding time interval. The i-th bin contains values in the interval [i * time_interval, (i + 1) * time_interval).

Raises:
    None...

## Dependencies

This function calls:

- `tests/unit/litellm_services/utils.py::bin_time_intervals`

