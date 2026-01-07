---
sidebar_position: 24
---

# path_autocomplete

**File:** `graphrag/cli/main.py` (lines 30-76)

## Signature

```python
def path_autocomplete(
    file_okay: bool = True,
    dir_okay: bool = True,
    readable: bool = True,
    writable: bool = False,
    match_wildcard: str | None = None,
) -> Callable[[str], list[str]]
```

## Description

Autocomplete file and directory paths.

Args:
    file_okay: bool
        If True, include files in the completions; otherwise, exclude files.
    dir_okay: bool
        If True, include directories in the completions; otherwise, exclude directories.
    readable: bool
        If True, include only items that are readable (os.R_OK).
    writable: bool
        If True, include only items that are writable (os.W_OK).
    match_wildcard: str | None
        Optional wildcard pattern to filter items; supports '?' and '*' characters.

Returns:
    Callable[[str], list[str]]
        A function that takes the current incomplete string and returns a list of matching item names.

Raises:
    OSError
        If an I/O error occurs during directory listing or permission checks.

