---
sidebar_position: 457
---

# cleanup

**File:** `tests/smoke/test_fixtures.py` (lines 71-89)

## Signature

```python
def cleanup(skip: bool = False)
```

## Description

Decorator to cleanup the output and cache folders after each test.

Args:
- skip: bool, optional. If True, skip cleanup of output and cache folders. Default is False.

Returns:
- A decorator that wraps a test function and performs cleanup after the test.

Raises:
- AssertionError: If the wrapped function raises an AssertionError, it is re-raised.

