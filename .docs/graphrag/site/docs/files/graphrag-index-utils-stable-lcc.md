---
sidebar_position: 114
---

# graphrag/index/utils/stable_lcc.py

## Overview

Utilities to stabilize graphs and compute a stable largest connected component for reproducible analyses.

Summary:
This module provides helpers to sort edges canonically, generate edge keys, normalize node names, stabilize graphs to deterministic representations, and compute the largest connected component in a stable, repeatable way.

Key exports:
- _sort_source_target(edge): Sorts a graph edge so that the source and target are in a stable, canonical order.
- _get_edge_key(source: Any, target: Any) -&gt; str: Returns a string key for the edge in the format 'source -&gt; target'.
- normalize_node_names(graph: nx.Graph | nx.DiGraph) -&gt; nx.Graph | nx.DiGraph: Normalize node names by HTML unescaping, converting to uppercase, and trimming whitespace on each node label.
- _stabilize_graph(graph: nx.Graph) -&gt; nx.Graph: Ensure an undirected graph with the same relationships will always be read the same way; preserves directedness and returns a new graph with deterministic ordering of nodes and edges.
- stable_largest_connected_component(graph: nx.Graph) -&gt; nx.Graph: Return the largest connected component with deterministic ordering of nodes and edges.

## Functions

- [`_sort_source_target`](../api/functions/graphrag-index-utils-stable-lcc-sort-source-target)
- [`_get_edge_key`](../api/functions/graphrag-index-utils-stable-lcc-get-edge-key)
- [`normalize_node_names`](../api/functions/graphrag-index-utils-stable-lcc-normalize-node-names)
- [`_stabilize_graph`](../api/functions/graphrag-index-utils-stable-lcc-stabilize-graph)
- [`stable_largest_connected_component`](../api/functions/graphrag-index-utils-stable-lcc-stable-largest-connected-component)

