---
sidebar_position: 44
---

# _apply_overrides

**File:** `graphrag/config/load_config.py` (lines 115-129)

## Signature

```python
def _apply_overrides(data: dict[str, Any], overrides: dict[str, Any]) -> None
```

## Description

Apply the overrides to the raw configuration.

Args:
    data: dict[str, Any]
        The raw configuration dictionary to be updated in place.
    overrides: dict[str, Any]
        A flat mapping of dot-separated keys to values to override in the configuration.

Returns:
    None

Raises:
    TypeError
        If attempting to override a non-dict value along the path.

## Called By

This function is called by:

- `graphrag/config/load_config.py::load_config`

