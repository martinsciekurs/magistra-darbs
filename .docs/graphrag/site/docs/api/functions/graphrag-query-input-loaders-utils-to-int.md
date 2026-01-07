---
sidebar_position: 368
---

# to_int

**File:** `graphrag/query/input/loaders/utils.py` (lines 91-99)

## Signature

```python
def to_int(data: Mapping[str, Any], column_name: str | None) -> int
```

## Description

Convert and validate a value to an int. The value is retrieved from data via _get_value(data, column_name, required=True). If the retrieved value is a Python float, it is truncated to an integer. After conversion, if the value is not a Python int, a TypeError is raised.

Args:
    data (Mapping[str, Any]): The mapping that contains column values.
    column_name (str | None): The name of the column to retrieve from data. If None or the column is missing, _get_value will raise a ValueError.

Returns:
    int: The value converted to int.

Raises:
    ValueError: If column_name is None or the column_name is not present in data (as raised by _get_value with required=True).
    TypeError: If the retrieved value cannot be interpreted as an int after any necessary conversion. Note that numpy integer types (e.g., np.int64) are not treated as ints and will trigger this error.

## Dependencies

This function calls:

- `graphrag/query/input/loaders/utils.py::_get_value`

