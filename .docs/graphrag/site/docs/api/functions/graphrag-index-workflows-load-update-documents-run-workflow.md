---
sidebar_position: 255
---

# run_workflow

**File:** `graphrag/index/workflows/load_update_documents.py` (lines 22-42)

## Signature

```python
def run_workflow(
    config: GraphRagConfig,
    context: PipelineRunContext,
) -> WorkflowFunctionOutput
```

## Description

Run the update-document loading workflow: load update-only input documents, write them to storage, and return the result.

Args:
  config: GraphRagConfig containing input configuration and related settings.
  context: PipelineRunContext providing access to input_storage, output_storage, and runtime statistics.

Returns:
  WorkflowFunctionOutput: The output containing the loaded update documents as a DataFrame, or a stop signal if no update documents were found.

Raises:
  Exception: Exceptions raised by the input loading or storage backends may propagate.

## Dependencies

This function calls:

- `graphrag/index/typing/workflow.py::WorkflowFunctionOutput`
- `graphrag/index/workflows/load_update_documents.py::load_update_documents`
- `graphrag/utils/storage.py::write_table_to_storage`

