---
sidebar_position: 455
---

# _notebook_run

**File:** `tests/notebook/test_notebooks.py` (lines 19-43)

## Signature

```python
def _notebook_run(filepath: Path)
```

## Description

Execute a notebook via nbconvert and collect error outputs.

Args:
- filepath: Path to the notebook file to execute.

Returns:
- list: A list of error outputs collected from the executed notebook cells.

Raises:
- subprocess.CalledProcessError: If the nbconvert command fails to execute.

## Called By

This function is called by:

- `tests/notebook/test_notebooks.py::test_notebook`

