---
sidebar_position: 540
---

# test_rate_limiter_validation

**File:** `tests/unit/litellm_services/test_rate_limiter.py` (lines 49-90)

## Signature

```python
def test_rate_limiter_validation()
```

## Description

Test rate limiter creation covering both valid and invalid parameter scenarios.

This test exercises creating a rate limiter with valid parameters as well as handling various invalid inputs, including an unknown strategy, missing TPM/RPM, negative RPM or TPM, and an invalid period_in_seconds. The test function takes no explicit parameters and returns None implicitly.

