---
sidebar_position: 136
---

# _at_level

**File:** `graphrag/index/operations/summarize_communities/graph_context/context_builder.py` (lines 269-271)

## Signature

```python
def _at_level(level: int, df: pd.DataFrame) -> pd.DataFrame
```

## Description

Return records at the given level.

Args:
    level: The level to filter by (int).
    df: DataFrame containing community records, expected to have a COMMUNITY_LEVEL column.

Returns:
    pd.DataFrame: A DataFrame containing only records where COMMUNITY_LEVEL equals level.

Raises:
    KeyError: If the COMMUNITY_LEVEL column is not present in df.

## Dependencies

This function calls:

- `graphrag/index/utils/dataframes.py::where_column_equals`

## Called By

This function is called by:

- `graphrag/index/operations/summarize_communities/graph_context/context_builder.py::_get_subcontext_df`
- `graphrag/index/operations/summarize_communities/graph_context/context_builder.py::_get_community_df`

