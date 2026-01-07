---
sidebar_position: 23
---

# wildcard_match

**File:** `graphrag/cli/main.py` (lines 39-41)

## Signature

```python
def wildcard_match(string: str, pattern: str) -> bool
```

## Description

Determine whether the entire string matches a wildcard pattern.
The pattern uses ? to match any single character and * to match any sequence of characters.

Args:
    string: The input string to test against the pattern.
    pattern: The wildcard pattern, where ? matches any single character and * matches any sequence of characters.

Returns:
    bool: True if the string matches the wildcard pattern, otherwise False.

Raises:
    TypeError: If string or pattern are not of type str.

## Called By

This function is called by:

- `graphrag/cli/main.py::completer`

