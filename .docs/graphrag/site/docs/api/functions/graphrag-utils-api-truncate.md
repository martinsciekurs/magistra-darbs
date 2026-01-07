---
sidebar_position: 402
---

# truncate

**File:** `graphrag/utils/api.py` (lines 283-287)

## Signature

```python
def truncate(text: str, max_length: int) -> str
```

## Description

Truncate a string to a maximum length.

If the input text length is greater than max_length, return the first max_length characters followed by "...[truncated]". Otherwise, return the input text unchanged.

Args:
    text: str
        The text to truncate.
    max_length: int
        The maximum allowed length of the text.

Returns:
    str
        The possibly truncated string. If truncation occurred, the returned string ends with "...[truncated]".

Raises:
    TypeError: If text is not a string or max_length is not an integer.

## Called By

This function is called by:

- `graphrag/api/query.py::global_search`
- `graphrag/api/query.py::multi_index_global_search`
- `graphrag/api/query.py::local_search`
- `graphrag/api/query.py::multi_index_local_search`
- `graphrag/api/query.py::drift_search`
- `graphrag/api/query.py::multi_index_drift_search`
- `graphrag/api/query.py::basic_search`

