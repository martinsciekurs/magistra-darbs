---
sidebar_position: 417
---

# test_get_logger_types

**File:** `tests/integration/logging/test_factory.py` (lines 56-60)

## Signature

```python
def test_get_logger_types()
```

## Description

Verify that built-in logger types are registered and returned by LoggerFactory.get_logger_types.

This test retrieves the list of registered logger types from LoggerFactory and asserts that
ReportingType.file.value and ReportingType.blob.value are present in the result.

Returns:
    None

Raises:
    AssertionError: If the expected logger types are not present in the result.

