---
sidebar_position: 232
---

# run_workflow

**File:** `graphrag/index/workflows/create_final_documents.py` (lines 19-33)

## Signature

```python
def run_workflow(
    _config: GraphRagConfig,
    context: PipelineRunContext,
) -> WorkflowFunctionOutput
```

## Description

Runs the final documents transformation workflow.

This async function loads the documents and text_units tables from storage via the given context, creates the final documents with create_final_documents, writes the resulting documents table back to storage, and returns a WorkflowFunctionOutput containing the produced DataFrame.

Args:
  _config: GraphRagConfig
      GraphRag configuration used by the workflow.
  context: PipelineRunContext
      Runtime context including the output storage handle.

Returns:
  WorkflowFunctionOutput
      The workflow output whose result is the final documents DataFrame.

Raises:
  Exception
      Exceptions raised by the storage backend or by the create_final_documents
      operation may propagate to the caller.

## Dependencies

This function calls:

- `graphrag/index/typing/workflow.py::WorkflowFunctionOutput`
- `graphrag/index/workflows/create_final_documents.py::create_final_documents`
- `graphrag/utils/storage.py::load_table_from_storage`
- `graphrag/utils/storage.py::write_table_to_storage`

## Called By

This function is called by:

- `tests/verbs/test_create_final_documents.py::test_create_final_documents`
- `tests/verbs/test_create_final_documents.py::test_create_final_documents_with_metadata_column`

