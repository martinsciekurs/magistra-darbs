---
sidebar_position: 367
---

# to_list

**File:** `graphrag/query/input/loaders/utils.py` (lines 49-64)

## Signature

```python
def to_list(
    data: Mapping[str, Any], column_name: str | None, item_type: type | None = None
) -> list
```

## Description

Convert and validate a value to a list.

This function retrieves the value for the given column from data using _get_value with required=True. If the value is a numpy.ndarray, it is converted to a Python list before validation. If the resulting value is not a list, a TypeError is raised. If item_type is provided, all items in the list must be instances of that type; otherwise a TypeError is raised.

Args:
    data (Mapping[str, Any]): The mapping that contains column values.
    column_name (str | None): The name of the column to retrieve, or None. If None or missing, _get_value will raise ValueError.
    item_type (type | None): Optional type that each item in the resulting list must be.

Returns:
    list: The converted and validated list.

Raises:
    TypeError: If the value is not a list, or any list item is not of the specified item_type.
    ValueError: If column_name is None or the column is missing from data (via _get_value).

## Dependencies

This function calls:

- `graphrag/query/input/loaders/utils.py::_get_value`

## Called By

This function is called by:

- `graphrag/query/input/loaders/dfs.py::read_communities`

