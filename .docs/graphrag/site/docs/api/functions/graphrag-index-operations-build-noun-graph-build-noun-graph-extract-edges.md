---
sidebar_position: 61
---

# _extract_edges

**File:** `graphrag/index/operations/build_noun_graph/build_noun_graph.py` (lines 92-140)

## Signature

```python
def _extract_edges(
    nodes_df: pd.DataFrame,
    normalize_edge_weights: bool = True,
) -> pd.DataFrame
```

## Description

Extract edges between nodes by linking nouns that co-occur in the same text unit.

Nodes that appear in the same text unit are connected. If normalize_edge_weights is True, PMI-based weights are computed via calculate_pmi_edge_weights.

Args:
  nodes_df (pd.DataFrame): DataFrame containing node information with columns including id, title, frequency, and text_unit_ids.
  normalize_edge_weights (bool): If True, PMI-based weights are computed instead of raw counts. Default: True.

Returns:
  pd.DataFrame: Edges DataFrame with columns [source, target, weight, text_unit_ids].

## Dependencies

This function calls:

- `graphrag/index/utils/graphs.py::calculate_pmi_edge_weights`

## Called By

This function is called by:

- `graphrag/index/operations/build_noun_graph/build_noun_graph.py::build_noun_graph`

