---
sidebar_position: 141
---

# _get_community_df

**File:** `graphrag/index/operations/summarize_communities/graph_context/context_builder.py` (lines 318-362)

## Signature

```python
def _get_community_df(
    level: int,
    invalid_context_df: pd.DataFrame,
    sub_context_df: pd.DataFrame,
    community_hierarchy_df: pd.DataFrame,
    tokenizer: Tokenizer,
    max_context_tokens: int,
) -> pd.DataFrame
```

## Description

Get community context for each community.

Args:
  level: The level to process.
  invalid_context_df: DataFrame containing IDs of communities considered invalid at this level.
  sub_context_df: DataFrame containing sub-community context data for each community.
  community_hierarchy_df: DataFrame representing the community hierarchy from which communities at the given level are selected.
  tokenizer: Tokenizer used to build and trim mixed context strings.
  max_context_tokens: Maximum number of tokens allowed for the resulting context.

Returns:
  pd.DataFrame: DataFrame containing one row per community at the specified level, including:
    - COMMUNITY_ID
    - ALL_CONTEXT: a list of dictionaries with keys SUB_COMMUNITY, ALL_CONTEXT, FULL_CONTENT, CONTEXT_SIZE
    - CONTEXT_STRING: mixed context string built from ALL_CONTEXT
    - COMMUNITY_LEVEL: the level value

Raises:
  KeyError: If required columns are missing from the input DataFrames.

## Dependencies

This function calls:

- `graphrag/index/operations/summarize_communities/graph_context/context_builder.py::_at_level`
- `graphrag/index/operations/summarize_communities/graph_context/context_builder.py::_build_mixed_context`
- `graphrag/index/operations/summarize_communities/graph_context/context_builder.py::_drop_community_level`
- `graphrag/index/utils/dataframes.py::join`
- `graphrag/index/utils/dataframes.py::select`

## Called By

This function is called by:

- `graphrag/index/operations/summarize_communities/graph_context/context_builder.py::build_level_context`

