---
sidebar_position: 362
---

# to_optional_int

**File:** `graphrag/query/input/loaders/utils.py` (lines 102-114)

## Signature

```python
def to_optional_int(data: Mapping[str, Any], column_name: str | None) -> int | None
```

## Description

Convert and validate a value to an optional int.

If the specified column is missing from data or is None, returns None. If the value is a float, it will be converted to an int by truncation. If the resulting value is not an int, a TypeError is raised.

Args:
    data (Mapping[str, Any]): Input data mapping containing potential value
    column_name (str | None): Key to retrieve from data; if None or not present, returns None

Returns:
    int | None: The value converted to int, or None if missing or None

Raises:
    TypeError: If the value cannot be interpreted as an int after conversion

## Called By

This function is called by:

- `graphrag/query/input/loaders/dfs.py::read_entities`
- `graphrag/query/input/loaders/dfs.py::read_relationships`
- `graphrag/query/input/loaders/dfs.py::read_text_units`

