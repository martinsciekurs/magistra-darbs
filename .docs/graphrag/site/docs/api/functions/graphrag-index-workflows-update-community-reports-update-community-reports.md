---
sidebar_position: 261
---

# _update_community_reports

**File:** `graphrag/index/workflows/update_community_reports.py` (lines 45-66)

## Signature

```python
def _update_community_reports(
    previous_storage: PipelineStorage,
    delta_storage: PipelineStorage,
    output_storage: PipelineStorage,
    community_id_mapping: dict,
) -> pd.DataFrame
```

## Description

Update the community reports output by merging old and delta reports and writing the result to storage.

Args:
    previous_storage: PipelineStorage
        Storage containing the existing/previous community reports.
    delta_storage: PipelineStorage
        Storage containing the delta (updated) community reports.
    output_storage: PipelineStorage
        Storage to write the merged community reports to.
    community_id_mapping: dict
        Mapping from original delta community IDs to final IDs.

Returns:
    pd.DataFrame
        The updated community reports aligned to COMMUNITY_REPORTS_FINAL_COLUMNS.

Raises:
    ValueError
        Could not find community_reports.parquet in storage.
    Exception
        Exceptions raised by the storage backend or parquet reader during the load operation.
    Exception
        Exceptions raised by the storage backend during the write operation may propagate.
    KeyError
        If required columns such as 'community' or 'parent' are missing from the input data when merging.

## Dependencies

This function calls:

- `graphrag/index/update/communities.py::_update_and_merge_community_reports`
- `graphrag/utils/storage.py::load_table_from_storage`
- `graphrag/utils/storage.py::write_table_to_storage`

## Called By

This function is called by:

- `graphrag/index/workflows/update_community_reports.py::run_workflow`

