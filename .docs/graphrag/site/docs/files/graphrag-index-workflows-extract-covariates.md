---
sidebar_position: 124
---

# graphrag/index/workflows/extract_covariates.py

## Overview

Covariate extraction workflows for GraphRAG index workflows.

Purpose:
This module provides the core workflow functions to extract covariates as part of GraphRAG indexing. It coordinates inputs, configuration, storage, and callbacks.

Key exports:
- extract_covariates(text_units: pd.DataFrame, callbacks: WorkflowCallbacks, cache: PipelineCache, covariate_type: str, extraction_strategy: dict[str, Any] | None, async_mode: AsyncType = AsyncType.AsyncIO, entity_types: list[str] | None = None, num_threads: int = 4) -&gt; pd.DataFrame
- run_workflow(config: GraphRagConfig, context: PipelineRunContext) -&gt; WorkflowFunctionOutput

Summary:
Implements end-to-end covariate extraction and orchestration within the GraphRAG indexing workflow.

Functions:
extract_covariates
  Args:
  - text_units (pd.DataFrame): Input text units to process. Must contain at least the columns "id" and "text". This function mutates text_units in place by adding a temporary text_unit_id column equal to id, and then removes it before returning.
  - callbacks (WorkflowCallbacks): Callbacks used during the extraction workflow.
  - cache (PipelineCache): Cache used during the extraction workflow.
  - covariate_type (str): Type of covariate to extract.
  - extraction_strategy (dict[str, Any] | None): Extraction strategy.
  - async_mode (AsyncType): Async execution mode. Defaults to AsyncType.AsyncIO.
  - entity_types (list[str] | None): Optional entity types to consider.
  - num_threads (int): Number of worker threads to use.
  Returns:
  - pd.DataFrame: DataFrame containing the extracted covariates.
  Raises:
  - Exception types raised by underlying components.

run_workflow
  Args:
  - config (GraphRagConfig): GraphRag configuration used to control extraction behavior.
  - context (PipelineRunContext): Context for the current pipeline run.
  Returns:
  - WorkflowFunctionOutput: The output of the workflow execution.
  Raises:
  - Exception types raised by underlying components.

## Functions

- [`extract_covariates`](../api/functions/graphrag-index-workflows-extract-covariates-extract-covariates)
- [`run_workflow`](../api/functions/graphrag-index-workflows-extract-covariates-run-workflow)

