---
sidebar_position: 613
---

# load_prompts

**File:** `unified-search-app/app/knowledge_loader/data_sources/loader.py` (lines 72-78)

## Signature

```python
def load_prompts(dataset: str) -> dict[str, str]
```

## Description

Return the prompts configuration for a specific dataset.

If a blob account name is configured, the prompts are loaded from blob storage; otherwise
they are loaded from local storage.

Args:
    dataset (str): The dataset name to load prompts for.

Returns:
    dict[str, str]: The prompts configuration for the specified dataset.

Raises:
    Exception: Propagated exceptions from underlying loading functions (load_blob_prompt_config
        or load_local_prompt_config) may be raised.

## Dependencies

This function calls:

- `unified-search-app/app/knowledge_loader/data_sources/loader.py::_get_base_path`

