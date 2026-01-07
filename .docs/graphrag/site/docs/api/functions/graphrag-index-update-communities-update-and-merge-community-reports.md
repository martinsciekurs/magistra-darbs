---
sidebar_position: 176
---

# _update_and_merge_community_reports

**File:** `graphrag/index/update/communities.py` (lines 89-151)

## Signature

```python
def _update_and_merge_community_reports(
    old_community_reports: pd.DataFrame,
    delta_community_reports: pd.DataFrame,
    community_id_mapping: dict,
) -> pd.DataFrame
```

## Description

Update and merge old and delta community reports into a single DataFrame aligned to the final columns.

Args:
    old_community_reports: The old community reports.
    delta_community_reports: The delta community reports.
    community_id_mapping: The mapping from original delta community IDs to final IDs.

Returns:
    pd.DataFrame: The updated community reports aligned to COMMUNITY_REPORTS_FINAL_COLUMNS.

Raises:
    KeyError: If required columns such as 'community' or 'parent' are missing from input DataFrames.
    ValueError: If a column intended to be numeric cannot be cast to int when applying the mapping.
    TypeError: If inputs are not DataFrames or the mapping is not a dict-like.

## Called By

This function is called by:

- `graphrag/index/workflows/update_community_reports.py::_update_community_reports`

