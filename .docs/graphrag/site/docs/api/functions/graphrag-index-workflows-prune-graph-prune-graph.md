---
sidebar_position: 256
---

# prune_graph

**File:** `graphrag/index/workflows/prune_graph.py` (lines 53-82)

## Signature

```python
def prune_graph(
    entities: pd.DataFrame,
    relationships: pd.DataFrame,
    pruning_config: PruneGraphConfig,
) -> tuple[pd.DataFrame, pd.DataFrame]
```

## Description

Prune a full graph based on graph statistics.

Args:
    entities (pd.DataFrame): DataFrame of entity nodes used to construct the graph. Must include a 'title' column to identify nodes.
    relationships (pd.DataFrame): DataFrame of relationships/edges. Must include 'source' and 'target' columns. May include a 'weight' column used as an edge attribute during pruning.
    pruning_config (PruneGraphConfig): Configuration object containing pruning parameters such as min_node_freq, max_node_freq_std, min_node_degree, max_node_degree_std, min_edge_weight_pct, remove_ego_nodes, and lcc_only.

Returns:
    tuple[pd.DataFrame, pd.DataFrame]: A tuple containing the pruned entities and pruned relationships as DataFrames. These DataFrames are subsets of the input DataFrames corresponding to the pruned graph.

Raises:
    Propagates exceptions from the underlying graph construction and pruning operations (e.g., due to invalid input data or missing required columns).

## Dependencies

This function calls:

- `graphrag/index/operations/create_graph.py::create_graph`
- `graphrag/index/operations/graph_to_dataframes.py::graph_to_dataframes`

