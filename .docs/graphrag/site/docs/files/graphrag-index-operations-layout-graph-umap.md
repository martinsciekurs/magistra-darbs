---
sidebar_position: 79
---

# graphrag/index/operations/layout_graph/umap.py

## Overview

UMAP-based layout for graphs using node embeddings.

This module provides a UMAP-based approach to compute 2D (or 3D) layouts for graphs by projecting node embeddings with UMAP and mapping the results to graph node locations. It also includes a fallback layout mechanism in case the UMAP computation fails.

Functions
  _filter_raw_embeddings(embeddings): Filter out None entries from the input node embeddings mapping.
    Args:
      embeddings: NodeEmbeddings - Mapping of node identifiers to embedding vectors; may contain None values.
    Returns:
      NodeEmbeddings - A new mapping with all entries whose embeddings are not None.

  compute_umap_positions(
    embedding_vectors,
    node_labels,
    node_categories=None,
    node_sizes=None,
    min_dist=0.75,
    n_neighbors=5,
    spread=1,
    metric="euclidean",
    n_components=2,
    random_state=86,
  ) -&gt; list[NodePosition]: Project embedding vectors down to 2D/3D coordinates using UMAP.
    Args:
      embedding_vectors: Embedding vectors to project, provided as a numpy array.
      node_labels: Labels for each node.
      node_categories: Optional per-node category identifiers. If None, defaults to 1 for all nodes.
      node_sizes: Optional per-node sizes. If None, defaults to 1 for all nodes.
      min_dist: UMAP min_dist hyperparameter.
      n_neighbors: UMAP n_neighbors hyperparameter.
      spread: UMAP spread hyperparameter.
      metric: Distance metric for UMAP.
      n_components: Number of output dimensions (2 or 3).
      random_state: Random seed.
    Returns:
      list[NodePosition] - The computed positions containing x, y (and optional z) coordinates along with metadata such as label, size, and cluster.

  run(
    graph: nx.Graph,
    embeddings: NodeEmbeddings,
    on_error: ErrorHandlerFn,
  ) -&gt; GraphLayout: Compute a UMAP-based layout for the given graph using node embeddings and optional per-node attributes, with a fallback layout if the UMAP computation fails.
    Args:
      graph: nx.Graph - The input graph. Nodes may have attributes such as cluster (or community) and degree (or size) that are used to influence the layout.
      embeddings: NodeEmbeddings - Mapping of node identifiers to embedding vectors.
      on_error: ErrorHandlerFn - Callback invoked on error to handle/log failures.
    Returns:
      GraphLayout - The computed layout including positions and metadata.

Summary
- The layout uses NodePosition entries (with fields x, y, label, size, cluster) to describe node placements and attributes.
- A top-level fallback layout is used if UMAP fails, ensuring robust graph visualization.

## Functions

- [`_filter_raw_embeddings`](../api/functions/graphrag-index-operations-layout-graph-umap-filter-raw-embeddings)
- [`compute_umap_positions`](../api/functions/graphrag-index-operations-layout-graph-umap-compute-umap-positions)
- [`run`](../api/functions/graphrag-index-operations-layout-graph-umap-run)

