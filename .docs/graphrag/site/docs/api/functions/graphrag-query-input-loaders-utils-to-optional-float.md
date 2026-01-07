---
sidebar_position: 360
---

# to_optional_float

**File:** `graphrag/query/input/loaders/utils.py` (lines 126-135)

## Signature

```python
def to_optional_float(data: Mapping[str, Any], column_name: str | None) -> float | None
```

## Description

Convert a value to an optional float.

If the specified column is missing or its value is None, returns None. Otherwise, converts the value to a float using Python's built-in float().

Args:
    data (Mapping[str, Any]): Input data mapping containing potential value
    column_name (str | None): Key to retrieve from data; if None or not present, returns None

Returns:
    float | None: The value converted to a float, or None if the column is missing or its value is None

Raises:
    ValueError: If the value cannot be converted to a float (e.g., non-numeric strings).
    TypeError: If the value type is not compatible with float().
    OverflowError: If the numeric value is too large to convert.

Notes:
    - If column_name is None or not present in data, returns None.
    - If the value is None, returns None.
    - Non-numeric inputs that cannot be parsed as float will raise ValueError.

## Example 💡 Generated

```python
from module import to_optional_float
row = {"weight": "72.5", "rank": 3}
weight_col, rank_col = "weight", "rank"
weight = to_optional_float(row, weight_col)
rank = to_optional_float(row, rank_col)
# expected: weight 72.5, rank 3.0
```

## Called By

This function is called by:

- `graphrag/query/input/loaders/dfs.py::read_relationships`
- `graphrag/query/input/loaders/dfs.py::read_community_reports`

