---
sidebar_position: 252
---

# load_input_documents

**File:** `graphrag/index/workflows/load_input_documents.py` (lines 39-43)

## Signature

```python
def load_input_documents(
    config: InputConfig, storage: PipelineStorage
) -> pd.DataFrame
```

## Description

Load and parse input documents into a standard format.

Args:
    config: InputConfig containing input configuration (such as file_type and metadata) and storage base_dir information.
    storage: PipelineStorage used to access the input data.

Returns:
    pandas.DataFrame: The loaded input data as a DataFrame.

## Dependencies

This function calls:

- `graphrag/index/input/factory.py::create_input`

## Called By

This function is called by:

- `graphrag/index/workflows/load_input_documents.py::run_workflow`

