---
sidebar_position: 544
---

# test_tpm

**File:** `tests/unit/litellm_services/test_rate_limiter.py` (lines 121-146)

## Signature

```python
def test_tpm()
```

## Description

Test that the rate limiter enforces TPM limits.

This test creates a rate limiter with a static strategy configured with a TPM and a period,
then issues _num_requests token acquisitions with token_count set to _tokens_per_request and
records the time elapsed for each. The recorded times are binned into intervals of _period_in_seconds.
The test expects the number of bins to be equal to ceil((_num_requests * _tokens_per_request) / _tpm)
and that the maximum number of requests per bin is _tpm // _tokens_per_request.

Returns:
    None

Raises:
    AssertionError: If TPM constraints are violated.

## Dependencies

This function calls:

- `tests/unit/litellm_services/utils.py::assert_max_num_values_per_period`
- `tests/unit/litellm_services/utils.py::bin_time_intervals`

