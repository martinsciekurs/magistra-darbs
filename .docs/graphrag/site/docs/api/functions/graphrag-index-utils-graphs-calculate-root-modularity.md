---
sidebar_position: 198
---

# calculate_root_modularity

**File:** `graphrag/index/utils/graphs.py` (lines 20-30)

## Signature

```python
def calculate_root_modularity(
    graph: nx.Graph,
    max_cluster_size: int = 10,
    random_seed: int = 0xDEADBEEF,
) -> float
```

## Description

Compute the modularity of the graph's root clusters.

This function applies Hierarchical Leiden to the input graph to generate a hierarchical clustering and then uses the first_level_hierarchical_clustering (root level) to define the root clusters. It returns the modularity of the graph with respect to these root clusters.

Args:
    graph (nx.Graph): The input graph.
    max_cluster_size (int): Maximum cluster size for the root-level clustering produced by Hierarchical Leiden.
    random_seed (int): Seed for the randomized algorithm to ensure reproducibility.

Returns:
    float: The modularity score of the graph computed against its root-level clusters.

Notes:
- The computation operates on the entire graph and does not compare to any target modularity.
- Root clusters are obtained via first_level_hierarchical_clustering; internal steps involve Hierarchical Leiden.

## Called By

This function is called by:

- `graphrag/index/utils/graphs.py::calculate_graph_modularity`
- `graphrag/index/utils/graphs.py::calculate_lcc_modularity`
- `graphrag/index/utils/graphs.py::calculate_weighted_modularity`

