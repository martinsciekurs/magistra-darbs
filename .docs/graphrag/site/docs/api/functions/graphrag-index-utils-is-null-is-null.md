---
sidebar_position: 209
---

# is_null

**File:** `graphrag/index/utils/is_null.py` (lines 10-19)

## Signature

```python
def is_null(value: Any) -> bool
```

## Description

Check if value is None or NaN.

Args:
    value (Any): The value to check.

Returns:
    bool: True if value is None or NaN (NaN is recognized only for floating-point values); otherwise False.

## Dependencies

This function calls:

- `graphrag/index/utils/is_null.py::is_nan`
- `graphrag/index/utils/is_null.py::is_none`

## Called By

This function is called by:

- `graphrag/index/operations/embed_text/strategies/openai.py::run`

