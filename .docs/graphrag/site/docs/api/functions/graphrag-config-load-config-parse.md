---
sidebar_position: 45
---

# _parse

**File:** `graphrag/config/load_config.py` (lines 132-143)

## Signature

```python
def _parse(file_extension: str, contents: str) -> dict[str, Any]
```

## Description

Parse configuration contents based on the file extension.

Parses YAML (.yaml/.yml) using yaml.safe_load and JSON (.json) using json.loads.

Args:
    file_extension: The file extension determining the parsing method (e.g., ".yaml", ".yml", ".json").
    contents: The raw string content of the configuration file to parse.

Returns:
    Any: The parsed configuration. Typically a dict[str, Any], but the result can be None (for empty content) or other JSON/YAML types depending on the input.

Raises:
    ValueError: If the file extension is not supported.
    yaml.YAMLError: If YAML parsing fails.
    json.JSONDecodeError: If JSON parsing fails.

## Called By

This function is called by:

- `graphrag/config/load_config.py::load_config`

