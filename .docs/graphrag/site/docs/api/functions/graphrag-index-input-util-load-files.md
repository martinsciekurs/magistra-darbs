---
sidebar_position: 59
---

# load_files

**File:** `graphrag/index/input/util.py` (lines 19-53)

## Signature

```python
def load_files(
    loader: Any,
    config: InputConfig,
    storage: PipelineStorage,
) -> pd.DataFrame
```

## Description

Load files from storage asynchronously and apply a loader function, then concatenate the results into a single pandas DataFrame.

The loader is awaited for each file. Failures are logged and the corresponding file is skipped rather than raised.

Args:
    loader: Any
        Async loader callable that accepts (file, group) and returns a value compatible with pandas.concat.
        The loader will be awaited for each file. If it raises, the file is skipped with a warning.
    config: InputConfig
        Configuration for input files, including file_pattern, file_filter, and file_type/storage details used to locate files.
    storage: PipelineStorage
        Storage backend used to locate and read files.

Returns:
    pd.DataFrame
        A DataFrame formed by concatenating all successfully loaded data.

Raises:
    ValueError
        If no files matching the pattern are found in the configured storage location.

Notes:
    - The final concatenation uses pd.concat on the list of successfully loaded objects. If none are loaded, pd.concat may raise a ValueError for no objects to concatenate. This edge case should be considered by callers.
    - The function logs the number of files found and the number successfully loaded.

## Called By

This function is called by:

- `graphrag/index/input/csv.py::load_csv`
- `graphrag/index/input/json.py::load_json`
- `graphrag/index/input/text.py::load_text`

