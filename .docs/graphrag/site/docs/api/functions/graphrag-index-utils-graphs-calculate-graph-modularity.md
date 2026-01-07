---
sidebar_position: 202
---

# calculate_graph_modularity

**File:** `graphrag/index/utils/graphs.py` (lines 46-59)

## Signature

```python
def calculate_graph_modularity(
    graph: nx.Graph,
    max_cluster_size: int = 10,
    random_seed: int = 0xDEADBEEF,
    use_root_modularity: bool = True,
) -> float
```

## Description

Calculate modularity of the whole graph.

Args:
    graph (nx.Graph): The input graph.
    max_cluster_size (int): Maximum cluster size for the root-level clustering produced by Hierarchical Leiden.
    random_seed (int): Seed for random number generation.
    use_root_modularity (bool): If True, compute modularity using root-level clustering; otherwise compute using leaf-level clustering.

Returns:
    float: The modularity score for the graph with respect to the chosen clustering.

## Dependencies

This function calls:

- `graphrag/index/utils/graphs.py::calculate_leaf_modularity`
- `graphrag/index/utils/graphs.py::calculate_root_modularity`

## Called By

This function is called by:

- `graphrag/index/utils/graphs.py::calculate_modularity`

