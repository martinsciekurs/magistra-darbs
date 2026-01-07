---
sidebar_position: 580
---

# run_workflow_2

**File:** `tests/verbs/test_pipeline_state.py` (lines 22-26)

## Signature

```python
def run_workflow_2(  # noqa: RUF029
    _config: GraphRagConfig, context: PipelineRunContext
)
```

## Description

Async function that increments the pipeline state's count by one.

Args:
    _config: GraphRagConfig - Configuration for Graphrag configuration
    context: PipelineRunContext - The PipelineRunContext for the current run; its state is updated by this function

Returns:
    WorkflowFunctionOutput: The function output; the result is None in this implementation.

Raises:
    KeyError: If 'count' is not present in context.state when attempting to increment.

## Dependencies

This function calls:

- `graphrag/index/typing/workflow.py::WorkflowFunctionOutput`

