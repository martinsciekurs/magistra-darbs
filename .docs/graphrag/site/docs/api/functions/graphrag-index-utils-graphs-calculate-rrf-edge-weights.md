---
sidebar_position: 201
---

# calculate_rrf_edge_weights

**File:** `graphrag/index/utils/graphs.py` (lines 204-235)

## Signature

```python
def calculate_rrf_edge_weights(
    nodes_df: pd.DataFrame,
    edges_df: pd.DataFrame,
    node_name_col="title",
    node_freq_col="freq",
    edge_weight_col="weight",
    edge_source_col="source",
    edge_target_col="target",
    rrf_smoothing_factor: int = 60,
) -> pd.DataFrame
```

## Description

Calculate reciprocal rank fusion (RRF) edge weights as a combination of PMI weight and combined freq of source and target.

Args:
    nodes_df (pd.DataFrame): DataFrame containing node information with at least the columns specified by node_name_col and node_freq_col.
    edges_df (pd.DataFrame): DataFrame containing edge information with at least the columns specified by edge_weight_col, edge_source_col, and edge_target_col.
    node_name_col (str): Column in nodes_df that identifies the node name. Default "title".
    node_freq_col (str): Column in nodes_df that indicates node frequency. Default "freq".
    edge_weight_col (str): Column in edges_df that holds edge weights (PMI) before RRF adjustment. Default "weight".
    edge_source_col (str): Column in edges_df that indicates the source node. Default "source".
    edge_target_col (str): Column in edges_df that indicates the target node. Default "target".
    rrf_smoothing_factor (int): Smoothing factor used in reciprocal rank fusion. Default 60.

Returns:
    pd.DataFrame: Edge dataframe with edge weights updated using the RRF formula. It first computes PMI-based weights, ranks them, and then combines the ranks to produce the new weight. The resulting DataFrame retains edge information and the updated weight column.

Raises:
    Not documented in the provided data.

## Dependencies

This function calls:

- `graphrag/index/utils/graphs.py::calculate_pmi_edge_weights`

