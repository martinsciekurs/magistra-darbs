---
sidebar_position: 196
---

# dict_has_keys_with_types

**File:** `graphrag/index/utils/dicts.py` (lines 7-22)

## Signature

```python
def dict_has_keys_with_types(
    data: dict, expected_fields: list[tuple[str, type]], inplace: bool = False
) -> bool
```

## Description

Check that a dictionary contains the specified keys and that their values can be cast to the provided types.

Args:
    data: The dictionary to inspect and (optionally) mutate.
    expected_fields: A list of (key, type) pairs describing the required keys and the types their values must be cast to.
    inplace: If True, casted values are written back into the dictionary for the corresponding keys.

Returns:
    bool: True if all specified keys exist in the dictionary and their values can be cast to the given types; otherwise False.

