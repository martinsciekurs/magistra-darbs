---
sidebar_position: 153
---

# build_local_context

**File:** `graphrag/index/operations/summarize_communities/text_unit_context/context_builder.py` (lines 26-82)

## Signature

```python
def build_local_context(
    community_membership_df: pd.DataFrame,
    text_units_df: pd.DataFrame,
    node_df: pd.DataFrame,
    tokenizer: Tokenizer,
    max_context_tokens: int = 16000,
) -> pd.DataFrame
```

## Description

Prepare local context data for community report generation using text unit data.

Computes per-community local context by enriching text units with degree information, merging with community membership, and producing a per-community context string sorted by relevance. The function relies on prep_text_units to obtain text unit details (including short_id, text, and entity_degree) and merges these details with membership information to build a per-community ALL_CONTEXT list. The resulting DataFrame includes a sorted CONTEXT_STRING, its token size CONTEXT_SIZE, and a flag CONTEXT_EXCEED_FLAG indicating whether the context exceeds max_context_tokens.

Args:
  community_membership_df: DataFrame containing community membership data with columns including COMMUNITY_ID, COMMUNITY_LEVEL, and TEXT_UNIT_IDS.
  text_units_df: DataFrame of text units used to enrich with degree information via prep_text_units.
  node_df: DataFrame of nodes used to compute entity degrees for text units.
  tokenizer: Tokenizer used to compute token counts and to sort contexts.
  max_context_tokens: Maximum number of tokens allowed for a community's local context.

Returns:
  A pandas DataFrame containing per-community local context data, keyed by COMMUNITY_ID and COMMUNITY_LEVEL, including ALL_CONTEXT (list of dictionaries with id, text, entity_degree), CONTEXT_STRING (sorted context), CONTEXT_SIZE (token count), and CONTEXT_EXCEED_FLAG (whether CONTEXT_SIZE exceeds max_context_tokens).

## Dependencies

This function calls:

- `graphrag/index/operations/summarize_communities/text_unit_context/prep_text_units.py::prep_text_units`
- `graphrag/index/operations/summarize_communities/text_unit_context/sort_context.py::sort_context`

## Called By

This function is called by:

- `graphrag/index/workflows/create_community_reports_text.py::create_community_reports_text`

