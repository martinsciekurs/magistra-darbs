---
sidebar_position: 405
---

# file_exist

**File:** `graphrag/utils/cli.py` (lines 11-16)

## Signature

```python
def file_exist(path)
```

## Description

Check that the given path points to an existing file.

Args:
    path (str): Path to the file to validate. May be a string or Path object.

Returns:
    str: The input path if the file exists.

Raises:
    argparse.ArgumentTypeError: If the file does not exist.

Notes:
    This check uses Path.is_file() to verify that the path refers to a regular file.

