---
sidebar_position: 366
---

# to_optional_str

**File:** `graphrag/query/input/loaders/utils.py` (lines 43-46)

## Signature

```python
def to_optional_str(data: Mapping[str, Any], column_name: str | None) -> str | None
```

## Description

Convert and validate a value to an optional string.

Retrieve the value for column_name from data and convert it to a string if it is not None. If the value is None, returns None. If column_name is None or not present in data, raises ValueError.

Args:
    data (Mapping[str, Any]): Input data mapping containing column values.
    column_name (str | None): The name of the column to retrieve. If None or not present in data, a ValueError will be raised.

Returns:
    str | None: The string representation of the value, or None if the value is None.

Raises:
    ValueError: If column_name is None or column_name is not found in data.

## Dependencies

This function calls:

- `graphrag/query/input/loaders/utils.py::_get_value`

## Called By

This function is called by:

- `graphrag/query/input/loaders/dfs.py::read_entities`
- `graphrag/query/input/loaders/dfs.py::read_relationships`
- `graphrag/query/input/loaders/dfs.py::read_covariates`
- `graphrag/query/input/loaders/dfs.py::read_communities`
- `graphrag/query/input/loaders/dfs.py::read_community_reports`

