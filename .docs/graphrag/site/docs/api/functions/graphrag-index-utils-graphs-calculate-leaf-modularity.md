---
sidebar_position: 200
---

# calculate_leaf_modularity

**File:** `graphrag/index/utils/graphs.py` (lines 33-43)

## Signature

```python
def calculate_leaf_modularity(
    graph: nx.Graph,
    max_cluster_size: int = 10,
    random_seed: int = 0xDEADBEEF,
) -> float
```

## Description

Compute the modularity score of the graph using the leaf-level partition produced by hierarchical Leiden. The function applies hierarchical Leiden to the input graph, derives the leaf-level clustering via final_level_hierarchical_clustering, and returns the modularity of the graph with respect to that partition.

Args:
    graph (nx.Graph): The input graph.
    max_cluster_size (int): Maximum size of clusters considered during hierarchical Leiden.
    random_seed (int): Seed for random number generation to ensure reproducibility.

Returns:
    float: The modularity score of the graph computed using the leaf-cluster partition.

Raises:
    None

## Called By

This function is called by:

- `graphrag/index/utils/graphs.py::calculate_graph_modularity`
- `graphrag/index/utils/graphs.py::calculate_lcc_modularity`
- `graphrag/index/utils/graphs.py::calculate_weighted_modularity`

