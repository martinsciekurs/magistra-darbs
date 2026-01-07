---
sidebar_position: 221
---

# run_workflow

**File:** `graphrag/index/workflows/create_base_text_units.py` (lines 25-50)

## Signature

```python
def run_workflow(
    config: GraphRagConfig,
    context: PipelineRunContext,
) -> WorkflowFunctionOutput
```

## Description

Run the base text units workflow to transform documents into base text units by loading documents from storage, chunking them, and writing the resulting text units back to storage.

Args:
  config (GraphRagConfig): GraphRag configuration for the workflow, including chunking settings such as group_by_columns, size, overlap, encoding_model, strategy, prepend_metadata, and chunk_size_includes_metadata.
  context (PipelineRunContext): Pipeline run context containing the output storage and callbacks used for loading input and writing output.

Returns:
  WorkflowFunctionOutput: The workflow output containing the produced text_units DataFrame.

Raises:
  ValueError: Could not find documents.parquet in storage!
  Exception: Exceptions raised by the storage backend or parquet reader during the load or write operations may propagate.

## Dependencies

This function calls:

- `graphrag/index/typing/workflow.py::WorkflowFunctionOutput`
- `graphrag/index/workflows/create_base_text_units.py::create_base_text_units`
- `graphrag/utils/storage.py::load_table_from_storage`
- `graphrag/utils/storage.py::write_table_to_storage`

## Called By

This function is called by:

- `tests/verbs/test_create_base_text_units.py::test_create_base_text_units`
- `tests/verbs/test_create_base_text_units.py::test_create_base_text_units_metadata`
- `tests/verbs/test_create_base_text_units.py::test_create_base_text_units_metadata_included_in_chunk`

