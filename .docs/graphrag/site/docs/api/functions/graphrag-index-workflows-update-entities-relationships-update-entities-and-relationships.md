---
sidebar_position: 266
---

# _update_entities_and_relationships

**File:** `graphrag/index/workflows/update_entities_relationships.py` (lines 56-106)

## Signature

```python
def _update_entities_and_relationships(
    previous_storage: PipelineStorage,
    delta_storage: PipelineStorage,
    output_storage: PipelineStorage,
    config: GraphRagConfig,
    cache: PipelineCache,
    callbacks: WorkflowCallbacks,
) -> tuple[pd.DataFrame, pd.DataFrame, dict]
```

## Description

Update Final Entities and Relationships output.

This function merges the existing (previous) entities with the delta of new/updated entities, updates and merges relationships, applies summarization to the merged entities and relationships, and writes the results to the provided output storage.

Parameters:
  previous_storage (PipelineStorage): The storage containing the previous state data.
  delta_storage (PipelineStorage): The storage containing delta (new/updated) data.
  output_storage (PipelineStorage): The storage to write updated entities and relationships to.
  config (GraphRagConfig): GraphRag configuration used for summarization and merging.
  cache (PipelineCache): Cache used by the summarization routine.
  callbacks (WorkflowCallbacks): Callbacks for progress reporting during the workflow.

Returns:
  tuple[pd.DataFrame, pd.DataFrame, dict]: The updated entities DataFrame, the updated relationships DataFrame, and the entity_id_mapping dictionary.

Raises:
  ValueError: If required data is missing from storage or a storage read error occurs.
  KeyError: If required columns are missing from the input DataFrames used by _update_and_merge_relationships.
  TypeError: If inputs to _update_and_merge_relationships are not pandas DataFrames.
  Exception: General exceptions raised by the storage backends during read/write operations or by the summarization step.

## Dependencies

This function calls:

- `graphrag/index/update/entities.py::_group_and_resolve_entities`
- `graphrag/index/update/relationships.py::_update_and_merge_relationships`
- `graphrag/index/workflows/extract_graph.py::get_summarized_entities_relationships`
- `graphrag/utils/storage.py::load_table_from_storage`
- `graphrag/utils/storage.py::write_table_to_storage`

## Called By

This function is called by:

- `graphrag/index/workflows/update_entities_relationships.py::run_workflow`

