---
sidebar_position: 134
---

# _drop_community_level

**File:** `graphrag/index/operations/summarize_communities/graph_context/context_builder.py` (lines 264-266)

## Signature

```python
def _drop_community_level(df: pd.DataFrame) -> pd.DataFrame
```

## Description

Drop the community level column from the dataframe.

Args:
    df (pd.DataFrame): The DataFrame from which to drop the community level column.

Returns:
    pd.DataFrame: The DataFrame with the COMMUNITY_LEVEL column dropped.

Raises:
    KeyError: If the COMMUNITY_LEVEL column does not exist in df.

## Dependencies

This function calls:

- `graphrag/index/utils/dataframes.py::drop_columns`

## Called By

This function is called by:

- `graphrag/index/operations/summarize_communities/graph_context/context_builder.py::_get_subcontext_df`
- `graphrag/index/operations/summarize_communities/graph_context/context_builder.py::_get_community_df`

