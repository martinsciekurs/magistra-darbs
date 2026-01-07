---
sidebar_position: 589
---

# dataset_name

**File:** `unified-search-app/app/app_logic.py` (lines 63-65)

## Signature

```python
def dataset_name(key: str, sv: SessionVariables) -> str
```

## Description

Get dataset name.

Args:
    key: The dataset key to look up.
    sv: SessionVariables containing dataset information; sv.datasets.value is an iterable of objects with key and name attributes.

Returns:
    The name of the dataset whose key matches the provided key.

Raises:
    AttributeError: If no dataset with the given key is found, since the implementation accesses .name on None.

