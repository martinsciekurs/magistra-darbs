---
sidebar_position: 260
---

# run_workflow

**File:** `graphrag/index/workflows/update_communities.py` (lines 19-36)

## Signature

```python
def run_workflow(
    config: GraphRagConfig,
    context: PipelineRunContext,
) -> WorkflowFunctionOutput
```

## Description

Update the communities from an incremental index run.

Args:
    config (GraphRagConfig): GraphRagConfig configuration for the workflow.
    context (PipelineRunContext): PipelineRunContext carrying the state for the run, including update_timestamp.

Returns:
    WorkflowFunctionOutput: The output of the workflow function. The result is None.

Notes:
    During execution, context.state["incremental_update_community_id_mapping"] is set to the
    mapping produced by updating and merging the communities.

Raises:
    Exception: Propagates exceptions raised by storage backends or related IO operations (e.g.,
        storage IO errors, network issues, or data serialization problems).

## Dependencies

This function calls:

- `graphrag/index/run/utils.py::get_update_storages`
- `graphrag/index/typing/workflow.py::WorkflowFunctionOutput`
- `graphrag/index/workflows/update_communities.py::_update_communities`

