---
sidebar_position: 154
---

# build_level_context

**File:** `graphrag/index/operations/summarize_communities/text_unit_context/context_builder.py` (lines 85-235)

## Signature

```python
def build_level_context(
    report_df: pd.DataFrame | None,
    community_hierarchy_df: pd.DataFrame,
    local_context_df: pd.DataFrame,
    level: int,
    tokenizer: Tokenizer,
    max_context_tokens: int = 16000,
) -> pd.DataFrame
```

## Description

Prep context for each community in a given level.

For each community:
- Check if local context fits within the limit, if yes use local context
- If local context exceeds the limit, iteratively replace local context with sub-community reports, starting from the biggest sub-community

Args:
    report_df: pd.DataFrame | None
        DataFrame with reports for communities. May be None if no reports are available.
    community_hierarchy_df: pd.DataFrame
        DataFrame describing the community hierarchy.
    local_context_df: pd.DataFrame
        DataFrame containing the local context per community.
    level: int
        The level in the community hierarchy to prepare context for.
    tokenizer: Tokenizer
        Tokenizer used to count tokens and enforce the max_context_tokens limit.
    max_context_tokens: int
        Maximum number of tokens allowed for the resulting context. Defaults to 16000.

Returns:
    pd.DataFrame
        DataFrame containing prepared context for communities at the specified level, with context strings, sizes and exceed flags as computed.

## Dependencies

This function calls:

- `graphrag/index/operations/summarize_communities/build_mixed_context.py::build_mixed_context`
- `graphrag/index/operations/summarize_communities/text_unit_context/sort_context.py::sort_context`

