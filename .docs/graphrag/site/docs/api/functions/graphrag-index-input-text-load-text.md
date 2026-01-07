---
sidebar_position: 57
---

# load_text

**File:** `graphrag/index/input/text.py` (lines 19-35)

## Signature

```python
def load_text(
    config: InputConfig,
    storage: PipelineStorage,
) -> pd.DataFrame
```

## Description

Load text inputs from a directory.

Args:
    config: InputConfig
        Configuration for the text input, including encoding and storage settings.
    storage: PipelineStorage
        Storage backend used to retrieve text files and metadata.

Returns:
    pd.DataFrame
        Concatenated DataFrame containing the data from loaded text files with any
        additional processing applied.

Raises:
    None
        The per-file loading failures are logged and skipped by the internal loader
        (load_files) rather than raised to the caller.

## Dependencies

This function calls:

- `graphrag/index/input/util.py::load_files`

