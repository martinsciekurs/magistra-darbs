---
sidebar_position: 82
---

# compute_degree

**File:** `graphrag/index/operations/compute_degree.py` (lines 10-15)

## Signature

```python
def compute_degree(graph: nx.Graph) -> pd.DataFrame
```

## Description

Create a new DataFrame with the degree of each node in the graph.

Args:
    graph (nx.Graph): NetworkX graph from which to compute node degrees.

Returns:
    pd.DataFrame: DataFrame with one row per node, containing the columns:
        title: the node identifier
        degree: the degree of the node as an integer.

## Called By

This function is called by:

- `graphrag/index/operations/finalize_entities.py::finalize_entities`
- `graphrag/index/operations/finalize_relationships.py::finalize_relationships`

