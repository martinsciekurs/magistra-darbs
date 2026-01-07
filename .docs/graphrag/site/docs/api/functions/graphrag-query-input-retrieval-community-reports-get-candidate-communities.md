---
sidebar_position: 372
---

# get_candidate_communities

**File:** `graphrag/query/input/retrieval/community_reports.py` (lines 14-36)

## Signature

```python
def get_candidate_communities(
    selected_entities: list[Entity],
    community_reports: list[CommunityReport],
    include_community_rank: bool = False,
    use_community_summary: bool = False,
) -> pd.DataFrame
```

## Description

Get all communities that are related to selected entities.

This function collects all community IDs from the provided selected entities, filters the given
community_reports to those IDs, and returns a DataFrame produced by to_community_report_dataframe
using the specified options.

Args:
  selected_entities: The selected entities for which to retrieve candidate communities.
  community_reports: The pool of CommunityReport objects to search.
  include_community_rank: Whether to include a rank column in the output.
  use_community_summary: Whether to include the summary field instead of full content.

Returns:
  pd.DataFrame: A DataFrame representing the candidate communities related to the selected entities.

Raises:
  None

## Dependencies

This function calls:

- `graphrag/query/input/retrieval/community_reports.py::to_community_report_dataframe`

## Called By

This function is called by:

- `graphrag/query/structured_search/local_search/mixed_context.py::LocalSearchMixedContext._build_community_context`

