---
sidebar_position: 135
---

# _antijoin_reports

**File:** `graphrag/index/operations/summarize_communities/graph_context/context_builder.py` (lines 274-276)

## Signature

```python
def _antijoin_reports(df: pd.DataFrame, reports: pd.DataFrame) -> pd.DataFrame
```

## Description

Return records in df that are not in reports.

Args:
    df: The DataFrame to apply the exclusion to.
    reports: The DataFrame containing rows to remove from df.

Returns:
    pd.DataFrame: The rows from df whose COMMUNITY_ID value is not present in reports.

## Dependencies

This function calls:

- `graphrag/index/utils/dataframes.py::antijoin`

## Called By

This function is called by:

- `graphrag/index/operations/summarize_communities/graph_context/context_builder.py::build_level_context`

