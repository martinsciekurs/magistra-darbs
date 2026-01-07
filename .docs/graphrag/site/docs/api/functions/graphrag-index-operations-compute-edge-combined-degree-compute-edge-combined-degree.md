---
sidebar_position: 85
---

# compute_edge_combined_degree

**File:** `graphrag/index/operations/compute_edge_combined_degree.py` (lines 11-39)

## Signature

```python
def compute_edge_combined_degree(
    edge_df: pd.DataFrame,
    node_degree_df: pd.DataFrame,
    node_name_column: str,
    node_degree_column: str,
    edge_source_column: str,
    edge_target_column: str,
) -> pd.Series
```

## Description

Compute the combined degree for each edge in a graph.

Args:
    edge_df: pd.DataFrame
        The DataFrame containing edges with columns for source and target nodes.
    node_degree_df: pd.DataFrame
        DataFrame containing node degree information, keyed by node name.
    node_name_column: str
        The column in node_degree_df that contains node names to join on.
    node_degree_column: str
        The column in node_degree_df that contains the degree values to join.
    edge_source_column: str
        The column name in edge_df that identifies the source node for each edge.
    edge_target_column: str
        The column name in edge_df that identifies the target node for each edge.

Returns:
    pd.Series
        A Series of the per-edge combined degree values (sum of the source and target node degrees; missing degrees are treated as 0).

Raises:
    Propagates exceptions raised by pandas operations or invalid inputs.

## Dependencies

This function calls:

- `graphrag/index/operations/compute_edge_combined_degree.py::_degree_colname`
- `graphrag/index/operations/compute_edge_combined_degree.py::join_to_degree`

## Called By

This function is called by:

- `graphrag/index/operations/finalize_relationships.py::finalize_relationships`

