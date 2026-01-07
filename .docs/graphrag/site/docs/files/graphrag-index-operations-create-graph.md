---
sidebar_position: 61
---

# graphrag/index/operations/create_graph.py

## Overview

Utilities to construct NetworkX graphs from tabular data.

Purpose:
Provide a simple API to build a NetworkX Graph from a pandas DataFrame of edges and an optional DataFrame of node attributes. The function supports optional edge attributes and a node identifier column parameter.

Key exports:
- create_graph: Build a NetworkX Graph from edges and optional nodes DataFrames.

Summary:
This module defines create_graph(edges, edge_attr=None, nodes=None, node_id='title') -&gt; nx.Graph which returns a NetworkX graph constructed from the provided edges and optional node attributes.

## Functions

- [`create_graph`](../api/functions/graphrag-index-operations-create-graph-create-graph)

