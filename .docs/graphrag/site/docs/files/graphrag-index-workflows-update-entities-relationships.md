---
sidebar_position: 137
---

# graphrag/index/workflows/update_entities_relationships.py

## Overview

Utilities to update entities and relationships during incremental index runs in GraphRag.

Summary:
This module defines two core functions that drive the incremental update of entities and relationships by merging previous state with delta updates, updating and merging relationships, applying summarization, and writing results to output storage. The functions are designed to be composed within a larger workflow pipeline and rely on storage, config, and callback mechanisms.

Exports:
- _update_entities_and_relationships: Merges previous entities with delta, updates and merges relationships, applies summarization, and writes results to output storage.
- run_workflow: Runs the incremental update workflow given a GraphRagConfig and PipelineRunContext, returning a WorkflowFunctionOutput. May raise KeyError.

Functions
- _update_entities_and_relationships(
    previous_storage: PipelineStorage,
    delta_storage: PipelineStorage,
    output_storage: PipelineStorage,
    config: GraphRagConfig,
    cache: PipelineCache,
    callbacks: WorkflowCallbacks,
  ) -&gt; tuple[pd.DataFrame, pd.DataFrame, dict]
  Args:
    previous_storage: The storage containing the previous state data.
    delta_storage: The storage containing the delta updates.
    output_storage: The storage where results are written.
    config: GraphRagConfig containing configuration for the workflow.
    cache: PipelineCache used during processing.
    callbacks: WorkflowCallbacks to handle workflow events.
  Returns:
    A tuple of (entities_df, relationships_df, summaries) representing the merged entities,
    merged/updated relationships, and any summarization metadata.
  Raises:
    (not specified)

- run_workflow(
    config: GraphRagConfig,
    context: PipelineRunContext,
  ) -&gt; WorkflowFunctionOutput
  Args:
    config: GraphRagConfig containing configuration for the workflow.
    context: PipelineRunContext carrying the state for the run, including update_timestamp.
  Returns:
    WorkflowFunctionOutput: The output of the workflow function.
  Raises:
    KeyError: if required keys are missing from the context or config.

## Functions

- [`_update_entities_and_relationships`](../api/functions/graphrag-index-workflows-update-entities-relationships-update-entities-and-relationships)
- [`run_workflow`](../api/functions/graphrag-index-workflows-update-entities-relationships-run-workflow)

