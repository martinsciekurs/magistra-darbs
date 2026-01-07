---
sidebar_position: 370
---

# to_dict

**File:** `graphrag/query/input/loaders/utils.py` (lines 138-159)

## Signature

```python
def to_dict(
    data: Mapping[str, Any],
    column_name: str | None,
    key_type: type | None = None,
    value_type: type | None = None,
) -> dict
```

## Description

Convert and validate a value to a dict.

This function retrieves a value for the given column from data using _get_value with required=True and validates that the value is a dictionary. If key_type is provided, all keys must be instances of that type. If value_type is provided, all values must be instances of that type. Returns the dict if valid.

Args:
  data: Mapping[str, Any]
      The mapping that contains column values.
  column_name: str | None
      The name of the column to retrieve, or None.
  key_type: type | None
      If provided, require all dict keys to be instances of this type.
  value_type: type | None
      If provided, require all dict values to be instances of this type.

Returns:
  dict: The validated dictionary retrieved from data.

Raises:
  ValueError: If column_name is None or not in data.
  TypeError: If the value is not a dict, or if any keys/values do not match the provided types.

## Dependencies

This function calls:

- `graphrag/query/input/loaders/utils.py::_get_value`

