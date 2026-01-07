---
sidebar_position: 364
---

# to_optional_list

**File:** `graphrag/query/input/loaders/utils.py` (lines 67-88)

## Signature

```python
def to_optional_list(
    data: Mapping[str, Any], column_name: str | None, item_type: type | None = None
) -> list | None
```

## Description

Convert and validate a value to an optional list.

This function retrieves the value for column_name from data. If column_name is None or not present in data, or if the value is None, it returns None. If the value is a numpy array, it is converted to a Python list. If the value is a string, it is wrapped in a single-element list. If the resulting value is not a list, a TypeError is raised. If item_type is provided, every element in the list must be an instance of item_type; otherwise a TypeError is raised.

Args:
  data: Mapping[str, Any]
      Input data container.
  column_name: str | None
      The key in data to retrieve. If None or not present, returns None. If present but value is None, also returns None.
  item_type: type | None
      If provided, require all list items to be instances of this type.

Returns:
  list | None
      The optional list value, or None if the key is missing or its value is None.

Raises:
  TypeError
      If the retrieved value cannot be converted to a list or if any list item is not of the specified item_type.

## Called By

This function is called by:

- `graphrag/query/input/loaders/dfs.py::read_entities`
- `graphrag/query/input/loaders/dfs.py::read_relationships`
- `graphrag/query/input/loaders/dfs.py::read_covariates`
- `graphrag/query/input/loaders/dfs.py::read_communities`
- `graphrag/query/input/loaders/dfs.py::read_community_reports`
- `graphrag/query/input/loaders/dfs.py::read_text_units`

