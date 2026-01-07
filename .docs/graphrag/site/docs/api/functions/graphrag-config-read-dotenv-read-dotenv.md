---
sidebar_position: 51
---

# read_dotenv

**File:** `graphrag/config/read_dotenv.py` (lines 15-25)

## Signature

```python
def read_dotenv(root: str) -> None
```

## Description

Read a .env file in the given root path.

Loads environment variables from a .env file located at the specified root into the process environment (os.environ). Only variables that are not already defined in os.environ are set, so existing environment variables are preserved.

Side effects:
    - Mutates os.environ by adding new variables from the .env file without overwriting existing ones.

Logging:
    - Logs an info message when a .env file is found and loaded.
    - Logs an info message if no .env file is found at the given root.

Args:
    root: str
        Path to the root directory containing a .env file to load.

Returns:
    None
        This function does not return a value.

Notes:
    - If the .env file contains invalid lines or is unreadable, dotenv_values will skip invalid lines or
      otherwise perform its internal handling; this function does not perform additional error handling.

## Example 💡 Generated

```python
from module import read_dotenv
import os
os.environ.setdefault("EXIST","1")
root = "/workspace/app"
read_dotenv(root)  # loads .env, preserves existing vars
```

