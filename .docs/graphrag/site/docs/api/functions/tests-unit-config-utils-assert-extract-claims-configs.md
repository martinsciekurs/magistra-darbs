---
sidebar_position: 474
---

# assert_extract_claims_configs

**File:** `tests/unit/config/utils.py` (lines 292-300)

## Signature

```python
def assert_extract_claims_configs(
    actual: ClaimExtractionConfig, expected: ClaimExtractionConfig
) -> None
```

## Description

Assert that the actual and expected ClaimExtractionConfig instances are equal.

This helper asserts that the fields enabled, prompt, description, max_gleanings, strategy, and model_id on actual match those on expected.

Args:
    actual: The actual ClaimExtractionConfig instance produced by the code under test.
    expected: The expected ClaimExtractionConfig instance to compare against.

Returns:
    None

Raises:
    AssertionError: If any of the compared fields differ between actual and expected.

## Called By

This function is called by:

- `tests/unit/config/utils.py::assert_graphrag_configs`

