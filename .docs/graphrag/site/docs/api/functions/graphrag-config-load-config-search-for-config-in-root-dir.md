---
sidebar_position: 46
---

# _search_for_config_in_root_dir

**File:** `graphrag/config/load_config.py` (lines 21-46)

## Signature

```python
def _search_for_config_in_root_dir(root: str | Path) -> Path | None
```

## Description

Resolve the config path from the given root directory.

Args:
    root: str | Path
        The path to the root directory containing the config file. Searches for a default config file (settings.&#123;yaml,yml,json&#125;).

Returns:
    Path | None: The Path to the config file if one exists in the root directory; otherwise None.

Raises:
    FileNotFoundError: If the provided root is not a directory.

## Called By

This function is called by:

- `graphrag/config/load_config.py::_get_config_path`

