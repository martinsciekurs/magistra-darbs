---
sidebar_position: 133
---

# explode_communities

**File:** `graphrag/index/operations/summarize_communities/explode_communities.py` (lines 13-23)

## Signature

```python
def explode_communities(
    communities: pd.DataFrame, entities: pd.DataFrame
) -> pd.DataFrame
```

## Description

Explode a list of communities into nodes for filtering.

Args:
    communities: pd.DataFrame
        DataFrame containing an entity_ids column with the IDs of entities in each community, along with community and level metadata used after exploding.
    entities: pd.DataFrame
        DataFrame containing an id column used to join with the exploded entity_ids, and a community identifier column (the one named by COMMUNITY_ID) for filtering.

Returns:
    pd.DataFrame
        A DataFrame of entities enriched with community information after the explode and merge, filtered to exclude rows where the community identifier equals -1.

Raises:
    KeyError
        If required columns are missing from the input DataFrames (for example entity_ids in communities, id in entities, or the COMMUNITY_ID column).

## Called By

This function is called by:

- `graphrag/index/workflows/create_community_reports.py::create_community_reports`
- `graphrag/index/workflows/create_community_reports_text.py::create_community_reports_text`

