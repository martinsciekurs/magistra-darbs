---
sidebar_position: 484
---

# assert_drift_search_configs

**File:** `tests/unit/config/utils.py` (lines 346-376)

## Signature

```python
def assert_drift_search_configs(
    actual: DRIFTSearchConfig, expected: DRIFTSearchConfig
) -> None
```

## Description

Assert that two DRIFTSearchConfig objects have equal drift-search configuration values.

Args:
    actual: The actual DRIFTSearchConfig to validate.
    expected: The expected DRIFTSearchConfig to compare against.

Returns:
    None

Raises:
    AssertionError: If any corresponding fields differ between actual and expected.

## Called By

This function is called by:

- `tests/unit/config/utils.py::assert_graphrag_configs`

