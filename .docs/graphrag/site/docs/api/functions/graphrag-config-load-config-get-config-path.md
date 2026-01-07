---
sidebar_position: 48
---

# _get_config_path

**File:** `graphrag/config/load_config.py` (lines 84-112)

## Signature

```python
def _get_config_path(root_dir: Path, config_filepath: Path | None) -> Path
```

## Description

Resolve and return the configuration file path.

Args:
    root_dir (Path): The root directory of the project to search when config_filepath is not provided.
    config_filepath (Path | None): The explicit path to the config file. If None, the config file will be searched for in root_dir.

Returns:
    Path: The resolved configuration file path.

Raises:
    FileNotFoundError: If the specified config file does not exist or if no configuration file can be found in the root directory.

## Dependencies

This function calls:

- `graphrag/config/load_config.py::_search_for_config_in_root_dir`

## Called By

This function is called by:

- `graphrag/config/load_config.py::load_config`

