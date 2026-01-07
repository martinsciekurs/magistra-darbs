---
sidebar_position: 81
---

# graphrag/index/operations/prune_graph.py

## Overview

Prune graphs by filtering nodes and edges based on frequency, degree, and edge weights.

This module implements two primary utilities for pruning: _get_upper_threshold_by_std and prune_graph. The functions operate on networkx graphs and rely on numpy for statistics and graspologic for graph manipulation.

Functions
_get_upper_threshold_by_std
    Get upper threshold by standard deviation.
    Args:
        data: list[float] | list[int], a list of numeric values used to compute the threshold.
        std_trim: float, multiplier for the standard deviation to offset the mean.
    Returns:
        float: The upper threshold computed as mean + std_trim * std of the data.

prune_graph
    Prune graph by removing nodes that are out of frequency/degree ranges and edges with low weights.
    Args:
        graph: nx.Graph, The graph to prune.
        min_node_freq: int, Minimum node frequency threshold; nodes with frequency below this value are removed.
        max_node_freq_std: float | None, If provided, upper threshold is mean + max_node_freq_std * std of node frequencies; nodes with frequency above this threshold will be pruned.
        min_node_degree: int, Minimum node degree threshold; nodes with degree below this value are removed.
        max_node_degree_std: float | None, If provided, upper threshold is mean + max_node_degree_std * std of node degrees; nodes with degree above this threshold will be pruned.
        min_edge_weight_pct: float, Minimum edge weight percentage to retain; edges with weight below this threshold will be removed.
        remove_ego_nodes: bool, If True, remove ego (isolated) nodes as part of pruning.
        lcc_only: bool, If True, prune only within the largest connected component.
    Returns:
        nx.Graph: The pruned graph.

## Functions

- [`_get_upper_threshold_by_std`](../api/functions/graphrag-index-operations-prune-graph-get-upper-threshold-by-std)
- [`prune_graph`](../api/functions/graphrag-index-operations-prune-graph-prune-graph)

