---
sidebar_position: 271
---

# _update_text_units

**File:** `graphrag/index/workflows/update_text_units.py` (lines 42-57)

## Signature

```python
def _update_text_units(
    previous_storage: PipelineStorage,
    delta_storage: PipelineStorage,
    output_storage: PipelineStorage,
    entity_id_mapping: dict,
) -> pd.DataFrame
```

## Description

Asynchronously update and merge text units from storage and write the result to the output storage.

Args:
    previous_storage: PipelineStorage
        The storage containing the old text units.
    delta_storage: PipelineStorage
        The storage containing the delta text units to apply.
    output_storage: PipelineStorage
        The storage where the merged text units will be written.
    entity_id_mapping: dict
        Mapping from old entity ids to new ids to apply to delta_text_units.

Returns:
    pd.DataFrame
        The updated text units.

Raises:
    ValueError
        Could not find text_units.parquet in storage.
    Exception
        Exceptions raised by the storage backend or parquet reader during the load or write operations.
    KeyError
        If required columns are missing from the input dataframes (e.g., 'entity_ids' or 'human_readable_id') during the update/merge process.

## Dependencies

This function calls:

- `graphrag/index/workflows/update_text_units.py::_update_and_merge_text_units`
- `graphrag/utils/storage.py::load_table_from_storage`
- `graphrag/utils/storage.py::write_table_to_storage`

## Called By

This function is called by:

- `graphrag/index/workflows/update_text_units.py::run_workflow`

