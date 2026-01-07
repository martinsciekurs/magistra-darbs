---
sidebar_position: 547
---

# test_rpm_and_tpm_with_tpm_as_limiting_factor

**File:** `tests/unit/litellm_services/test_rate_limiter.py` (lines 207-233)

## Signature

```python
def test_rpm_and_tpm_with_tpm_as_limiting_factor()
```

## Description

Test that the rate limiter enforces TPM limits when TPM is the limiting factor.

This test configures a static rate limiter with rpm, tpm and a period, and issues _num_requests acquisitions
with token_count set to _tokens_per_request (non-zero). It records the elapsed time for each acquisition and bins
the results into intervals of _period_in_seconds. The TPM value drives the binning and per bin capacity.

Expected behavior:
- Number of bins equals ceil((_num_requests * _tokens_per_request) / _tpm).
- Maximum number of requests per bin equals _tpm // _tokens_per_request.

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

