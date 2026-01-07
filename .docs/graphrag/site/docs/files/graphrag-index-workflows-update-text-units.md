---
sidebar_position: 140
---

# graphrag/index/workflows/update_text_units.py

## Overview

Utilities to update and merge text units for incremental GraphRAG runs.

This module provides utilities to update and merge text units by applying a delta of text units to the existing set and to write the merged result to storage as part of an incremental index workflow. It supports asynchronous-like orchestration by reading from previous and delta storages and persisting the merged output to an output storage.

Key exports:
- _update_and_merge_text_units(old_text_units: pd.DataFrame, delta_text_units: pd.DataFrame, entity_id_mapping: dict) -&gt; pd.DataFrame
  Update and merge text units given the current and delta dataframes and an entity ID mapping.
- _update_text_units(previous_storage: PipelineStorage, delta_storage: PipelineStorage, output_storage: PipelineStorage, entity_id_mapping: dict) -&gt; pd.DataFrame
  Asynchronously update and merge text units from storage and write the result to the output storage.
- run_workflow(config: GraphRagConfig, context: PipelineRunContext) -&gt; WorkflowFunctionOutput
  Entry point to run the text unit update workflow for an incremental index run.

Brief summary: Orchestrates incremental text unit updates by applying delta data to existing units and persisting the merged result in the configured storages within the GraphRAG workflow.

## Functions

- [`_update_and_merge_text_units`](../api/functions/graphrag-index-workflows-update-text-units-update-and-merge-text-units)
- [`_update_text_units`](../api/functions/graphrag-index-workflows-update-text-units-update-text-units)
- [`run_workflow`](../api/functions/graphrag-index-workflows-update-text-units-run-workflow)

