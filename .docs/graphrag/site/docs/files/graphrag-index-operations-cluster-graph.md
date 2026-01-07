---
sidebar_position: 58
---

# graphrag/index/operations/cluster_graph.py

## Overview

Module to compute hierarchical Leiden-based clustering for graphs and expose a user-facing clustering function.

Summary
- This module provides utilities to compute Leiden root communities and a hierarchical cluster representation for a graph. It can operate on the graph's largest connected component when requested. The main user-facing entry point is cluster_graph, which returns a hierarchical list of clusters as (level, cluster_id, parent_cluster_id, nodes).

Key exports
- cluster_graph(graph: nx.Graph, max_cluster_size: int, use_lcc: bool, seed: int | None = None) -&gt; Communities
  Compute hierarchical Leiden-based clusters for the input graph and return them as a list of (level, cluster_id, parent_cluster_id, nodes).
- _compute_leiden_communities(
    graph: nx.Graph | nx.DiGraph,
    max_cluster_size: int,
    use_lcc: bool,
    seed: int | None = None,
  ) -&gt; tuple[dict[int, dict[str, int]], dict[int, int]]
  Internal helper that returns level-wise node-to-community mappings and a cluster hierarchy.

Data types
- Communities: list[tuple[int, int, int, list[str]]]

Raises
- Exceptions from underlying libraries may be raised (e.g., invalid input graph or Leiden computation errors); these should propagate to the caller as appropriate.

## Functions

- [`_compute_leiden_communities`](../api/functions/graphrag-index-operations-cluster-graph-compute-leiden-communities)
- [`cluster_graph`](../api/functions/graphrag-index-operations-cluster-graph-cluster-graph)

