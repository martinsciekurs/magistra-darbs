---
sidebar_position: 397
---

# load_search_prompt

**File:** `graphrag/utils/api.py` (lines 250-261)

## Signature

```python
def load_search_prompt(root_dir: str, prompt_config: str | None) -> str | None
```

## Description

Load the search prompt from disk if configured.

If not, leave it empty - the search functions will load their defaults.

Args:
    root_dir: Root directory path as a string where the prompt_config is resolved.
    prompt_config: Optional path to the prompt file, relative to root_dir. If provided, the function will attempt to load the file if it exists.

Returns:
    The contents of the prompt file decoded as UTF-8 if found, otherwise None.

Raises:
    OSError: If a filesystem error occurs while reading the prompt file.
    UnicodeDecodeError: If the prompt file contents cannot be decoded as UTF-8.

## Example 💡 Generated

```python
from module import load_search_prompt
root_dir = "/project"
map_path = "config/global/map_prompt.txt"
prompt_text = load_search_prompt(root_dir, map_path)
# returns the prompt text or None
local_path = "config/local_search/prompt.txt"
local_text = load_search_prompt(root_dir, local_path)
# holds the prompt text or None
```

## Called By

This function is called by:

- `graphrag/api/query.py::global_search_streaming`
- `graphrag/api/query.py::local_search_streaming`
- `graphrag/api/query.py::drift_search_streaming`
- `graphrag/api/query.py::basic_search_streaming`

