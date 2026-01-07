---
sidebar_position: 238
---

# run_workflow

**File:** `graphrag/index/workflows/create_final_text_units.py` (lines 23-52)

## Signature

```python
def run_workflow(
    config: GraphRagConfig,
    context: PipelineRunContext,
) -> WorkflowFunctionOutput
```

## Description

Run the final text units transformation workflow by loading input tables from storage, constructing final text units using entities, relationships, and optional covariates, and writing the output back to storage.

Args:
  config (GraphRagConfig): GraphRag configuration for the workflow
  context (PipelineRunContext): Pipeline run context containing the output storage used for load/write operations

Returns:
  WorkflowFunctionOutput: The output object containing the final text units DataFrame in its result attribute

Raises:
  Exception: Exceptions raised by storage backends during load or write operations may propagate.

## Dependencies

This function calls:

- `graphrag/index/typing/workflow.py::WorkflowFunctionOutput`
- `graphrag/index/workflows/create_final_text_units.py::create_final_text_units`
- `graphrag/utils/storage.py::load_table_from_storage`
- `graphrag/utils/storage.py::storage_has_table`
- `graphrag/utils/storage.py::write_table_to_storage`

## Called By

This function is called by:

- `tests/verbs/test_create_final_text_units.py::test_create_final_text_units`

