---
sidebar_position: 460
---

# pytest_generate_tests

**File:** `tests/smoke/test_fixtures.py` (lines 51-68)

## Signature

```python
def pytest_generate_tests(metafunc)
```

## Description

Generate parameterized tests for all test functions in this module.

Args:
metafunc: The pytest metafunc object used to inspect, filter, and parametrize tests.

Returns:
None

Raises:
KeyError: If the expected per-function configuration is missing from metafunc.cls.params for the given function name.
AttributeError: If expected attributes are not present on metafunc (e.g., metafunc.function or metafunc.cls).

