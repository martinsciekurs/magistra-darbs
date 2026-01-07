---
sidebar_position: 135
---

# graphrag/index/workflows/update_community_reports.py

## Overview

Utilities to update community reports during incremental GraphRAG index runs.

Purpose
Provide the workflow helpers to merge existing (previous) and updated (delta) community reports and persist the result to storage as part of an incremental GraphRAG run.

Key exports
- _update_community_reports(previous_storage: PipelineStorage, delta_storage: PipelineStorage, output_storage: PipelineStorage, community_id_mapping: dict) -&gt; pd.DataFrame
  Merge old and delta community reports and write the merged results to storage. Returns the merged DataFrame.
- run_workflow(config: GraphRagConfig, context: PipelineRunContext) -&gt; WorkflowFunctionOutput
  Drive the update of community reports for an incremental index run using the provided config and run context.

Brief summary
This module encapsulates the internal workflow steps needed to update community reports by integrating updates with the existing report dataset
and persisting the merged results to the configured storage backends during incremental processing.

## Functions

- [`_update_community_reports`](../api/functions/graphrag-index-workflows-update-community-reports-update-community-reports)
- [`run_workflow`](../api/functions/graphrag-index-workflows-update-community-reports-run-workflow)

