---
sidebar_position: 254
---

# load_update_documents

**File:** `graphrag/index/workflows/load_update_documents.py` (lines 45-55)

## Signature

```python
def load_update_documents(
    config: InputConfig,
    input_storage: PipelineStorage,
    previous_storage: PipelineStorage,
) -> pd.DataFrame
```

## Description

Load and parse update-only input documents into a standard format.

This asynchronous function loads input documents using create_input(config, input_storage), computes the delta against previously stored documents using get_delta_docs(input_documents, previous_storage), and returns the new inputs as a DataFrame.

Args:
    config: InputConfig containing input configuration (such as file_type and metadata) and storage base_dir information.
    input_storage: PipelineStorage used to access the input data.
    previous_storage: PipelineStorage containing the previously stored final documents to diff against.

Returns:
    pandas.DataFrame: The new/update input documents as determined by the delta computation (delta_documents.new_inputs).

Raises:
    Exceptions raised by create_input and get_delta_docs as encountered.

## Dependencies

This function calls:

- `graphrag/index/input/factory.py::create_input`
- `graphrag/index/update/incremental_index.py::get_delta_docs`

## Called By

This function is called by:

- `graphrag/index/workflows/load_update_documents.py::run_workflow`

