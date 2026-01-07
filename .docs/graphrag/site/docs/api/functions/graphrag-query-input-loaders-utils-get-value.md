---
sidebar_position: 361
---

# _get_value

**File:** `graphrag/query/input/loaders/utils.py` (lines 12-34)

## Signature

```python
def _get_value(
    data: Mapping[str, Any], column_name: str | None, required: bool = True
) -> Any
```

## Description

Retrieve a value for a column from the given data mapping.

If the column is required (required=True), raises ValueError when:
- column_name is None, or
- column_name is not in data.

For optional columns (required=False), returns None when column_name is None or when the column is missing from data.

Args:
    data: Mapping[str, Any]
        The mapping that contains column values.
    column_name: str | None
        The name of the column to retrieve, or None.
    required: bool
        Whether the column must be present in data.

Returns:
    Any
        The value associated with column_name in data if present; otherwise None when
        the column is optional and missing, or when column_name is None and required is False.

Raises:
    ValueError
        If column_name is None and required is True, or if column_name is not in data and
        required is True.

## Example 💡 Generated

```python
from mymodule import _get_value
data = {"id": 1, "name": "Alice"}
print(_get_value(data, 'name', required=True))  # Alice
data2 = {"id": 1}
print(_get_value(data2, 'age', required=False))  # None
# outputs: 'Alice' and None
```

## Called By

This function is called by:

- `graphrag/query/input/loaders/utils.py::to_str`
- `graphrag/query/input/loaders/utils.py::to_optional_str`
- `graphrag/query/input/loaders/utils.py::to_list`
- `graphrag/query/input/loaders/utils.py::to_int`
- `graphrag/query/input/loaders/utils.py::to_float`
- `graphrag/query/input/loaders/utils.py::to_dict`

