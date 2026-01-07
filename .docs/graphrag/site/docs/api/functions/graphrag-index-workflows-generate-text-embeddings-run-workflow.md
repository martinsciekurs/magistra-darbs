---
sidebar_position: 251
---

# run_workflow

**File:** `graphrag/index/workflows/generate_text_embeddings.py` (lines 35-93)

## Signature

```python
def run_workflow(
    config: GraphRagConfig,
    context: PipelineRunContext,
) -> WorkflowFunctionOutput
```

## Description

Generates text embeddings for the configured fields and returns the results. This workflow loads input data conditionally based on the configured embed_text fields, invokes the embedding generation, and optionally persists the resulting embeddings as snapshots to storage.

Args:
  config: GraphRagConfig
      GraphRagConfig containing embed_text and snapshot settings used by the workflow.
  context: PipelineRunContext
      PipelineRunContext providing output_storage, callbacks, and cache.

Returns:
  WorkflowFunctionOutput
      The workflow result containing generated embeddings as a mapping from embedding name to DataFrame.

Raises:
  ValueError
      Could not find &#123;name&#125;.parquet in storage!
  Exception
      Exceptions raised by the storage backend or parquet reader during the load operation, or by the storage backend during the write operation when snapshots are enabled.

## Dependencies

This function calls:

- `graphrag/config/get_embedding_settings.py::get_embedding_settings`
- `graphrag/index/typing/workflow.py::WorkflowFunctionOutput`
- `graphrag/index/workflows/generate_text_embeddings.py::generate_text_embeddings`
- `graphrag/utils/storage.py::load_table_from_storage`
- `graphrag/utils/storage.py::write_table_to_storage`

## Called By

This function is called by:

- `tests/verbs/test_generate_text_embeddings.py::test_generate_text_embeddings`

