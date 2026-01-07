---
sidebar_position: 80
---

# graphrag/index/operations/layout_graph/zero.py

## Overview

Utilities to generate a zero-coordinate graph layout as a baseline.

This module provides a minimal layout where all node positions are initialized to zeros. No embedding or projection is performed.

Exports:
- get_zero_positions(node_labels: list[str], node_categories: list[int] | None = None, node_sizes: list[int] | None = None, three_d: bool | None = False) -&gt; list[NodePosition]
  Create zero-coordinate positions for nodes. No embedding or projection is performed; coordinates are initialized to zeros.
- run(graph: nx.Graph, on_error: ErrorHandlerFn) -&gt; GraphLayout
  Compute a zero-coordinate GraphLayout for the given graph, optionally using per-node cluster/category and size hints, and fall back to a default layout if an error occurs.

## Functions

- [`get_zero_positions`](../api/functions/graphrag-index-operations-layout-graph-zero-get-zero-positions)
- [`run`](../api/functions/graphrag-index-operations-layout-graph-zero-run)

