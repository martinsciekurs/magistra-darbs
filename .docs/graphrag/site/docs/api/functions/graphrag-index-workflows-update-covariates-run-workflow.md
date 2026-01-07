---
sidebar_position: 265
---

# run_workflow

**File:** `graphrag/index/workflows/update_covariates.py` (lines 25-42)

## Signature

```python
def run_workflow(
    config: GraphRagConfig,
    context: PipelineRunContext,
) -> WorkflowFunctionOutput
```

## Description

Update the covariates from a incremental index run.

Args:
    config: GraphRagConfig configuration for the workflow.
    context: PipelineRunContext containing state for the run, including update_timestamp.

Returns:
    WorkflowFunctionOutput: The output of the workflow function. The result is None.

Raises:
    Exception: Propagates exceptions raised by storage backends or related IO operations.

## Dependencies

This function calls:

- `graphrag/index/run/utils.py::get_update_storages`
- `graphrag/index/typing/workflow.py::WorkflowFunctionOutput`
- `graphrag/index/workflows/update_covariates.py::_update_covariates`
- `graphrag/utils/storage.py::storage_has_table`

