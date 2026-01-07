---
sidebar_position: 155
---

# prep_text_units

**File:** `graphrag/index/operations/summarize_communities/text_unit_context/prep_text_units.py` (lines 15-45)

## Signature

```python
def prep_text_units(
    text_unit_df: pd.DataFrame,
    node_df: pd.DataFrame,
) -> pd.DataFrame
```

## Description

Calculate text unit degree and concatenate text unit details.

Args:
    text_unit_df (pd.DataFrame): DataFrame containing text unit information to be enriched with degree information.
    node_df (pd.DataFrame): DataFrame of nodes. Each row should include TEXT_UNIT_IDS, TITLE, COMMUNITY_ID, and NODE_DEGREE used to compute text unit degrees.

Returns:
    pd.DataFrame: DataFrame with columns [COMMUNITY_ID, TEXT_UNIT_ID, ALL_DETAILS].

## Called By

This function is called by:

- `graphrag/index/operations/summarize_communities/text_unit_context/context_builder.py::build_local_context`

