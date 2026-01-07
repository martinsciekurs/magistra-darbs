---
sidebar_position: 264
---

# _update_covariates

**File:** `graphrag/index/workflows/update_covariates.py` (lines 45-55)

## Signature

```python
def _update_covariates(
    previous_storage: PipelineStorage,
    delta_storage: PipelineStorage,
    output_storage: PipelineStorage,
) -> None
```

## Description

Update the covariates output by merging existing covariates with the delta covariates and writing the result to storage.

Args:
    previous_storage: The storage containing the previous covariates.
    delta_storage: The storage containing the delta covariates to apply.
    output_storage: The storage to write the merged covariates to.

Returns:
    None

Raises:
    ValueError: Could not find covariates.parquet in storage!
    Exception: Exceptions raised by the storage backend or parquet reader during load or write operations.

## Dependencies

This function calls:

- `graphrag/index/workflows/update_covariates.py::_merge_covariates`
- `graphrag/utils/storage.py::load_table_from_storage`
- `graphrag/utils/storage.py::write_table_to_storage`

## Called By

This function is called by:

- `graphrag/index/workflows/update_covariates.py::run_workflow`

