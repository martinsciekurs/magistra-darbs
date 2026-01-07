---
sidebar_position: 549
---

# test_tpm_threaded

**File:** `tests/unit/litellm_services/test_rate_limiter.py` (lines 311-368)

## Signature

```python
def test_tpm_threaded()
```

## Description

Test that the rate limiter enforces TPM limits in a threaded environment.

Returns:
    None

Raises:
    AssertionError: If any assertion fails during the test.

## Dependencies

This function calls:

- `tests/unit/litellm_services/utils.py::assert_max_num_values_per_period`
- `tests/unit/litellm_services/utils.py::assert_stagger`
- `tests/unit/litellm_services/utils.py::bin_time_intervals`

