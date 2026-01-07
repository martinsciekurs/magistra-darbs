---
sidebar_position: 22
---

# initialize_project_at

**File:** `graphrag/cli/initialize.py` (lines 37-95)

## Signature

```python
def initialize_project_at(path: Path, force: bool) -> None
```

## Description

Initialize the project at the given path.

Args:
    path: The path at which to initialize the project.
    force: Whether to force initialization even if the project already exists.

Returns:
    None

Raises:
    ValueError: If the project already exists and force is False.

## Called By

This function is called by:

- `graphrag/cli/main.py::_initialize_cli`

