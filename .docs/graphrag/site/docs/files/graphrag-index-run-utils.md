---
sidebar_position: 100
---

# graphrag/index/run/utils.py

## Overview

Utilities for running a GraphRAG pipeline by providing helpers to create a callback chain, assemble a run context, and derive update-related storage objects.

Key exports
- create_callback_chain(callbacks: list[WorkflowCallbacks] | None) -&gt; WorkflowCallbacks
- create_run_context(input_storage: PipelineStorage | None = None, output_storage: PipelineStorage | None = None, previous_storage: PipelineStorage | None = None, cache: PipelineCache | None = None, callbacks: WorkflowCallbacks | None = None, stats: PipelineRunStats | None = None, state: PipelineState | None = None) -&gt; PipelineRunContext
- get_update_storages(config: GraphRagConfig, timestamp: str) -&gt; tuple[PipelineStorage, PipelineStorage, PipelineStorage]

Functions
def create_callback_chain(callbacks: list[WorkflowCallbacks] | None) -&gt; WorkflowCallbacks
  Create a callback manager that encompasses multiple callbacks.
  Args:
    callbacks: list[WorkflowCallbacks] | None. The callbacks to register on the manager. If None, an empty list is used.
  Returns:
    WorkflowCallbacks: A manager that aggregates the provided callbacks.
  Raises:
    Propagates exceptions raised by underlying components.

def create_run_context(
  input_storage: PipelineStorage | None = None,
  output_storage: PipelineStorage | None = None,
  previous_storage: PipelineStorage | None = None,
  cache: PipelineCache | None = None,
  callbacks: WorkflowCallbacks | None = None,
  stats: PipelineRunStats | None = None,
  state: PipelineState | None = None,
) -&gt; PipelineRunContext
  Create the run context for the pipeline.
  Args:
    input_storage: PipelineStorage | None The input storage to use for the run.
    output_storage: PipelineStorage | None The output storage to use for the run.
    previous_storage: PipelineStorage | None The previous storage to use for the run.
    cache: PipelineCache | None The cache to use for the run.
    callbacks: WorkflowCallbacks | None The callbacks to apply during the run.
    stats: PipelineRunStats | None The stats collector for the run.
    state: PipelineState | None The state for the run.
  Returns:
    PipelineRunContext: The run context for the pipeline.
  Raises:
    Propagates exceptions from underlying components.

def get_update_storages(config: GraphRagConfig, timestamp: str) -&gt; tuple[PipelineStorage, PipelineStorage, PipelineStorage]
  Get storage objects for the update index run.
  Args:
    config: GraphRagConfig The GraphRag configuration used to derive storages from.
    timestamp: str The timestamp applied to the update storage to create a timestamped storage.
  Returns:
    tuple[PipelineStorage, PipelineStorage, PipelineStorage]: The output_storage, update_storage, and timestamped_storage.
  Raises:
    Propagates exceptions from storage creation.

## Functions

- [`create_callback_chain`](../api/functions/graphrag-index-run-utils-create-callback-chain)
- [`create_run_context`](../api/functions/graphrag-index-run-utils-create-run-context)
- [`get_update_storages`](../api/functions/graphrag-index-run-utils-get-update-storages)

