---
sidebar_position: 272
---

# run_workflow

**File:** `graphrag/index/workflows/update_text_units.py` (lines 21-39)

## Signature

```python
def run_workflow(
    config: GraphRagConfig,
    context: PipelineRunContext,
) -> WorkflowFunctionOutput
```

## Description

Update the text units from a incremental index run.

Args:
    config: GraphRagConfig containing configuration for the workflow.
    context: PipelineRunContext carrying the state for the run.

Returns:
    WorkflowFunctionOutput: A WorkflowFunctionOutput with result=None.

Raises:
    KeyError: If 'update_timestamp' is not present in context.state.

## Dependencies

This function calls:

- `graphrag/index/run/utils.py::get_update_storages`
- `graphrag/index/typing/workflow.py::WorkflowFunctionOutput`
- `graphrag/index/workflows/update_text_units.py::_update_text_units`

