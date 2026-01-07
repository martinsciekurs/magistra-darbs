---
sidebar_position: 406
---

# redact

**File:** `graphrag/utils/cli.py` (lines 27-54)

## Signature

```python
def redact(config: dict) -> str
```

## Description

Sanitize secrets in a configuration object by redacting sensitive fields.

This function traverses the input configuration and redacts values for keys identified as sensitive. The redaction keys are currently hard-coded as api_key, connection_string, container_name, and organization. If a sensitive key's value is None, that key is omitted from the resulting JSON instead of being redacted. The function recursively processes nested dictionaries and lists. The set of sensitive keys is hard-coded but designed to be extendable.

Returns:
    str: A JSON-formatted string with sensitive values replaced by "==== REDACTED ====" and with None-valued sensitive keys omitted.

Raises:
    TypeError: If the resulting object cannot be serialized to JSON (for example, when non-serializable values are present in the input).

Notes:
    json.dumps is used for serialization; non-serializable input values will trigger a TypeError. To customize redaction behavior, modify the sensitive-keys set or implement a separate configuration mechanism.

## Dependencies

This function calls:

- `graphrag/utils/cli.py::redact_dict`

## Called By

This function is called by:

- `graphrag/api/query.py::local_search_streaming`
- `graphrag/api/query.py::drift_search_streaming`
- `graphrag/api/query.py::basic_search_streaming`
- `graphrag/cli/index.py::_run_index`
- `graphrag/cli/prompt_tune.py::prompt_tune`

