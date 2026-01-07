---
sidebar_position: 614
---

# load_local_prompt_config

**File:** `unified-search-app/app/knowledge_loader/data_sources/local_source.py` (lines 21-30)

## Signature

```python
def load_local_prompt_config(base_path="") -> dict[str, str]
```

## Description

Load local prompt configuration.

Args:
    base_path: Path to the folder containing prompt files.

Returns:
    dict[str, str]: Mapping from the prompt name (filename without extension) to the file contents as a string.

Raises:
    FileNotFoundError: If base_path does not exist.
    OSError: If an OS error occurs while listing or reading files.

