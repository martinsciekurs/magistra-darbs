---
sidebar_position: 223
---

# run_workflow

**File:** `graphrag/index/workflows/create_communities.py` (lines 25-51)

## Signature

```python
def run_workflow(
    config: GraphRagConfig,
    context: PipelineRunContext,
) -> WorkflowFunctionOutput
```

## Description

Run the create_communities workflow to generate final communities from input entities and relationships.

Args:
  config: GraphRagConfig containing cluster_graph settings used by the workflow.
  context: PipelineRunContext providing storage context for input and output data.

Returns:
  WorkflowFunctionOutput: The workflow output which includes the resulting communities.

Raises:
  ValueError: Could not find the required parquet files in storage when loading inputs (entities or relationships).
  Exception: Exceptions raised by the storage backend or by downstream processing may propagate.

## Dependencies

This function calls:

- `graphrag/index/typing/workflow.py::WorkflowFunctionOutput`
- `graphrag/index/workflows/create_communities.py::create_communities`
- `graphrag/utils/storage.py::load_table_from_storage`
- `graphrag/utils/storage.py::write_table_to_storage`

## Called By

This function is called by:

- `tests/verbs/test_create_communities.py::test_create_communities`

