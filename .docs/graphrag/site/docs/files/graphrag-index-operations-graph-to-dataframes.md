---
sidebar_position: 76
---

# graphrag/index/operations/graph_to_dataframes.py

## Overview

Utilities to deconstruct a NetworkX graph into Pandas DataFrames.

Purpose:
This module provides a function to deconstruct an nx.Graph into two Pandas DataFrames: one describing nodes and one describing edges.

Key exports:
- graph_to_dataframes(graph, node_columns=None, edge_columns=None, node_id="title") -&gt; tuple[pd.DataFrame, pd.DataFrame]

Summary:
The graph_to_dataframes function accepts a NetworkX graph and optional lists of node and edge attribute columns to include in the respective DataFrames. It returns a tuple containing the nodes DataFrame and the edges DataFrame. The nodes DataFrame uses the specified node_id as the identifier column and may include the selected node attributes; the edges DataFrame includes the selected edge attributes.

## Functions

- [`graph_to_dataframes`](../api/functions/graphrag-index-operations-graph-to-dataframes-graph-to-dataframes)

