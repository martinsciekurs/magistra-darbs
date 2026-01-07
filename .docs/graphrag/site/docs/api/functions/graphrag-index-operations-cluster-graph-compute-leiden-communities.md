---
sidebar_position: 80
---

# _compute_leiden_communities

**File:** `graphrag/index/operations/cluster_graph.py` (lines 57-80)

## Signature

```python
def _compute_leiden_communities(
    graph: nx.Graph | nx.DiGraph,
    max_cluster_size: int,
    use_lcc: bool,
    seed: int | None = None,
) -> tuple[dict[int, dict[str, int]], dict[int, int]]
```

## Description

Compute Leiden root communities for a graph and return level wise node to community mappings and a cluster hierarchy.

Args:
    graph: nx.Graph | nx.DiGraph
        Input graph from which to compute Leiden communities. If use_lcc is True, the graph's largest connected component is used.
    max_cluster_size: int
        Maximum size of a cluster allowed by Leiden algorithm.
    use_lcc: bool
        If True, compute on the largest connected component of the input graph.
    seed: int | None
        Random seed for reproducibility in the Leiden clustering.

Returns:
    tuple[dict[int, dict[str, int]], dict[int, int]]
        A tuple containing:
        - node_id_to_community_map: dict[int, dict[str, int]]
            Mapping from level to a dictionary that maps node_id to its community id.
        - parent_mapping: dict[int, int]
            Mapping from cluster_id to its parent cluster id, or -1 if there is no parent.

Raises:
    Propagates exceptions from the underlying libraries or graph processing steps; there are no explicit raises documented for this function.

## Dependencies

This function calls:

- `graphrag/index/utils/stable_lcc.py::stable_largest_connected_component`

## Called By

This function is called by:

- `graphrag/index/operations/cluster_graph.py::cluster_graph`

