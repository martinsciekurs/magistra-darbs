---
sidebar_position: 125
---

# graphrag/index/workflows/extract_graph.py

## Overview

Module that orchestrates the extract_graph workflow within the graphrag indexing pipeline. It wires together data validation, graph extraction, summarization of entities and relationships, and persistence to storage. This module exposes the main workflow entry point and helper utilities used by the indexing pipeline to build and persist the base entity graph.

Key exports:
  - _validate_data(df: pd.DataFrame) -&gt; bool: Validate that the dataframe has data.
  - get_summarized_entities_relationships( 
      extracted_entities: pd.DataFrame,
      extracted_relationships: pd.DataFrame,
      callbacks: WorkflowCallbacks,
      cache: PipelineCache,
      summarization_strategy: dict[str, Any] | None = None,
      summarization_num_threads: int = 4,
    ) -&gt; tuple[pd.DataFrame, pd.DataFrame]
  - extract_graph(
      text_units: pd.DataFrame,
      callbacks: WorkflowCallbacks,
      cache: PipelineCache,
      extraction_strategy: dict[str, Any] | None = None,
      extraction_num_threads: int = 4,
      extraction_async_mode: AsyncType = AsyncType.AsyncIO,
      entity_types: list[str] | None = None,
      summarization_strategy: dict[str, Any] | None = None,
      summarization_num_threads: int = 4,
    ) -&gt; tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]
  - run_workflow(
      config: GraphRagConfig,
      context: PipelineRunContext,
    ) -&gt; WorkflowFunctionOutput

Overview:
  This module serves as the orchestration layer for constructing the base entity graph from text units by combining extraction, summarization, and persistence steps. It relies on underlying operations and utilities to perform the actual work and exposes a clear entry point for running the workflow within a larger pipeline.

Args:
  None: The module exposes functions with their own typed parameters; there are no module-level arguments.

Returns:
  None: The module defines functions that return values, but the module itself does not return a value upon import.

Raises:
  Exceptions raised by the underlying components (e.g., extract_graph, summarize_descriptions, and storage utilities) may propagate to the caller.

## Functions

- [`_validate_data`](../api/functions/graphrag-index-workflows-extract-graph-validate-data)
- [`get_summarized_entities_relationships`](../api/functions/graphrag-index-workflows-extract-graph-get-summarized-entities-relationships)
- [`extract_graph`](../api/functions/graphrag-index-workflows-extract-graph-extract-graph)
- [`run_workflow`](../api/functions/graphrag-index-workflows-extract-graph-run-workflow)

