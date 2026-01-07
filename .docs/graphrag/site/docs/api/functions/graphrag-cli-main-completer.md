---
sidebar_position: 25
---

# completer

**File:** `graphrag/cli/main.py` (lines 45-74)

## Signature

```python
def completer(incomplete: str) -> list[str]
```

## Description

Return a list of possible completions for the given incomplete input from the current directory.

Args:
    incomplete: str
        The partial string to match against directory item names in the current directory.

Returns:
    list[str]
        A list of completion strings that start with the provided incomplete string, after applying
        filtering based on external configuration (file_okay, dir_okay, readable, writable) and
        optional wildcard matching.

Raises:
    TypeError
        If the underlying wildcard matching function is invoked with non-string arguments.

## Dependencies

This function calls:

- `graphrag/cli/main.py::wildcard_match`

