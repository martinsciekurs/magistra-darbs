---
sidebar_position: 369
---

# to_float

**File:** `graphrag/query/input/loaders/utils.py` (lines 117-123)

## Signature

```python
def to_float(data: Mapping[str, Any], column_name: str | None) -> float
```

## Description

Convert and validate a value to a float.

Args:
    data: The mapping that contains column values.
    column_name: The name of the column to retrieve, or None.

Returns:
    float: The value as a float.

Raises:
    TypeError: If the retrieved value is not a float.

## Dependencies

This function calls:

- `graphrag/query/input/loaders/utils.py::_get_value`

