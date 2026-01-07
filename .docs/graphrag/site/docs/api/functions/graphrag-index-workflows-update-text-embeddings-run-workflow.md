---
sidebar_position: 269
---

# run_workflow

**File:** `graphrag/index/workflows/update_text_embeddings.py` (lines 19-59)

## Signature

```python
def run_workflow(
    config: GraphRagConfig,
    context: PipelineRunContext,
) -> WorkflowFunctionOutput
```

## Description

Update the text embeddings from an incremental index run.

Args:
  config: GraphRagConfig containing configuration for embedding and storage behavior.
  context: PipelineRunContext carrying the state for the run, including update_timestamp and incremental update data. The function reads the following keys from context.state: 'update_timestamp', 'incremental_update_final_documents', 'incremental_update_merged_relationships', 'incremental_update_merged_text_units', 'incremental_update_merged_entities', and 'incremental_update_merged_community_reports'. It also uses context.callbacks and context.cache.

Returns:
  WorkflowFunctionOutput: A WorkflowFunctionOutput with result=None.

Raises:
  KeyError: If required keys are missing from context.state (for example, update_timestamp or any incremental_update_* keys).

Notes:
  The function calls get_update_storages(config, context.state['update_timestamp']) to obtain storage backends, and then generate_text_embeddings with the incremental update data to produce embeddings.
  If config.snapshots.embeddings is True, the resulting embedding tables are written to storage using write_table_to_storage with names embeddings.&lt;name&gt;.

State requirements:
  context.state must include:
    update_timestamp (str)
    incremental_update_final_documents
    incremental_update_merged_relationships
    incremental_update_merged_text_units
    incremental_update_merged_entities
    incremental_update_merged_community_reports

## Dependencies

This function calls:

- `graphrag/config/get_embedding_settings.py::get_embedding_settings`
- `graphrag/index/run/utils.py::get_update_storages`
- `graphrag/index/typing/workflow.py::WorkflowFunctionOutput`
- `graphrag/index/workflows/generate_text_embeddings.py::generate_text_embeddings`
- `graphrag/utils/storage.py::write_table_to_storage`

