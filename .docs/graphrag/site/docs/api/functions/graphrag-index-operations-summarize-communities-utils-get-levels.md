---
sidebar_position: 158
---

# get_levels

**File:** `graphrag/index/operations/summarize_communities/utils.py` (lines 11-17)

## Signature

```python
def get_levels(
    df: pd.DataFrame, level_column: str = schemas.COMMUNITY_LEVEL
) -> list[int]
```

## Description

Get the levels of the communities.

Args:
    df (pd.DataFrame): The data frame containing community data.
    level_column (str): The name of the column that contains the level values. Defaults to schemas.COMMUNITY_LEVEL.

Returns:
    list[int]: A list of integer levels in descending order, with -1 and NaN values ignored.

Raises:
    KeyError: If level_column is not a column in df.

## Called By

This function is called by:

- `graphrag/index/operations/summarize_communities/graph_context/context_builder.py::build_local_context`
- `graphrag/index/operations/summarize_communities/summarize_communities.py::summarize_communities`

