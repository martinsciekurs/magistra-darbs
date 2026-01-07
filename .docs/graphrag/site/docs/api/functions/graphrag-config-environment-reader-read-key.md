---
sidebar_position: 41
---

# read_key

**File:** `graphrag/config/environment_reader.py` (lines 19-23)

## Signature

```python
def read_key(value: KeyValue) -> str
```

## Description

Read a key value and normalize it to lowercase string.

Args:
    value: KeyValue
        The key to normalize. It can be a string or an Enum. If value is a string, the result is the string converted to lowercase. If value is an Enum, the Enum.value attribute is used and lowercased. The Enum.value is assumed to be a string; otherwise a runtime error may occur.

Returns:
    str
        The lowercase representation of the key.

Raises:
    AttributeError
        If value is not a string and does not have a value attribute, or if value.value is not a string or cannot call lower().

## Called By

This function is called by:

- `graphrag/config/environment_reader.py::EnvironmentReader.envvar_prefix`
- `graphrag/config/environment_reader.py::EnvironmentReader.str`
- `graphrag/config/environment_reader.py::EnvironmentReader.int`
- `graphrag/config/environment_reader.py::EnvironmentReader.bool`
- `graphrag/config/environment_reader.py::EnvironmentReader.float`
- `graphrag/config/environment_reader.py::EnvironmentReader.list`

