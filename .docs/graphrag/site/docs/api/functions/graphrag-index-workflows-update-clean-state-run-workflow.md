---
sidebar_position: 258
---

# run_workflow

**File:** `graphrag/index/workflows/update_clean_state.py` (lines 15-31)

## Signature

```python
def run_workflow(  # noqa: RUF029
    _config: GraphRagConfig,
    context: PipelineRunContext,
) -> WorkflowFunctionOutput
```

## Description

Clean the state after the update.

Args:
    _config (GraphRagConfig): GraphRag configuration.
    context (PipelineRunContext): Runtime context for the workflow execution.

Returns:
    WorkflowFunctionOutput: Output object for the workflow function; result is None.

## Dependencies

This function calls:

- `graphrag/index/typing/workflow.py::WorkflowFunctionOutput`

