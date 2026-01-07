---
sidebar_position: 208
---

# is_none

**File:** `graphrag/index/utils/is_null.py` (lines 13-14)

## Signature

```python
def is_none() -> bool
```

## Description

Check if the input value is None or NaN.

Args:
    value (Any): The value to check.

Returns:
    bool: True if value is None or NaN (NaN is recognized only for floating-point values); otherwise False.

## Called By

This function is called by:

- `graphrag/index/utils/is_null.py::is_null`

