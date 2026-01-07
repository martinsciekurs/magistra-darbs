---
sidebar_position: 456
---

# test_notebook

**File:** `tests/notebook/test_notebooks.py` (lines 47-48)

## Signature

```python
def test_notebook(notebook_path: Path)
```

## Description

Test that a notebook executes without errors.

Args:
    notebook_path: Path to the notebook file to test.

Returns:
    None

Raises:
    subprocess.CalledProcessError: If the nbconvert command fails to execute.

## Dependencies

This function calls:

- `tests/notebook/test_notebooks.py::_notebook_run`

