---
sidebar_position: 69
---

# graphrag/index/operations/extract_graph/extract_graph.py

## Overview

Utilities for extracting graph data from text using configurable entity extraction strategies.

Overview:
This module provides the core logic to load entity extraction strategies, run extraction per input row, and merge resulting entities and relationships into consolidated DataFrames that can be used to build a graph. It coordinates with the graph intelligence layer to produce graph representations from text data.

Exports:
- _load_strategy(strategy_type: ExtractEntityStrategyType) -&gt; EntityExtractStrategy
  Load the strategy method implementation for the given strategy type.
- _merge_entities(entity_dfs) -&gt; pandas.DataFrame
  Merge and aggregate multiple entity DataFrames into a single aggregated entities DataFrame by
  title and type. Each DataFrame is expected to include the columns: "title", "type",
  "description", and "source_id".
- _merge_relationships(relationship_dfs) -&gt; pandas.DataFrame
  Merge multiple relationship DataFrames into a single aggregated DataFrame by source and target.
  Each DataFrame should contain at least the columns 'source', 'target', 'description',
  'source_id', and 'weight'.
- run_strategy(row)
  Run a strategy on a single input row to extract graph data. Args: row: A row from the input DataFrame
  containing the values for text_column and id_column. Returns: a list with three elements: the
  entities, relationships, and graph returned by the strategy execution for this row. Raises:
  Exceptions raised by the strategy.
- extract_graph(
    text_units: pd.DataFrame,
    callbacks: WorkflowCallbacks,
    cache: PipelineCache,
    text_column: str,
    id_column: str,
    strategy: dict[str, Any] | None,
    async_mode: AsyncType = AsyncType.AsyncIO,
    entity_types=DEFAULT_ENTITY_TYPES,
    num_threads: int = 4,
  ) -&gt; tuple[pd.DataFrame, pd.DataFrame]
  Extract a graph from a piece of text using a language model. Returns a tuple of (entities_df,\n  relationships_df).

Notes:
- DEFAULT_ENTITY_TYPES defines the default entity types used when none are provided.
- This module relies on types and classes such as PipelineCache, WorkflowCallbacks, AsyncType, and
  typing helpers defined in graphrag.index.operations.extract_graph.typing.

## Functions

- [`_load_strategy`](../api/functions/graphrag-index-operations-extract-graph-extract-graph-load-strategy)
- [`_merge_entities`](../api/functions/graphrag-index-operations-extract-graph-extract-graph-merge-entities)
- [`_merge_relationships`](../api/functions/graphrag-index-operations-extract-graph-extract-graph-merge-relationships)
- [`run_strategy`](../api/functions/graphrag-index-operations-extract-graph-extract-graph-run-strategy)
- [`extract_graph`](../api/functions/graphrag-index-operations-extract-graph-extract-graph-extract-graph)

