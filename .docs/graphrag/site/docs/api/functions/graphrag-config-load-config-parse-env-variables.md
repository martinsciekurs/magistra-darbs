---
sidebar_position: 47
---

# _parse_env_variables

**File:** `graphrag/config/load_config.py` (lines 49-67)

## Signature

```python
def _parse_env_variables(text: str) -> str
```

## Description

Parse environment variables in the configuration text.

Args:
    text: The configuration text.

Returns:
    The configuration text with environment variables parsed.

Raises:
    KeyError: If an environment variable is not found.

## Called By

This function is called by:

- `graphrag/config/load_config.py::load_config`

