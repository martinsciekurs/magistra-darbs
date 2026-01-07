---
sidebar_position: 257
---

# run_workflow

**File:** `graphrag/index/workflows/prune_graph.py` (lines 22-50)

## Signature

```python
def run_workflow(
    config: GraphRagConfig,
    context: PipelineRunContext,
) -> WorkflowFunctionOutput
```

## Description

Executes the prune-graph workflow in three steps: load entities and relationships from storage, prune using the provided pruning configuration, and write the pruned entities and relationships back to storage. Returns the pruned data as part of the WorkflowFunctionOutput.

Args:
  config (GraphRagConfig): Configuration for pruning, including parameters exposed under prune_graph to control pruning behavior.
  context (PipelineRunContext): Execution context containing the storage backend and runtime information used for reading and writing tables.

Returns:
  WorkflowFunctionOutput: Output with a result dictionary containing:
  - "entities": pruned entities DataFrame
  - "relationships": pruned relationships DataFrame

Raises:
  ValueError: If required input tables (entities or relationships) are not found in storage.
  Exception: Exceptions raised by the storage backend during load or write operations may propagate.

## Dependencies

This function calls:

- `graphrag/index/operations/prune_graph.py::prune_graph`
- `graphrag/index/typing/workflow.py::WorkflowFunctionOutput`
- `graphrag/utils/storage.py::load_table_from_storage`
- `graphrag/utils/storage.py::write_table_to_storage`

## Called By

This function is called by:

- `tests/verbs/test_prune_graph.py::test_prune_graph`

