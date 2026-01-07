---
sidebar_position: 60
---

# graphrag/index/operations/compute_edge_combined_degree.py

## Overview

Utilities to compute and attach node degree information to edges and to compute per-edge combined degree.

Purpose:
This module provides helpers to augment edge data with node degree information and to compute a per-edge combined degree using node degrees.

Key exports:
- _degree_colname(column: str) -&gt; str: Return the degree column name derived from the given column.
- join_to_degree(df: pd.DataFrame, column: str) -&gt; pd.DataFrame: Join the input DataFrame with the node degree information for the specified column and return the result augmented with a degree column. Returns a DataFrame with an additional column named '&lt;column&gt;_degree' containing the degree values; missing degrees are filled with 0.
- compute_edge_combined_degree(edge_df: pd.DataFrame, node_degree_df: pd.DataFrame, node_name_column: str, node_degree_column: str, edge_source_column: str, edge_target_column: str) -&gt; pd.Series: Compute the combined degree for each edge in a graph.

Brief summary:
The module focuses on computing edge-level degree metrics by leveraging node degree data, enabling analyses that rely on combined degree information for graph edges. The utilities are designed to handle missing degree data by defaulting to 0 where necessary.

## Functions

- [`_degree_colname`](../api/functions/graphrag-index-operations-compute-edge-combined-degree-degree-colname)
- [`join_to_degree`](../api/functions/graphrag-index-operations-compute-edge-combined-degree-join-to-degree)
- [`compute_edge_combined_degree`](../api/functions/graphrag-index-operations-compute-edge-combined-degree-compute-edge-combined-degree)

