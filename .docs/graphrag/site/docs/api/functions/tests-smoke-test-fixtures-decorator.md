---
sidebar_position: 462
---

# decorator

**File:** `tests/smoke/test_fixtures.py` (lines 74-87)

## Signature

```python
def decorator(func)
```

## Description

Decorator factory that wraps a test function to forward all positional and keyword arguments to the wrapped function and to perform post-execution cleanup of test artefacts.

Parameters:
- skip (bool): If True, skip performing cleanup after the wrapped function returns. Defaults to False.

Returns:
- Callable[[Callable[..., Any]], Callable[..., Any]]: A decorator that can be applied to a test function. The decorated function will forward all positional and keyword arguments to the wrapped function and, after execution, clean up the output and cache directories under the root path derived from the input_path keyword argument, unless skip is True.

Notes:
- The cleanup targets are root/output and root/cache, where root is obtained from kwargs["input_path"].
- input_path must be provided in the call to the decorated function, as it is used to determine the cleanup root.
- All positional and keyword arguments are forwarded to the wrapped function. Any AssertionError raised by the wrapped function is propagated.

