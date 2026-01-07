---
sidebar_position: 99
---

# graphrag/index/run/run_pipeline.py

## Overview

Utilities for running the GraphRag index run pipeline.

This module implements helpers to execute a GraphRag pipeline, persist run state,
and copy outputs between storages. It exposes a public run_pipeline entry point and
private helpers used internally by the run workflow.

Exports:
- _dump_json(context: PipelineRunContext) -&gt; None
  Dumps the stats and context state to the storage.

  Args:
    context: PipelineRunContext The pipeline run context containing stats, state, and output storage used for persistence.

  Returns:
    None

  Raises:
    Exception If storage operations fail or JSON serialization fails.

- _copy_previous_output(storage: PipelineStorage, copy_storage: PipelineStorage) -&gt; None
  Copy parquet outputs from the source storage to the copy storage asynchronously.

  Args:
    storage: PipelineStorage The source storage containing parquet outputs.
    copy_storage: PipelineStorage The destination storage where outputs will be copied.

  Returns:
    None

  Raises:
    Exception If copy operations fail.

- _run_pipeline(pipeline: Pipeline, config: GraphRagConfig, context: PipelineRunContext) -&gt; AsyncIterable[PipelineRunResult]
  Execute the provided pipeline asynchronously and yield results for each workflow as it completes.

  Args:
    pipeline: Pipeline The pipeline to run
    config: GraphRagConfig Configuration for the run
    context: PipelineRunContext Runtime context, including storage, callbacks, and state

  Returns:
    AsyncIterable[PipelineRunResult] An async iterable that yields a PipelineRunResult for each workflow.

  Raises:
    Exception If the pipeline execution fails.

- run_pipeline(pipeline: Pipeline, config: GraphRagConfig, callbacks: WorkflowCallbacks, is_update_run: bool = False, additional_context: dict[str, Any] | None = None, input_documents: pd.DataFrame | None = None) -&gt; AsyncIterable[PipelineRunResult]
  Run all workflows using a simplified pipeline.

  Args:
    pipeline: Pipeline The pipeline to run.
    config: GraphRagConfig The GraphRag configuration to use for the run.
    callbacks: WorkflowCallbacks The callbacks to invoke during workflow execution.
    is_update_run: bool Whether this run should perform an incremental update (default: False).
    additional_context: dict[str, Any] | None Additional context to pass into the run.
    input_documents: pd.DataFrame | None Optional input documents for the run.

  Returns:
    AsyncIterable[PipelineRunResult] An async iterable that yields a PipelineRunResult for each workflow as it completes.

  Raises:
    Exception If the run fails.

## Functions

- [`_dump_json`](../api/functions/graphrag-index-run-run-pipeline-dump-json)
- [`_copy_previous_output`](../api/functions/graphrag-index-run-run-pipeline-copy-previous-output)
- [`_run_pipeline`](../api/functions/graphrag-index-run-run-pipeline-run-pipeline)
- [`run_pipeline`](../api/functions/graphrag-index-run-run-pipeline-run-pipeline)

