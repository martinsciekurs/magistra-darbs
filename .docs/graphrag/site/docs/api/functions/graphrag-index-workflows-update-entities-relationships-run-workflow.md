---
sidebar_position: 267
---

# run_workflow

**File:** `graphrag/index/workflows/update_entities_relationships.py` (lines 25-53)

## Signature

```python
def run_workflow(
    config: GraphRagConfig,
    context: PipelineRunContext,
) -> WorkflowFunctionOutput
```

## Description

Update the entities and relationships from a incremental index run.

Args:
    config: GraphRagConfig
        GraphRagConfig containing configuration for the workflow.
    context: PipelineRunContext
        PipelineRunContext carrying the state for the run, including update_timestamp.

Returns:
    WorkflowFunctionOutput
        The output of the workflow function.

Raises:
    KeyError
        If 'update_timestamp' is not present in context.state.

## Dependencies

This function calls:

- `graphrag/index/run/utils.py::get_update_storages`
- `graphrag/index/typing/workflow.py::WorkflowFunctionOutput`
- `graphrag/index/workflows/update_entities_relationships.py::_update_entities_and_relationships`

