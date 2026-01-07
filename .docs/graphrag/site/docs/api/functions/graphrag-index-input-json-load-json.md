---
sidebar_position: 55
---

# load_json

**File:** `graphrag/index/input/json.py` (lines 18-47)

## Signature

```python
def load_json(
    config: InputConfig,
    storage: PipelineStorage,
) -> pd.DataFrame
```

## Description

Load json inputs from a directory.

Args:
    config: InputConfig
        Configuration for the JSON input, including encoding and storage settings.
    storage: PipelineStorage
        Storage backend used to retrieve JSON files and metadata.

Returns:
    pd.DataFrame
        Concatenated DataFrame containing the data from loaded JSON files with any
        additional processing applied (including adding per-file group keys as columns
        and a creation_date column).

Raises:
    json.JSONDecodeError
        If a JSON payload cannot be decoded from the loaded text.

## Dependencies

This function calls:

- `graphrag/index/input/util.py::load_files`

