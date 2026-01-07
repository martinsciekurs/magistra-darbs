---
sidebar_position: 126
---

# graphrag/index/workflows/extract_graph_nlp.py

## Overview

Module for extracting the base entity graph from NLP-derived text units and persisting results to storage as part of the GraphRAG NLP workflow.

Exports:
- extract_graph_nlp(text_units: pd.DataFrame, cache: PipelineCache, extraction_config: ExtractGraphNLPConfig) -&gt; tuple[pd.DataFrame, pd.DataFrame]
- run_workflow(config: GraphRagConfig, context: PipelineRunContext) -&gt; WorkflowFunctionOutput

Overview:
This module provides functionality to asynchronously extract a noun-phrase based entity graph (nodes and edges) from input text units and to orchestrate the full workflow of loading text units from storage, performing extraction, persisting the resulting tables back to storage, and returning the produced results wrapped in a WorkflowFunctionOutput.

Functions:
- extract_graph_nlp(text_units: pd.DataFrame, cache: PipelineCache, extraction_config: ExtractGraphNLPConfig) -&gt; tuple[pd.DataFrame, pd.DataFrame]
  Asynchronously extract the base entity graph (nodes and edges) from the given text units.
  Args:
  - text_units: pd.DataFrame: Input text units used to extract noun phrases for graph construction.
  - cache: PipelineCache: Cache used during extraction and graph construction.
  - extraction_config: ExtractGraphNLPConfig: Configuration for extraction settings, including text_analyzer, normalize_edge...
  Returns:
  - tuple[pd.DataFrame, pd.DataFrame]: A tuple containing the nodes and edges DataFrames representing the extracted graph.
  Raises:
  - May raise exceptions from NLP processing or storage I/O.

- run_workflow(config: GraphRagConfig, context: PipelineRunContext) -&gt; WorkflowFunctionOutput
  Run the extract_graph_nlp workflow to build the base entity graph and persist results to storage.
  This coroutine orchestrates the extraction of noun-phrase based graph components by loading text units from storage, invoking extract_graph_nlp to produce entities and relationships, writing the resulting tables back to storage, and returning a WorkflowFunctionOutput containing the produced data.
  Args:
  - config: GraphRagConfig: Configuration for the Rag workflow and extraction.
  - context: PipelineRunContext: Execution context for the workflow, including storage and run metadata.
  Returns:
  - WorkflowFunctionOutput: The produced data and references as produced by the workflow.
  Raises:
  - May raise exceptions from storage I/O or NLP processing.

## Functions

- [`extract_graph_nlp`](../api/functions/graphrag-index-workflows-extract-graph-nlp-extract-graph-nlp)
- [`run_workflow`](../api/functions/graphrag-index-workflows-extract-graph-nlp-run-workflow)

