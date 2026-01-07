---
sidebar_position: 240
---

# run_workflow

**File:** `graphrag/index/workflows/extract_covariates.py` (lines 27-61)

## Signature

```python
def run_workflow(
    config: GraphRagConfig,
    context: PipelineRunContext,
) -> WorkflowFunctionOutput
```

## Description

Run the covariates extraction workflow.

This asynchronous workflow performs the following steps:
- If extraction of claims is enabled in the provided config:
  - Load text_units from storage using the context's output storage.
  - Get language model settings for the configured claims model and resolve the extraction strategy.
  - Execute extract_covariates with the prepared inputs and write the resulting covariates to storage under the name covariates.
- If extraction is disabled:
  - Skip loading, extraction, and writing; output remains None.

The function returns a WorkflowFunctionOutput whose result is the covariates DataFrame when extraction occurred, or None when extraction was skipped.

Args:
  config (GraphRagConfig): GraphRag configuration for the covariates extraction workflow.
  context (PipelineRunContext): Pipeline run context containing the output storage, callbacks, and cache used by the workflow.

Returns:
  WorkflowFunctionOutput: The workflow output wrapper containing the covariates DataFrame, or None if extraction was skipped.

Raises:
  ValueError: Could not find required parquet files in storage, or other storage load errors.
  Exception: Exceptions raised by the storage backend or the covariate extraction process may propagate during the workflow.

Note:
  The function may propagate exceptions from storage or extraction; these are not caught within the workflow.

## Dependencies

This function calls:

- `graphrag/index/operations/extract_covariates/extract_covariates.py::extract_covariates`
- `graphrag/index/typing/workflow.py::WorkflowFunctionOutput`
- `graphrag/utils/storage.py::load_table_from_storage`
- `graphrag/utils/storage.py::write_table_to_storage`

## Called By

This function is called by:

- `tests/verbs/test_extract_covariates.py::test_extract_covariates`

