---
sidebar_position: 228
---

# run_workflow

**File:** `graphrag/index/workflows/create_community_reports.py` (lines 42-81)

## Signature

```python
def run_workflow(
    config: GraphRagConfig,
    context: PipelineRunContext,
) -> WorkflowFunctionOutput
```

## Description

Runs the create_community_reports workflow to transform community reports and persist the results.

Args:
  config: GraphRagConfig containing settings used by the workflow, including language model and data extraction configurations.
  context: PipelineRunContext providing access to output_storage, callbacks, and cache used during the workflow.

Returns:
  WorkflowFunctionOutput: The output of the workflow, which wraps the resulting community_reports DataFrame.

Raises:
  ValueError: Could not find required parquet file in storage during loading.
  Exception: Exceptions raised by the storage backend or parquet reader during load or write operations.

## Dependencies

This function calls:

- `graphrag/index/typing/workflow.py::WorkflowFunctionOutput`
- `graphrag/index/workflows/create_community_reports.py::create_community_reports`
- `graphrag/utils/storage.py::load_table_from_storage`
- `graphrag/utils/storage.py::storage_has_table`
- `graphrag/utils/storage.py::write_table_to_storage`

## Called By

This function is called by:

- `tests/verbs/test_create_community_reports.py::test_create_community_reports`

