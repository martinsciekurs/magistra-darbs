---
sidebar_position: 371
---

# to_community_report_dataframe

**File:** `graphrag/query/input/retrieval/community_reports.py` (lines 39-75)

## Signature

```python
def to_community_report_dataframe(
    reports: list[CommunityReport],
    include_community_rank: bool = False,
    use_community_summary: bool = False,
) -> pd.DataFrame
```

## Description

Convert a list of CommunityReport objects to a pandas DataFrame.

Args:
  reports: list[CommunityReport] - List of CommunityReport objects to convert to a DataFrame.
  include_community_rank: bool - Whether to include a rank column in the output.
  use_community_summary: bool - Whether to include a summary column (summary) instead of content.

Returns:
  pd.DataFrame - A DataFrame representing the provided community reports. If the input list is empty, an empty DataFrame is returned.

Raises:
  None - This function does not raise exceptions.

## Called By

This function is called by:

- `graphrag/query/input/retrieval/community_reports.py::get_candidate_communities`

