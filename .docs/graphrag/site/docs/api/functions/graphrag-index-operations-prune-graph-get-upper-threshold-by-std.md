---
sidebar_position: 129
---

# _get_upper_threshold_by_std

**File:** `graphrag/index/operations/prune_graph.py` (lines 86-92)

## Signature

```python
def _get_upper_threshold_by_std(
    data: list[float] | list[int], std_trim: float
) -> float
```

## Description

Get upper threshold by standard deviation.

Args:
    data: list[float] | list[int], a list of numeric values used to compute the threshold.
    std_trim: float, multiplier for the standard deviation to offset the mean.

Returns:
    float: The upper threshold computed as mean + std_trim * std of the data.

## Example 💡 Generated

```python
from module import _get_upper_threshold_by_std
data = [1.0, 2.5, 3.0, 4.2, 5.5]
std_trim = 1.0
upper_threshold = _get_upper_threshold_by_std(
    data, std_trim)  # e.g., ~4.77
```

## Called By

This function is called by:

- `graphrag/index/operations/prune_graph.py::prune_graph`

