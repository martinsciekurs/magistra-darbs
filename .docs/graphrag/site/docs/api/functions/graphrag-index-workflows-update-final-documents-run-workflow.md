---
sidebar_position: 268
---

# run_workflow

**File:** `graphrag/index/workflows/update_final_documents.py` (lines 17-34)

## Signature

```python
def run_workflow(
    config: GraphRagConfig,
    context: PipelineRunContext,
) -> WorkflowFunctionOutput
```

## Description

Update the final documents from an incremental index run.

Args:
    config: GraphRagConfig
        GraphRagConfig containing configuration for the workflow.

    context: PipelineRunContext
        PipelineRunContext carrying the state for the run.

Returns:
    WorkflowFunctionOutput
        A WorkflowFunctionOutput with result=None.

Raises:
    KeyError
        If 'update_timestamp' is not present in context.state.

Side effects:
    Updates context.state['incremental_update_final_documents'] with the final
    documents dataframe produced by concatenating previous and delta
    documents into the output storage.

## Dependencies

This function calls:

- `graphrag/index/run/utils.py::get_update_storages`
- `graphrag/index/typing/workflow.py::WorkflowFunctionOutput`
- `graphrag/index/update/incremental_index.py::concat_dataframes`

