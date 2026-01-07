---
sidebar_position: 407
---

# redact_dict

**File:** `graphrag/utils/cli.py` (lines 31-51)

## Signature

```python
def redact_dict(config: dict) -> dict
```

## Description

Redact sensitive values in a dictionary.

Args:
    config (dict): The configuration dictionary to redact.

Returns:
    dict: A new dictionary with sensitive keys redacted. Keys in &#123;"api_key", "connection_string", "container_name", "organization"&#125; will have their values replaced with "==== REDACTED ====" when not None. Nested dictionaries and lists are processed recursively; non-dictionary/list values are preserved.

## Dependencies

This function calls:

- `graphrag/utils/cli.py::redact_dict`

## Called By

This function is called by:

- `graphrag/utils/cli.py::redact`
- `graphrag/utils/cli.py::redact_dict`

