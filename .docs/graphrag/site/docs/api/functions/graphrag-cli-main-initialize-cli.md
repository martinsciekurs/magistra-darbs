---
sidebar_position: 26
---

# _initialize_cli

**File:** `graphrag/cli/main.py` (lines 95-116)

## Signature

```python
def _initialize_cli(
    root: Path = typer.Option(
        Path(),
        "--root",
        "-r",
        help="The project root directory.",
        dir_okay=True,
        writable=True,
        resolve_path=True,
        autocompletion=ROOT_AUTOCOMPLETE,
    ),
    force: bool = typer.Option(
        False,
        "--force",
        "-f",
        help="Force initialization even if the project already exists.",
    ),
) -> None
```

## Description

Generate a default configuration file.

Args:
    root (Path): The project root directory.
    force (bool): Force initialization even if the project already exists.

Returns:
    None: This function does not return a value.

Raises:
    ValueError: If the project already exists and force is False.

## Dependencies

This function calls:

- `graphrag/cli/initialize.py::initialize_project_at`

