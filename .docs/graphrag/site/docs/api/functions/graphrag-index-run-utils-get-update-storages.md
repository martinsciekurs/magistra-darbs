---
sidebar_position: 171
---

# get_update_storages

**File:** `graphrag/index/run/utils.py` (lines 51-61)

## Signature

```python
def get_update_storages(
    config: GraphRagConfig, timestamp: str
) -> tuple[PipelineStorage, PipelineStorage, PipelineStorage]
```

## Description

Get storage objects for the update index run.

The function creates storage objects from the provided config:
- output_storage: created from config.output
- update_storage: created from config.update_index_output
- timestamped_storage: derived by applying the given timestamp to update_storage
- delta_storage: timestamped_storage.child("delta")
- previous_storage: timestamped_storage.child("previous")

Returns:
    tuple[PipelineStorage, PipelineStorage, PipelineStorage]: A tuple containing
    output_storage, previous_storage, delta_storage respectively.

Args:
    config: GraphRagConfig The configuration containing storage settings to use for output and update index outputs.
    timestamp: str The timestamp used to namespace the update index storage.

Raises:
    ValueError: If the storage type is not registered when creating a storage from config.

## Dependencies

This function calls:

- `graphrag/utils/api.py::create_storage_from_config`

## Called By

This function is called by:

- `graphrag/index/workflows/update_communities.py::run_workflow`
- `graphrag/index/workflows/update_community_reports.py::run_workflow`
- `graphrag/index/workflows/update_covariates.py::run_workflow`
- `graphrag/index/workflows/update_entities_relationships.py::run_workflow`
- `graphrag/index/workflows/update_final_documents.py::run_workflow`
- `graphrag/index/workflows/update_text_embeddings.py::run_workflow`
- `graphrag/index/workflows/update_text_units.py::run_workflow`

