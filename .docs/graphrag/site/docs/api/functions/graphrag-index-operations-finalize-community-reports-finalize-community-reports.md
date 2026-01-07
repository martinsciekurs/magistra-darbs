---
sidebar_position: 118
---

# finalize_community_reports

**File:** `graphrag/index/operations/finalize_community_reports.py` (lines 13-33)

## Signature

```python
def finalize_community_reports(
    reports: pd.DataFrame,
    communities: pd.DataFrame,
) -> pd.DataFrame
```

## Description

Merge input reports with communities to create final community reports.

Args:
    reports: The input reports data to be enriched with community metadata.
    communities: The communities dataset containing metadata used for enrichment (including fields used for the merge: 'community', 'parent', 'children', 'size', 'period').

Returns:
    The finalized community reports DataFrame containing only the columns defined by COMMUNITY_REPORTS_FINAL_COLUMNS, augmented with a human_readable_id and an id per row.

Raises:
    KeyError: If required columns are missing from the inputs or if the final column set referenced by COMMUNITY_REPORTS_FINAL_COLUMNS is not present in the merged result.

## Called By

This function is called by:

- `graphrag/index/workflows/create_community_reports.py::create_community_reports`
- `graphrag/index/workflows/create_community_reports_text.py::create_community_reports_text`

