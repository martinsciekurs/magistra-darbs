---
sidebar_position: 262
---

# run_workflow

**File:** `graphrag/index/workflows/update_community_reports.py` (lines 21-42)

## Signature

```python
def run_workflow(
    config: GraphRagConfig,
    context: PipelineRunContext,
) -> WorkflowFunctionOutput
```

## Description

Update the community reports from a incremental index run.

Args:
    config: GraphRagConfig
        GraphRagConfig configuration for the workflow.
    context: PipelineRunContext
        PipelineRunContext carrying the state for the run, including update_timestamp and incremental_update_community_id_mapping.

Returns:
    WorkflowFunctionOutput
        The output of the workflow function. The result is None.

Raises:
    KeyError
        If 'update_timestamp' is not present in context.state.

## Dependencies

This function calls:

- `graphrag/index/run/utils.py::get_update_storages`
- `graphrag/index/typing/workflow.py::WorkflowFunctionOutput`
- `graphrag/index/workflows/update_community_reports.py::_update_community_reports`

