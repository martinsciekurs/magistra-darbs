---
sidebar_position: 326
---

# _is_included

**File:** `graphrag/query/context_builder/community_context.py` (lines 51-52)

## Signature

```python
def _is_included(report: CommunityReport) -> bool
```

## Description

Determine whether the given CommunityReport should be included in the context based on its rank.

Args:
    report (CommunityReport): The community report to evaluate for inclusion.

Returns:
    bool: True if report.rank is not None and report.rank &gt;= min_community_rank, otherwise False.

## Called By

This function is called by:

- `graphrag/query/context_builder/community_context.py::build_community_context`

