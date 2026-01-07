---
sidebar_position: 178
---

# get_delta_docs

**File:** `graphrag/index/update/incremental_index.py` (lines 34-63)

## Signature

```python
def get_delta_docs(
    input_dataset: pd.DataFrame, storage: PipelineStorage
) -> InputDelta
```

## Description

Compute the delta between the input dataset and the final documents stored in the pipeline storage.

This asynchronous function compares the input_dataset against the documents currently stored in storage and returns the delta as an InputDelta with new_inputs and deleted_inputs.

Notes
    - new_inputs corresponds to documents in input_dataset whose titles are not present in the stored final documents.
    - deleted_inputs corresponds to documents present in the stored final documents but not present in input_dataset.

Parameters
    input_dataset (pd.DataFrame): The input dataset containing documents to be indexed.
    storage (PipelineStorage): The Pipeline storage where final documents are stored.

Returns
    InputDelta
        The input delta containing:
        new_inputs (pd.DataFrame): The new documents to add (rows from input_dataset not present in storage).
        deleted_inputs (pd.DataFrame): The documents to remove (rows from storage not present in input_dataset).

Raises
    Exception
        Exceptions raised by the storage backend or parquet reader during the load operation.

## Dependencies

This function calls:

- `graphrag/utils/storage.py::load_table_from_storage`

## Called By

This function is called by:

- `graphrag/index/workflows/load_update_documents.py::load_update_documents`

