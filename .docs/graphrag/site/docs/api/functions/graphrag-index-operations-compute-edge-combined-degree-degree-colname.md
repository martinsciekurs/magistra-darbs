---
sidebar_position: 83
---

# _degree_colname

**File:** `graphrag/index/operations/compute_edge_combined_degree.py` (lines 42-43)

## Signature

```python
def _degree_colname(column: str) -> str
```

## Description

Return the degree column name derived from the given column.

Args:
    column: The original column name.

Returns:
    The degree column name as a string, formed by appending '_degree' to the input column name.

## Example 💡 Generated

```python
from module import _degree_colname
column = "score" 
degree = _degree_colname(column)  # -> "score_degree" 
print(degree)
```

## Called By

This function is called by:

- `graphrag/index/operations/compute_edge_combined_degree.py::compute_edge_combined_degree`
- `graphrag/index/operations/compute_edge_combined_degree.py::join_to_degree`

