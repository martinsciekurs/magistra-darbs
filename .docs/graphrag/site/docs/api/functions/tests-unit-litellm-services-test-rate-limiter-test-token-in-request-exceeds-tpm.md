---
sidebar_position: 545
---

# test_token_in_request_exceeds_tpm

**File:** `tests/unit/litellm_services/test_rate_limiter.py` (lines 149-175)

## Signature

```python
def test_token_in_request_exceeds_tpm()
```

## Description

Test that the rate limiter allows for requests that use more tokens than the TPM.

A rate limiter could be configured with a tpm of 1000 but a request may use 2000 tokens,
greater than the tpm limit but still below the context window limit of the underlying model.
In this case, the request should still be allowed to proceed but may take up its own rate limit bin.

## Dependencies

This function calls:

- `tests/unit/litellm_services/utils.py::assert_max_num_values_per_period`
- `tests/unit/litellm_services/utils.py::bin_time_intervals`

