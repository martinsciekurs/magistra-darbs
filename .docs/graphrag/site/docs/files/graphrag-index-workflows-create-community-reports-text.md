---
sidebar_position: 121
---

# graphrag/index/workflows/create_community_reports_text.py

## Overview

Create and manage the community reports text workflow.

Overview:
This module provides workflows to transform input data into finalized community reports text by building local contexts and summarizing communities, and to run the end-to-end workflow that loads inputs, configures language-model and summarization settings, generates the reports text, and persists results to storage.

Key exports:
- create_community_reports_text(entities: pd.DataFrame, communities: pd.DataFrame, text_units: pd.DataFrame, callbacks: WorkflowCallbacks, cache: PipelineCache, summarization_strategy: dict, async_mode: AsyncType = AsyncType.AsyncIO, num_threads: int = 4) -&gt; pd.DataFrame
  Transforms input data into finalized community reports by building local contexts and summarizing communities.
  Args:
    entities: DataFrame containing entities data used to explode communities into nodes.
    communities: DataFrame containing community definitions and metadata.
    text_units: DataFrame containing text unit data.
    callbacks: WorkflowCallbacks instance for workflow callbacks.
    cache: PipelineCache instance used for caching intermediate results.
    summarization_strategy: dict specifying summarization parameters.
    async_mode: AsyncType mode to run the workflow.
    num_threads: Number of threads to use.
  Returns:
    DataFrame with the finalized community reports.

- run_workflow(config: GraphRagConfig, context: PipelineRunContext) -&gt; WorkflowFunctionOutput
  Runs the workflow to transform community reports text and persists the results to storage.
  Args:
    config: GraphRagConfig containing configuration values for the workflow.
    context: PipelineRunContext with runtime context and state.
  Returns:
    WorkflowFunctionOutput containing the results and status.

Notes:
- This module depends on components such as PipelineCache, WorkflowCallbacks, GraphRagConfig, LanguageModelConfig, and storage utilities to perform its operations.

## Functions

- [`create_community_reports_text`](../api/functions/graphrag-index-workflows-create-community-reports-text-create-community-reports-text)
- [`run_workflow`](../api/functions/graphrag-index-workflows-create-community-reports-text-run-workflow)

