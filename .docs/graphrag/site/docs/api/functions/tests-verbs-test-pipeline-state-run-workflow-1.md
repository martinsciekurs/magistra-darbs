---
sidebar_position: 579
---

# run_workflow_1

**File:** `tests/verbs/test_pipeline_state.py` (lines 15-19)

## Signature

```python
def run_workflow_1(  # noqa: RUF029
    _config: GraphRagConfig, context: PipelineRunContext
)
```

## Description

Async function that initializes the pipeline state by setting context.state["count"] to 1 and returns a WorkflowFunctionOutput with result=None.

Args:
    _config: Configuration for Graphrag configuration
    context: The PipelineRunContext for the current run; its state is updated by this function

Returns:
    WorkflowFunctionOutput: The function output; the result is None in this implementation

## Dependencies

This function calls:

- `graphrag/index/typing/workflow.py::WorkflowFunctionOutput`

