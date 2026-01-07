---
sidebar_position: 610
---

# _get_base_path

**File:** `unified-search-app/app/knowledge_loader/data_sources/loader.py` (lines 31-40)

## Signature

```python
def _get_base_path(
    dataset: str | None, root: str | None, extra_path: str | None = None
) -> str
```

## Description

Construct and return the base path for the given dataset and extra path.

Args:
    dataset (str | None): The dataset folder name, or None to omit.
    root (str | None): The root path segment, or None to omit.
    extra_path (str | None): Additional path segments separated by '/' (if provided).

Returns:
    str: The constructed base path as a string.

## Called By

This function is called by:

- `unified-search-app/app/knowledge_loader/data_sources/loader.py::create_datasource`
- `unified-search-app/app/knowledge_loader/data_sources/loader.py::load_dataset_listing`
- `unified-search-app/app/knowledge_loader/data_sources/loader.py::load_prompts`

