---
sidebar_position: 322
---

# _rank_report_context

**File:** `graphrag/query/context_builder/community_context.py` (lines 228-243)

## Signature

```python
def _rank_report_context(
    report_df: pd.DataFrame,
    weight_column: str | None = "occurrence weight",
    rank_column: str | None = "rank",
) -> pd.DataFrame
```

## Description

Sorts the report context by the provided weight and rank columns in descending order, in-place.

Args:
  report_df (pd.DataFrame): The DataFrame containing the report context to sort. The function mutates this DataFrame in place by casting the configured columns to float and sorting by them in descending order. If neither weight_column nor rank_column is provided, the DataFrame is returned unchanged.

  weight_column (str | None): Name of the column to use for weighting. If not None, the column is cast to float and used for sorting; defaults to "occurrence weight". If None, this column is ignored.

  rank_column (str | None): Name of the column to use for ranking. If not None, the column is cast to float and used for sorting; defaults to "rank". If None, this column is ignored.

Returns:
  pd.DataFrame: The input DataFrame, sorted by the specified columns in descending order. This is the same object that was passed in.

Raises:
  KeyError: If a provided column name does not exist in report_df.
  ValueError: If a provided column cannot be cast to float.
  TypeError: If an invalid argument type is provided.

## Called By

This function is called by:

- `graphrag/query/context_builder/community_context.py::_convert_report_context_to_df`

