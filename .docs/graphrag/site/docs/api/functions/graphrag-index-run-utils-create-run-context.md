---
sidebar_position: 170
---

# create_run_context

**File:** `graphrag/index/run/utils.py` (lines 20-38)

## Signature

```python
def create_run_context(
    input_storage: PipelineStorage | None = None,
    output_storage: PipelineStorage | None = None,
    previous_storage: PipelineStorage | None = None,
    cache: PipelineCache | None = None,
    callbacks: WorkflowCallbacks | None = None,
    stats: PipelineRunStats | None = None,
    state: PipelineState | None = None,
) -> PipelineRunContext
```

## Description

Create the run context for the pipeline.

Args:
    input_storage: PipelineStorage | None
        The input storage to use for the run.
    output_storage: PipelineStorage | None
        The output storage to use for the run.
    previous_storage: PipelineStorage | None
        The previous storage to use for the run.
    cache: PipelineCache | None
        The cache to use for the run.
    callbacks: WorkflowCallbacks | None
        The workflow callbacks to use during the run.
    stats: PipelineRunStats | None
        The statistics collector for the run.
    state: PipelineState | None
        Initial state for the run.

Returns:
    PipelineRunContext: The configured run context.

## Dependencies

This function calls:

- `graphrag.cache.memory_pipeline_cache::InMemoryCache`
- `graphrag/callbacks/noop_workflow_callbacks.py::NoopWorkflowCallbacks`
- `graphrag/index/typing/context.py::PipelineRunContext`
- `graphrag/index/typing/stats.py::PipelineRunStats`
- `graphrag/storage/memory_pipeline_storage.py::MemoryPipelineStorage`

## Called By

This function is called by:

- `graphrag/index/run/run_pipeline.py::run_pipeline`
- `tests/verbs/test_pipeline_state.py::test_pipeline_state`
- `tests/verbs/test_pipeline_state.py::test_pipeline_existing_state`
- `tests/verbs/util.py::create_test_context`

