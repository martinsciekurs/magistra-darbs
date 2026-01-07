---
sidebar_position: 138
---

# _get_subcontext_df

**File:** `graphrag/index/operations/summarize_communities/graph_context/context_builder.py` (lines 305-315)

## Signature

```python
def _get_subcontext_df(
    level: int, report_df: pd.DataFrame, local_context_df: pd.DataFrame
) -> pd.DataFrame
```

## Description

Get sub-community context for each community.

Args:
    level: int
        The level to extract sub-context for.
    report_df: pd.DataFrame
        DataFrame containing the reports for communities at the given level.
    local_context_df: pd.DataFrame
        DataFrame containing local context information for communities.

Returns:
    pd.DataFrame
        DataFrame containing sub-context for each community, with COMMUNITY_ID renamed to SUB_COMMUNITY.

Raises:
    KeyError: If the COMMUNITY_LEVEL column is not present in report_df or local_context_df.

## Dependencies

This function calls:

- `graphrag/index/operations/summarize_communities/graph_context/context_builder.py::_at_level`
- `graphrag/index/operations/summarize_communities/graph_context/context_builder.py::_drop_community_level`
- `graphrag/index/utils/dataframes.py::join`

## Called By

This function is called by:

- `graphrag/index/operations/summarize_communities/graph_context/context_builder.py::build_level_context`

