---
sidebar_position: 2
---

# build_index

**File:** `graphrag/api/index.py` (lines 29-96)

## Signature

```python
def build_index(
    config: GraphRagConfig,
    method: IndexingMethod | str = IndexingMethod.Standard,
    is_update_run: bool = False,
    memory_profile: bool = False,
    callbacks: list[WorkflowCallbacks] | None = None,
    additional_context: dict[str, Any] | None = None,
    verbose: bool = False,
    input_documents: pd.DataFrame | None = None,
) -> list[PipelineRunResult]
```

## Description

Run the indexing pipeline with the given configuration.

The asynchronous function orchestrates the indexing workflow: it initializes logging, prepares a callback chain, determines the final indexing method (including update semantics), builds the pipeline, executes the run, collects outputs, and returns them as a list of PipelineRunResult.

Parameters
----------
config : GraphRagConfig
    The configuration for GraphRAG indexing.
method : IndexingMethod | str default=IndexingMethod.Standard
    Styling of indexing to perform (full LLM, NLP + LLM, etc.). If a string is provided, it will be used directly.
is_update_run : bool
    Indicates whether this is an incremental update run. When True, the final method name will be suffixed with "-update".
memory_profile : bool
    Whether to enable memory profiling. Note: Memory profiling is not yet supported and a warning is logged.
callbacks : list[WorkflowCallbacks] | None default=None
    A list of callbacks to register for the pipeline lifecycle. If None, a NoopWorkflowCallbacks is used.
additional_context : dict[str, Any] | None default=None
    Additional context to pass to the pipeline run. This can be accessed in the pipeline state under the 'additional_context' key.
verbose : bool
    Enables verbose logging during initialization. Affects the logging configuration.
input_documents : pd.DataFrame | None default=None
    Override document loading and parsing and supply your own dataframe of documents to index.

Returns
-------
list[PipelineRunResult]
    The list of pipeline run results

Raises
------
Exception
    Exceptions raised by underlying components (e.g., logging initialization, pipeline execution) may propagate to the caller.

Notes
-----
- This function is asynchronous and must be awaited.
- The final method name is determined by _get_method(method, is_update_run).

## Dependencies

This function calls:

- `graphrag/api/index.py::_get_method`
- `graphrag/callbacks/noop_workflow_callbacks.py::NoopWorkflowCallbacks`
- `graphrag/index/run/run_pipeline.py::run_pipeline`
- `graphrag/index/run/utils.py::create_callback_chain`
- `graphrag/logger/standard_logging.py::init_loggers`

