---
sidebar_position: 481
---

# assert_reporting_configs

**File:** `tests/unit/config/utils.py` (lines 129-136)

## Signature

```python
def assert_reporting_configs(
    actual: ReportingConfig, expected: ReportingConfig
) -> None
```

## Description

Assert that two ReportingConfig objects have identical field values.

Parameters:
- actual: ReportingConfig - The actual ReportingConfig instance.
- expected: ReportingConfig - The expected ReportingConfig instance to compare against.

Returns:
- None

Raises:
- AssertionError: If any of the fields differ between actual and expected.

## Called By

This function is called by:

- `tests/unit/config/utils.py::assert_graphrag_configs`

