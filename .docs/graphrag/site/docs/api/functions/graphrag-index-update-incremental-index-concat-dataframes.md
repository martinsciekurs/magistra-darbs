---
sidebar_position: 179
---

# concat_dataframes

**File:** `graphrag/index/update/incremental_index.py` (lines 66-83)

## Signature

```python
def concat_dataframes(
    name: str,
    previous_storage: PipelineStorage,
    delta_storage: PipelineStorage,
    output_storage: PipelineStorage,
) -> pd.DataFrame
```

## Description

Concatenate dataframes.

Concatenate old and delta documents: load from previous_storage and delta_storage, append delta to old after assigning sequential human_readable_id values to delta rows, and write the final dataframe to output_storage.

Parameters
name: str
    Base name for the parquet file to load and to which the final dataframe will be written as &#123;name&#125;.parquet.
previous_storage: PipelineStorage
    Storage backend containing the existing (old) documents.
delta_storage: PipelineStorage
    Storage backend containing the delta (new) documents.
output_storage: PipelineStorage
    Storage backend where the final concatenated dataframe will be written.

Returns
pd.DataFrame
    The concatenated DataFrame containing old and delta documents.

Raises
ValueError
    Could not find &#123;name&#125;.parquet in storage!
Exception
    Exceptions raised by the storage backend or parquet reader during the load or write operations may propagate.

## Dependencies

This function calls:

- `graphrag/utils/storage.py::load_table_from_storage`
- `graphrag/utils/storage.py::write_table_to_storage`

## Called By

This function is called by:

- `graphrag/index/workflows/update_final_documents.py::run_workflow`

