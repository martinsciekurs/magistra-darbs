---
sidebar_position: 412
---

# pytest_addoption

**File:** `tests/conftest.py` (lines 5-8)

## Signature

```python
def pytest_addoption(parser)
```

## Description

Register the pytest option --run_slow to run slow tests.

Parameters:
    parser: object
        The pytest parser object used to register command-line options.

Returns:
    None
        The function does not return a value.

