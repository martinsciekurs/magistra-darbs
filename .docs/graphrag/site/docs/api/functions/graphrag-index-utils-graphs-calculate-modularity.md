---
sidebar_position: 205
---

# calculate_modularity

**File:** `graphrag/index/utils/graphs.py` (lines 117-152)

## Signature

```python
def calculate_modularity(
    graph: nx.Graph,
    max_cluster_size: int = 10,
    random_seed: int = 0xDEADBEEF,
    use_root_modularity: bool = True,
    modularity_metric: ModularityMetric = ModularityMetric.WeightedComponents,
) -> float
```

## Description

Calculate modularity of the graph based on the modularity metric type.

Args:
    graph (nx.Graph): The input graph.
    max_cluster_size (int): Maximum cluster size for the root-level clustering produced by Hierarchical Leiden.
    random_seed (int): Seed for random number generation.
    use_root_modularity (bool): If True, compute modularity using root-level clustering; otherwise compute using leaf-level clustering.
    modularity_metric (ModularityMetric): The modularity metric to use (Graph, LCC, or WeightedComponents).

Returns:
    float: The modularity value for the graph with respect to the chosen clustering.

Raises:
    ValueError: If an unknown modularity metric type is provided.

## Dependencies

This function calls:

- `graphrag/index/utils/graphs.py::calculate_graph_modularity`
- `graphrag/index/utils/graphs.py::calculate_lcc_modularity`
- `graphrag/index/utils/graphs.py::calculate_weighted_modularity`

