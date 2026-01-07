---
sidebar_position: 52
---

# load_csv

**File:** `graphrag/index/input/csv.py` (lines 18-43)

## Signature

```python
def load_csv(
    config: InputConfig,
    storage: PipelineStorage,
) -> pd.DataFrame
```

## Description

Load csv inputs from a directory.

Parameters:
    config: InputConfig
        Configuration for the CSV input, including encoding and storage settings.
    storage: PipelineStorage
        Storage backend used to retrieve CSV files and metadata.

Returns:
    pd.DataFrame
        Concatenated DataFrame containing the data from loaded CSV files with any
        additional processing applied (data columns, and creation_date).

Raises:
    Exception
        Propagates exceptions from the underlying storage or pandas operations; per-file
        failures are logged and skipped by the loader used to load files.

## Dependencies

This function calls:

- `graphrag/index/input/util.py::load_files`

