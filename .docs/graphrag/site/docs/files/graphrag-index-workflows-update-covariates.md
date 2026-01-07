---
sidebar_position: 136
---

# graphrag/index/workflows/update_covariates.py

## Overview

Utilities to update covariates from incremental GraphRAG runs by merging existing covariates with delta covariates and persisting results to storage.

This module provides internal helpers for covariate merging and applying updates, as well as the public run_workflow function that orchestrates the covariate update workflow for an incremental GraphRAG run.

Exports:
- _merge_covariates(old_covariates: pd.DataFrame, delta_covariates: pd.DataFrame) -&gt; pd.DataFrame
- _update_covariates(previous_storage: PipelineStorage, delta_storage: PipelineStorage, output_storage: PipelineStorage) -&gt; None
- run_workflow(config: GraphRagConfig, context: PipelineRunContext) -&gt; WorkflowFunctionOutput

Summary:
The workflow reads existing covariates and delta covariates from storage, merges them via _merge_covariates, and persists the updated covariates back to storage via _update_covariates within the incremental GraphRAG run.

## Functions

- [`_merge_covariates`](../api/functions/graphrag-index-workflows-update-covariates-merge-covariates)
- [`_update_covariates`](../api/functions/graphrag-index-workflows-update-covariates-update-covariates)
- [`run_workflow`](../api/functions/graphrag-index-workflows-update-covariates-run-workflow)

