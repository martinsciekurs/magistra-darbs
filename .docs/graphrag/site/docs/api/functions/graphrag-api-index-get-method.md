---
sidebar_position: 1
---

# _get_method

**File:** `graphrag/api/index.py` (lines 99-101)

## Signature

```python
def _get_method(method: IndexingMethod | str, is_update_run: bool) -> str
```

## Description

Return the method name to use for the indexing pipeline, optionally indicating an update run.

Args:
    method: IndexingMethod | str
        The indexing method. If an IndexingMethod is provided, its value is used; otherwise the string value is used directly.
    is_update_run: bool
        True if this is an update run, in which case the method name will be suffixed with "-update".

Returns:
    str: The computed method name, possibly suffixed with "-update" when is_update_run is True.

## Called By

This function is called by:

- `graphrag/api/index.py::build_index`

