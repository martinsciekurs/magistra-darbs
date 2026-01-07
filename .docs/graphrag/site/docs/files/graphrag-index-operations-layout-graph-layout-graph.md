---
sidebar_position: 77
---

# graphrag/index/operations/layout_graph/layout_graph.py

## Overview

Utilities to compute and apply layout algorithms to graphs.

Purpose:
This module provides functions to apply a layout algorithm to a graph and obtain node positions, using a UMAP-based layout when enabled and falling back to a Zero layout otherwise.

Key exports:
- _run_layout
- layout_graph

Function descriptions:
- _run_layout(graph: nx.Graph, enabled: bool, embeddings: NodeEmbeddings) -&gt; GraphLayout
  Args:
    graph: The graph to layout.
    enabled: If True, use the UMAP-based layout; otherwise fall back to the Zero layout.
    embeddings: Embeddings for each node in the graph.
  Returns:
    GraphLayout: The resulting layout representation.
- layout_graph(graph: nx.Graph, enabled: bool, embeddings: NodeEmbeddings | None) -&gt; pandas.DataFrame
  Args:
    graph: The nx.Graph to layout.
    enabled: If True, use the UMAP-based layout; otherwise fall back to the Zero layout.
    embeddings: Embeddings for each node in the graph. If None, embeddings are treated as empty.
  Returns:
    pandas.DataFrame: A DataFrame containing node positions.

Brief summary:
Given a graph and optional embeddings, the functions choose an appropriate layout algorithm and return node positions suitable for downstream processing or visualization.
Raises:
Exceptions raised by the underlying layout implementations may propagate (e.g., ValueError, RuntimeError).

## Functions

- [`_run_layout`](../api/functions/graphrag-index-operations-layout-graph-layout-graph-run-layout)
- [`layout_graph`](../api/functions/graphrag-index-operations-layout-graph-layout-graph-layout-graph)

