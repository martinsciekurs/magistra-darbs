---
sidebar_position: 461
---

# wrapper

**File:** `tests/smoke/test_fixtures.py` (lines 76-85)

## Signature

```python
def wrapper(*args, **kwargs)
```

## Description

Wrapper around the wrapped test function that forwards arguments and cleans up after execution when not skipped.

Args:
    args: Positional arguments forwarded to the wrapped function.
    kwargs: Keyword arguments forwarded to the wrapped function; must include input_path used for cleanup.

Returns:
    Any: The return value of the wrapped function.

Raises:
    AssertionError: The wrapped function's AssertionError is re-raised.

