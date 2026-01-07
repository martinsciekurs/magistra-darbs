---
sidebar_position: 543
---

# test_rpm

**File:** `tests/unit/litellm_services/test_rate_limiter.py` (lines 93-118)

## Signature

```python
def test_rpm()
```

## Description

Test that the rate limiter enforces RPM limits.

Args:
    None

Returns:
    None

Raises:
    AssertionError: If any assertion fails during the test.

## Dependencies

This function calls:

- `tests/unit/litellm_services/utils.py::assert_max_num_values_per_period`
- `tests/unit/litellm_services/utils.py::assert_stagger`
- `tests/unit/litellm_services/utils.py::bin_time_intervals`

