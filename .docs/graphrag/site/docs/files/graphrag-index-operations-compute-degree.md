---
sidebar_position: 59
---

# graphrag/index/operations/compute_degree.py

## Overview

Compute the degree of each node in a NetworkX graph and return a pandas DataFrame.

Purpose
Provide a utility to compute node degrees from a Graph and present them in a tabular format for downstream processing.

Key exports
- compute_degree(graph: nx.Graph) -&gt; pd.DataFrame: Creates a DataFrame with one row per node, containing the columns:
  - title: the node identifier
  - degree: the degree of the node as an integer

Brief summary
Given a NetworkX graph, compute_degree returns a DataFrame listing each node's identifier and its degree.

## Functions

- [`compute_degree`](../api/functions/graphrag-index-operations-compute-degree-compute-degree)

