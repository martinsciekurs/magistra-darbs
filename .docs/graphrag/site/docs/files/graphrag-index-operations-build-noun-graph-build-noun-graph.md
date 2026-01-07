---
sidebar_position: 47
---

# graphrag/index/operations/build_noun_graph/build_noun_graph.py

## Overview

Utilities for building a noun graph from text units by extracting noun phrases and linking co-occurring nouns.

Purpose:
This module provides the building blocks to (1) extract noun-phrase nodes from text units, (2) derive edges between nouns that co-occur in the same text unit, and (3) assemble a noun-graph representation suitable for indexing and analysis. Edge weights can be computed using PMI normalization when requested.

Key exports:
- _extract_edges(nodes_df: pd.DataFrame, normalize_edge_weights: bool = True) -&gt; pd.DataFrame
- extract(row)
- _extract_nodes(
    text_unit_df: pd.DataFrame,
    text_analyzer: BaseNounPhraseExtractor,
    num_threads: int = 4,
    async_mode: AsyncType = AsyncType.Threaded,
    cache: PipelineCache | None = None,
  ) -&gt; pd.DataFrame
- build_noun_graph(
    text_unit_df: pd.DataFrame,
    text_analyzer: BaseNounPhraseExtractor,
    normalize_edge_weights: bool,
    num_threads: int = 4,
    async_mode: AsyncType = AsyncType.Threaded,
    cache: PipelineCache | None = None,
  ) -&gt; tuple[pd.DataFrame, pd.DataFrame]

Brief summary:
The module coordinates noun-phrase extraction and edge-weighted graph construction to enable principled noun-graph representations of textual data.

## Functions

- [`_extract_edges`](../api/functions/graphrag-index-operations-build-noun-graph-build-noun-graph-extract-edges)
- [`extract`](../api/functions/graphrag-index-operations-build-noun-graph-build-noun-graph-extract)
- [`_extract_nodes`](../api/functions/graphrag-index-operations-build-noun-graph-build-noun-graph-extract-nodes)
- [`build_noun_graph`](../api/functions/graphrag-index-operations-build-noun-graph-build-noun-graph-build-noun-graph)

