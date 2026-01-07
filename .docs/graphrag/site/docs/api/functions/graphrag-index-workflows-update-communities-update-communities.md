---
sidebar_position: 259
---

# _update_communities

**File:** `graphrag/index/workflows/update_communities.py` (lines 39-53)

## Signature

```python
def _update_communities(
    previous_storage: PipelineStorage,
    delta_storage: PipelineStorage,
    output_storage: PipelineStorage,
) -> dict
```

## Description

Update the communities output.

Args:
  previous_storage: PipelineStorage
      Storage containing the existing/previous communities.
  delta_storage: PipelineStorage
      Storage containing the delta (updated) communities.
  output_storage: PipelineStorage
      Storage to write the merged communities to.

Returns:
  dict
      Mapping from original delta community IDs to the new IDs assigned during the merge.

Raises:
  ValueError
      Could not find &#123;name&#125;.parquet in storage!
  Exception
      Exceptions raised by the storage backend or parquet reader during the load operation.
  Exception
      Exceptions raised by the storage backend during the write operation may propagate.

## Dependencies

This function calls:

- `graphrag/index/update/communities.py::_update_and_merge_communities`
- `graphrag/utils/storage.py::load_table_from_storage`
- `graphrag/utils/storage.py::write_table_to_storage`

## Called By

This function is called by:

- `graphrag/index/workflows/update_communities.py::run_workflow`

