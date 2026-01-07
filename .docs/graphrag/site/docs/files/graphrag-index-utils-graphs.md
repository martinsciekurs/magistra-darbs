---
sidebar_position: 111
---

# graphrag/index/utils/graphs.py

## Overview

Graph modularity utilities for computing modularity metrics on graphs using hierarchical Leiden clustering and related edge weighting schemes.

This module exposes utilities to compute modularity at root and leaf levels, generate PMI and reciprocal rank fusion (RRF) edge weights, and aggregate modularity across connected components using a weighted approach. The Modularity metric used for the overall calculation is defined as the weighted average across components: Modularity = sum(component_modularity * component_size) / total_nodes.

Public API (key exports)
- get_upper_threshold_by_std(data, std_trim)
- calculate_root_modularity(graph, max_cluster_size=10, random_seed=0xDEADBEEF)
- calculate_pmi_edge_weights(nodes_df, edges_df, node_name_col="title", node_freq_col="frequency", edge_weight_col="weight", edge_source_col="source", edge_target_col="target")
- calculate_leaf_modularity(graph, max_cluster_size=10, random_seed=0xDEADBEEF)
- calculate_rrf_edge_weights(nodes_df, edges_df, node_name_col="title", node_freq_col="freq", edge_weight_col="weight", edge_source_col="source", edge_target_col="target", rrf_smoothing_factor=60)
- calculate_graph_modularity(graph, max_cluster_size=10, random_seed=0xDEADBEEF, use_root_modularity=True)
- calculate_lcc_modularity(graph, max_cluster_size=10, random_seed=0xDEADBEEF, use_root_modularity=True)
- calculate_weighted_modularity(graph, max_cluster_size=10, random_seed=0xDEADBEEF, min_connected_component_size=10, use_root_modularity=True)
- calculate_modularity(graph, max_cluster_size=10, random_seed=0xDEADBEEF, use_root_modularity=True, modularity_metric=ModularityMetric.WeightedComponents)

Dependencies include networkx, numpy, pandas, and graspologic's hierarchical_leiden and modularity utilities, as well as largest_connected_component, with Modularity defined as above.

## Functions

- [`get_upper_threshold_by_std`](../api/functions/graphrag-index-utils-graphs-get-upper-threshold-by-std)
- [`calculate_root_modularity`](../api/functions/graphrag-index-utils-graphs-calculate-root-modularity)
- [`calculate_pmi_edge_weights`](../api/functions/graphrag-index-utils-graphs-calculate-pmi-edge-weights)
- [`calculate_leaf_modularity`](../api/functions/graphrag-index-utils-graphs-calculate-leaf-modularity)
- [`calculate_rrf_edge_weights`](../api/functions/graphrag-index-utils-graphs-calculate-rrf-edge-weights)
- [`calculate_graph_modularity`](../api/functions/graphrag-index-utils-graphs-calculate-graph-modularity)
- [`calculate_lcc_modularity`](../api/functions/graphrag-index-utils-graphs-calculate-lcc-modularity)
- [`calculate_weighted_modularity`](../api/functions/graphrag-index-utils-graphs-calculate-weighted-modularity)
- [`calculate_modularity`](../api/functions/graphrag-index-utils-graphs-calculate-modularity)

