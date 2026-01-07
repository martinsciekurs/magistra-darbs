---
sidebar_position: 130
---

# prune_graph

**File:** `graphrag/index/operations/prune_graph.py` (lines 18-83)

## Signature

```python
def prune_graph(
    graph: nx.Graph,
    min_node_freq: int = 1,
    max_node_freq_std: float | None = None,
    min_node_degree: int = 1,
    max_node_degree_std: float | None = None,
    min_edge_weight_pct: float = 40,
    remove_ego_nodes: bool = False,
    lcc_only: bool = False,
) -> nx.Graph
```

## Description

Prune graph by removing nodes that are out of frequency/degree ranges and edges with low weights.

Args:
    graph (nx.Graph): The graph to prune.
    min_node_freq (int): Minimum node frequency threshold; nodes with frequency below this value are removed.
    max_node_freq_std (float | None): If provided, upper threshold is mean + max_node_freq_std * std of node frequencies; nodes with frequency above this threshold are removed.
    min_node_degree (int): Minimum degree threshold; nodes with degree below this value are removed.
    max_node_degree_std (float | None): If provided, upper threshold is mean + max_node_degree_std * std of node degrees; nodes with degree above this threshold are removed.
    min_edge_weight_pct (float): Percentile for edge weights; edges with weight below this percentile are removed.
    remove_ego_nodes (bool): If True, remove the ego node (the node with the highest degree) before pruning.
    lcc_only (bool): If True, return only the largest connected component of the pruned graph.

Returns:
    nx.Graph: The pruned graph. If lcc_only is True, returns the largest connected component of the pruned graph.

## Dependencies

This function calls:

- `graphrag/index/operations/prune_graph.py::_get_upper_threshold_by_std`

## Called By

This function is called by:

- `graphrag/index/workflows/prune_graph.py::run_workflow`

