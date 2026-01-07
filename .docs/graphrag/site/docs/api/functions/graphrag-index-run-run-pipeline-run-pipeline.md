---
sidebar_position: 168
---

# run_pipeline

**File:** `graphrag/index/run/run_pipeline.py` (lines 29-101)

## Signature

```python
def run_pipeline(
    pipeline: Pipeline,
    config: GraphRagConfig,
    callbacks: WorkflowCallbacks,
    is_update_run: bool = False,
    additional_context: dict[str, Any] | None = None,
    input_documents: pd.DataFrame | None = None,
) -> AsyncIterable[PipelineRunResult]
```

## Description

Run all workflows using a simplified pipeline.

Args:
    pipeline: Pipeline
        The pipeline to run.
    config: GraphRagConfig
        The GraphRag configuration to use for the run.
    callbacks: WorkflowCallbacks
        The callbacks to invoke during workflow execution.
    is_update_run: bool
        Whether this run should perform an incremental update (default: False).
    additional_context: dict[str, Any] | None
        Optional additional context to merge into the run state.
    input_documents: pd.DataFrame | None
        Optional input documents. If provided, they will be written directly to storage
        (skipping the usual load/parse steps) before running the pipeline.

Returns:
    AsyncIterable[PipelineRunResult]
        An asynchronous iterable that yields a PipelineRunResult for each workflow as it runs.

Raises:
    ValueError: If the storage type is not registered.
    Exception: May raise any exception raised by storage backends during read/write operations or by the pipeline execution.

## Dependencies

This function calls:

- `graphrag/index/run/run_pipeline.py::_copy_previous_output`
- `graphrag/index/run/run_pipeline.py::_run_pipeline`
- `graphrag/index/run/utils.py::create_run_context`
- `graphrag/utils/api.py::create_cache_from_config`
- `graphrag/utils/api.py::create_storage_from_config`
- `graphrag/utils/storage.py::write_table_to_storage`

## Called By

This function is called by:

- `graphrag/api/index.py::build_index`

