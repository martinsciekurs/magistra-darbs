---
sidebar_position: 363
---

# to_optional_dict

**File:** `graphrag/query/input/loaders/utils.py` (lines 162-187)

## Signature

```python
def to_optional_dict(
    data: Mapping[str, Any],
    column_name: str | None,
    key_type: type | None = None,
    value_type: type | None = None,
) -> dict | None
```

## Description

Convert and validate a value to an optional dict.

Args:
    data: Mapping[str, Any]
        Input data container.
    column_name: str | None
        The key in data to retrieve. If None or not present, returns None.
    key_type: type | None
        If provided, require all dict keys to be instances of this type.
    value_type: type | None
        If provided, require all dict values to be instances of this type.

Returns:
    dict | None
        The extracted dict if present and not None; otherwise None.

Raises:
    TypeError
        If the value associated with column_name is not a dict, or if any dict key does not
        match key_type, or if any dict value does not match value_type.

## Called By

This function is called by:

- `graphrag/query/input/loaders/dfs.py::read_communities`
- `graphrag/query/input/loaders/dfs.py::read_text_units`

