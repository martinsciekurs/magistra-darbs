---
sidebar_position: 185
---

# transform_series

**File:** `graphrag/index/utils/dataframes.py` (lines 34-36)

## Signature

```python
def transform_series(series: pd.Series, fn: Callable[[Any], Any]) -> pd.Series
```

## Description

Apply a transformation function to a Pandas Series.

Args:
    series: The input Pandas Series to transform.
    fn: A callable that takes a single value and returns a transformed value.

Returns:
    pd.Series: A new Series with the transformed values.

Raises:
    Exception: Any exception raised by fn will be propagated to the caller.

## Called By

This function is called by:

- `graphrag/index/operations/summarize_communities/graph_context/context_builder.py::_sort_and_trim_context`
- `graphrag/index/operations/summarize_communities/graph_context/context_builder.py::_build_mixed_context`

