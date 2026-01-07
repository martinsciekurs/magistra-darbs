---
sidebar_position: 199
---

# calculate_pmi_edge_weights

**File:** `graphrag/index/utils/graphs.py` (lines 155-201)

## Signature

```python
def calculate_pmi_edge_weights(
    nodes_df: pd.DataFrame,
    edges_df: pd.DataFrame,
    node_name_col: str = "title",
    node_freq_col: str = "frequency",
    edge_weight_col: str = "weight",
    edge_source_col: str = "source",
    edge_target_col: str = "target",
) -> pd.DataFrame
```

## Description

Calculate pointwise mutual information (PMI) edge weights for a graph.

Args:
    nodes_df (pd.DataFrame): DataFrame containing node information with at least the columns
        specified by node_name_col and node_freq_col.
    edges_df (pd.DataFrame): DataFrame containing edge information with at least the columns
        specified by edge_weight_col, edge_source_col, and edge_target_col.
    node_name_col (str): Column in nodes_df that identifies the node name.
    node_freq_col (str): Column in nodes_df that contains the frequency/count for each node.
    edge_weight_col (str): Column in edges_df that contains the raw edge weights.
    edge_source_col (str): Column in edges_df that identifies the source node.
    edge_target_col (str): Column in edges_df that identifies the target node.

Returns:
    pd.DataFrame: A DataFrame with PMI-weighted edge weights computed as:
        pmi(x,y) = p(x,y) * log2(p(x,y) / (p(x) * p(y)))
        where p(x,y) = edge_weight(x,y) / total_edge_weights and
        p(x) = freq(x) / total_freq_occurrences. The result is the input edges_df
        with the edge weights updated to the PMI value, and intermediate temporary
        columns removed (prop_weight, source_prop, target_prop).

Raises:
    KeyError: If any of the required columns are missing from the input DataFrames.

## Called By

This function is called by:

- `graphrag/index/operations/build_noun_graph/build_noun_graph.py::_extract_edges`
- `graphrag/index/utils/graphs.py::calculate_rrf_edge_weights`

