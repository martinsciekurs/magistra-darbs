---
sidebar_position: 175
---

# _update_and_merge_communities

**File:** `graphrag/index/update/communities.py` (lines 14-86)

## Signature

```python
def _update_and_merge_communities(
    old_communities: pd.DataFrame,
    delta_communities: pd.DataFrame,
) -> tuple[pd.DataFrame, dict]
```

## Description

Update and merge old and delta communities.

This function mutates the provided DataFrames to ensure required structure, remaps delta
community IDs to avoid collisions with old data, and merges them into a single DataFrame
aligned to COMMUNITIES_FINAL_COLUMNS. It also returns the mapping from original delta
community IDs to the new IDs assigned during the merge.

Args:
    old_communities (pd.DataFrame): The existing/old communities. If 'size' or 'period' columns
        are missing, they will be added with missing values. Must contain an integer or numeric
        'community' column.
    delta_communities (pd.DataFrame): The delta/new communities to merge into the old data.
        If 'size' or 'period' columns are missing, they will be added with missing values. Must contain
        a numeric 'community' column and a 'parent' column that will be remapped using the computed
        ID mapping.

Returns:
    tuple[pd.DataFrame, dict]:
        - The updated communities DataFrame, aligned to COMMUNITIES_FINAL_COLUMNS, with a new 'title'
          and 'human_readable_id' based on the remapped 'community' IDs.
        - A dictionary mapping from original delta_communities IDs to the new IDs assigned during the merge.

Raises:
    KeyError: If required columns (for example, 'community' in either input DataFrame, or 'parent' in delta_communities)
        are missing.

Notes:
    - The function mutates old_communities and delta_communities in place by adding missing columns and
      remapping IDs. Downstream code should be aware of input mutations.
    - The internal mapping also includes a sentinel mapping &#123;-1: -1&#125; to preserve a special value.

## Called By

This function is called by:

- `graphrag/index/workflows/update_communities.py::_update_communities`

