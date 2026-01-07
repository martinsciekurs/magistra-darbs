---
sidebar_position: 546
---

# test_rpm_and_tpm_with_rpm_as_limiting_factor

**File:** `tests/unit/litellm_services/test_rate_limiter.py` (lines 178-204)

## Signature

```python
def test_rpm_and_tpm_with_rpm_as_limiting_factor()
```

## Description

Test that the rate limiter enforces RPM and TPM limits.

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

