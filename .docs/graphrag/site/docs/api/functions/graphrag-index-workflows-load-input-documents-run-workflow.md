---
sidebar_position: 253
---

# run_workflow

**File:** `graphrag/index/workflows/load_input_documents.py` (lines 21-36)

## Signature

```python
def run_workflow(
    config: GraphRagConfig,
    context: PipelineRunContext,
) -> WorkflowFunctionOutput
```

## Description

Load input documents, write them to storage, and return the result as a WorkflowFunctionOutput.

Args:
    config: GraphRagConfig containing input configuration and related settings.
    context: PipelineRunContext providing access to input_storage, output_storage, and runtime statistics.

Returns:
    WorkflowFunctionOutput: The output containing the loaded input documents as a pandas DataFrame in the result field.

Raises:
    Exception: Exceptions raised by the storage backend during the write operation may propagate.

## Dependencies

This function calls:

- `graphrag/index/typing/workflow.py::WorkflowFunctionOutput`
- `graphrag/index/workflows/load_input_documents.py::load_input_documents`
- `graphrag/utils/storage.py::write_table_to_storage`

