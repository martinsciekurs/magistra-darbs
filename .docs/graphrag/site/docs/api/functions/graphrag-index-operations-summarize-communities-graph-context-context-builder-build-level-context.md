---
sidebar_position: 143
---

# build_level_context

**File:** `graphrag/index/operations/summarize_communities/graph_context/context_builder.py` (lines 191-261)

## Signature

```python
def build_level_context(
    report_df: pd.DataFrame | None,
    community_hierarchy_df: pd.DataFrame,
    local_context_df: pd.DataFrame,
    tokenizer: Tokenizer,
    level: int,
    max_context_tokens: int,
) -> pd.DataFrame
```

## Description

Prepare context for each community at a given level.

This function selects the communities at the specified level from local_context_df, then classifies their local contexts into valid (CONTEXT_EXCEED_FLAG is False) and invalid (CONTEXT_EXCEED_FLAG is True) records. It returns a DataFrame containing the prepared context for that level, including the contextual strings and metadata required for downstream processing. Note that this function may create or update columns such as CONTEXT_STRING, CONTEXT_SIZE, and CONTEXT_EXCEED_FLAG in the resulting DataFrame. The level scoping ensures only communities at the given level are processed.

Processing flow by branch:
- Early return when there are no invalid contexts: if invalid_context_df is empty, returns valid_context_df unchanged.
- No available reports (report_df is None or empty): for all invalid contexts, the context string is trimmed to fit max_context_tokens via _sort_and_trim_context, CONTEXT_SIZE is computed, CONTEXT_EXCEED_FLAG is set to False, and the function returns the union of valid_context_df and the trimmed invalid contexts.
- Reports are available: remove the observed reports from level_context_df (level_context_df = _antijoin_reports(level_context_df, report_df)); for each remaining invalid context, attempt substitution with sub-community reports by computing sub_context_df and building community_df; any remaining invalids not covered by sub-communities are collected in remaining_df, trimmed via _sort_and_trim_context, and finally all parts are united via union(valid_context_df, community_df, remaining_df). The resulting CONTEXT_SIZE is computed from CONTEXT_STRING, and CONTEXT_EXCEED_FLAG is set to False in the result.

Returns:
    pd.DataFrame: A DataFrame containing prepared contexts for communities at the specified level. The rows include CONTEXT_STRING and metadata columns such as CONTEXT_SIZE and CONTEXT_EXCEED_FLAG; the output is filtered to the given level.

Raises:
    Propagated exceptions from helper utilities may be raised (e.g., KeyError if required columns are missing); the function does not raise its own explicit errors.

## Dependencies

This function calls:

- `graphrag/index/operations/summarize_communities/graph_context/context_builder.py::_antijoin_reports`
- `graphrag/index/operations/summarize_communities/graph_context/context_builder.py::_get_community_df`
- `graphrag/index/operations/summarize_communities/graph_context/context_builder.py::_get_subcontext_df`
- `graphrag/index/operations/summarize_communities/graph_context/context_builder.py::_sort_and_trim_context`
- `graphrag/index/utils/dataframes.py::union`

