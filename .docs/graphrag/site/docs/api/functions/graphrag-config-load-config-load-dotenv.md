---
sidebar_position: 43
---

# _load_dotenv

**File:** `graphrag/config/load_config.py` (lines 70-81)

## Signature

```python
def _load_dotenv(config_path: Path | str) -> None
```

## Description

Load the .env file if it exists in the same directory as the config file.

Args:
    config_path (Path | str): The path to the config file.

Returns:
    None

## Example 💡 Generated

```python
from module import _load_dotenv
from pathlib import Path
cfg = Path("/etc/app/config.yaml")
_load_dotenv(cfg)
# loads .env if present
```

## Called By

This function is called by:

- `graphrag/config/load_config.py::load_config`

