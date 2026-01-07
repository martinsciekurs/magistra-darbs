---
sidebar_position: 81
---

# cluster_graph

**File:** `graphrag/index/operations/cluster_graph.py` (lines 19-53)

## Signature

```python
def cluster_graph(
    graph: nx.Graph,
    max_cluster_size: int,
    use_lcc: bool,
    seed: int | None = None,
) -> Communities
```

## Description

Compute hierarchical Leiden-based clusters for the input graph and return them as a list of (level, cluster_id, parent_cluster_id, nodes).

Args:
    graph: nx.Graph
        Input graph on which to perform clustering.
    max_cluster_size: int
        Maximum size of a cluster allowed by Leiden algorithm.
    use_lcc: bool
        If True, operate on the largest connected component of the input graph.
    seed: int | None
        Random seed for reproducibility of the clustering process.

Returns:
    Communities
        A list of tuples (level, cluster_id, parent_cluster_id, nodes) describing the
        clusters found at different hierarchical levels, the cluster's parent, and the
        member node identifiers.

## Dependencies

This function calls:

- `graphrag/index/operations/cluster_graph.py::_compute_leiden_communities`

## Called By

This function is called by:

- `graphrag/index/workflows/create_communities.py::create_communities`

