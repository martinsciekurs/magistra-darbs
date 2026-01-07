---
sidebar_position: 134
---

# graphrag/index/workflows/update_communities.py

## Overview

Module for updating and merging community data during incremental GraphRAG index runs.

Overview
This module exposes two callables used by the GraphRAG index workflow:
- _update_communities(previous_storage, delta_storage, output_storage): Merges existing (previous) and delta (updated) communities and writes the merged result to output_storage. Returns a dict mapping original delta community IDs to the new IDs assigned during the merge.
- run_workflow(config, context): Orchestrates the update of communities from an incremental index run. Returns a WorkflowFunctionOutput describing the outcome of the run. The implementation uses GraphRagConfig and PipelineRunContext and delegates the merge operation to _update_and_merge_communities.

Key details
- The module relies on get_update_storages to locate the relevant PipelineStorage instances for previous, delta, and output data.
- The actual merge logic is performed by _update_and_merge_communities; _update_communities simply coordinates inputs/outputs and returns the ID mapping.
- The run_workflow function returns a WorkflowFunctionOutput (not None) and may raise exceptions on failure; callers should handle these as part of the workflow execution.

Parameters
- For _update_communities:
  - previous_storage: PipelineStorage containing the existing communities.
  - delta_storage: PipelineStorage containing the updated/delta communities.
  - output_storage: PipelineStorage where merged communities are written.
Returns
  - dict: mapping from original delta IDs to new IDs assigned during the merge.
Raises
  - Exception: if loading, merging, or writing data fails.

- For run_workflow:
  - config: GraphRagConfig configuring the workflow.
  - context: PipelineRunContext carrying run state (e.g., update_timestamp).
Returns
  - WorkflowFunctionOutput: the structured output of the workflow execution.
Raises
  - Exception: if preconditions fail or storage/merge operations fail.

## Functions

- [`_update_communities`](../api/functions/graphrag-index-workflows-update-communities-update-communities)
- [`run_workflow`](../api/functions/graphrag-index-workflows-update-communities-run-workflow)

