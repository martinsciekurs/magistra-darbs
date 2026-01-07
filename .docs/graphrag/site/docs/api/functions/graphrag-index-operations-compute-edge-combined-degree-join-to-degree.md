---
sidebar_position: 84
---

# join_to_degree

**File:** `graphrag/index/operations/compute_edge_combined_degree.py` (lines 21-31)

## Signature

```python
def join_to_degree(df: pd.DataFrame, column: str) -> pd.DataFrame
```

## Description

Join the input DataFrame with the node degree information for the specified column and return the result augmented with a degree column.

Args:
  df: The input DataFrame to augment.
  column: The column name in df used to align with the node degree data.

Returns:
  A DataFrame with an additional column named '&lt;column&gt;_degree' containing the degree values; missing degrees are filled with 0.

## Dependencies

This function calls:

- `graphrag/index/operations/compute_edge_combined_degree.py::_degree_colname`

## Called By

This function is called by:

- `graphrag/index/operations/compute_edge_combined_degree.py::compute_edge_combined_degree`

