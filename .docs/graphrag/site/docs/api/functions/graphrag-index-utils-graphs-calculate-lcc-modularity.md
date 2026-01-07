---
sidebar_position: 203
---

# calculate_lcc_modularity

**File:** `graphrag/index/utils/graphs.py` (lines 62-76)

## Signature

```python
def calculate_lcc_modularity(
    graph: nx.Graph,
    max_cluster_size: int = 10,
    random_seed: int = 0xDEADBEEF,
    use_root_modularity: bool = True,
) -> float
```

## Description

Calculate modularity of the largest connected component of the graph.

Args:
    graph (nx.Graph): The input graph.
    max_cluster_size (int): Maximum cluster size for the root/leaf hierarchical clustering used to compute modularity.
    random_seed (int): Seed for random number generation.
    use_root_modularity (bool): If True, compute modularity using root-level clustering; otherwise compute using leaf-level clustering.

Returns:
    float: The modularity value of the largest connected component of the input graph.

## Dependencies

This function calls:

- `graphrag/index/utils/graphs.py::calculate_leaf_modularity`
- `graphrag/index/utils/graphs.py::calculate_root_modularity`

## Called By

This function is called by:

- `graphrag/index/utils/graphs.py::calculate_modularity`

