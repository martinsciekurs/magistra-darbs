---
sidebar_position: 365
---

# to_str

**File:** `graphrag/query/input/loaders/utils.py` (lines 37-40)

## Signature

```python
def to_str(data: Mapping[str, Any], column_name: str | None) -> str
```

## Description

Convert and validate a value to a string.

Args:
  data (Mapping[str, Any]): The mapping that contains column values.
  column_name (str | None): The name of the column to retrieve, or None.

Returns:
  str: The string representation of the value.

Raises:
  ValueError: If column_name is None or the column is missing from data.

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
- `graphrag/query/input/loaders/dfs.py::read_text_units`

