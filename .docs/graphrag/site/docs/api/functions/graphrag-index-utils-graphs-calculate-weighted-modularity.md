---
sidebar_position: 204
---

# calculate_weighted_modularity

**File:** `graphrag/index/utils/graphs.py` (lines 79-114)

## Signature

```python
def calculate_weighted_modularity(
    graph: nx.Graph,
    max_cluster_size: int = 10,
    random_seed: int = 0xDEADBEEF,
    min_connected_component_size: int = 10,
    use_root_modularity: bool = True,
) -> float
```

## Description

Calculate weighted modularity of all connected components with size greater than min_connected_component_size.

Modularity = sum(component_modularity * component_size) / total_nodes.
Modularity for the overall calculation is obtained by weighting each component's modularity by its size and normalizing by the total number of nodes in all considered components.

Args:
  graph (nx.Graph): The input graph.
  max_cluster_size (int): Maximum cluster size for the modularity computations per component.
  random_seed (int): Seed for random number generation.
  min_connected_component_size (int): Components with size less than or equal to this value are ignored; if no components pass this threshold, the entire graph is used.
  use_root_modularity (bool): If True, compute modularity using root-level clustering; otherwise compute leaf-level clustering.

Returns:
  float: The weighted modularity value.

## Dependencies

This function calls:

- `graphrag/index/utils/graphs.py::calculate_leaf_modularity`
- `graphrag/index/utils/graphs.py::calculate_root_modularity`

## Called By

This function is called by:

- `graphrag/index/utils/graphs.py::calculate_modularity`

