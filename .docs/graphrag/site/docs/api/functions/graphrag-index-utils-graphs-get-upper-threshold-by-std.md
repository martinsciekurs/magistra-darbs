---
sidebar_position: 197
---

# get_upper_threshold_by_std

**File:** `graphrag/index/utils/graphs.py` (lines 238-242)

## Signature

```python
def get_upper_threshold_by_std(data: list[float] | list[int], std_trim: float) -> float
```

## Description

Get upper threshold by standard deviation.

Args:
    data: list[float] | list[int], a list of numeric values used to compute the threshold.
    std_trim: float, multiplier for the standard deviation to offset the mean.

Returns:
    float: The upper threshold computed as mean + std_trim * std of the data.

