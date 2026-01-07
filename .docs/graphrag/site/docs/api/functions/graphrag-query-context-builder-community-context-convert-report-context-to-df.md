---
sidebar_position: 327
---

# _convert_report_context_to_df

**File:** `graphrag/query/context_builder/community_context.py` (lines 246-264)

## Signature

```python
def _convert_report_context_to_df(
    context_records: list[list[str]],
    header: list[str],
    weight_column: str | None = None,
    rank_column: str | None = None,
) -> pd.DataFrame
```

## Description

Convert report context records to a pandas DataFrame and sort by weight and rank if provided.

Args:
    context_records (list[list[str]]): The report context records to convert. Each inner list represents a row.
    header (list[str]): Column names for the resulting DataFrame.
    weight_column (str | None): Name of the column to use for weighting. If not None, the column will be cast to float and used for sorting in descending order.
    rank_column (str | None): Name of the column to use for ranking. If not None, the column will be cast to float and used for sorting in descending order.

Returns:
    pd.DataFrame: A DataFrame constructed from the context records with the provided header. If context_records is empty, an empty DataFrame is returned. The DataFrame is sorted in-place by the specified weight and rank columns when provided.

Raises:
    None

## Dependencies

This function calls:

- `graphrag/query/context_builder/community_context.py::_rank_report_context`

## Called By

This function is called by:

- `graphrag/query/context_builder/community_context.py::_cut_batch`

