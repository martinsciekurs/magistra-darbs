---
sidebar_position: 151
---

# run_generate

**File:** `graphrag/index/operations/summarize_communities/summarize_communities.py` (lines 71-82)

## Signature

```python
def run_generate(record)
```

## Description

Generate a community summary for a single record.

Args:
  record: dict-like containing the keys defined by schemas.COMMUNITY_ID, schemas.COMMUNITY_LEVEL, and schemas.CONTEXT_STRING. The function uses record[schemas.COMMUNITY_ID], record[schemas.COMMUNITY_LEVEL], and record[schemas.CONTEXT_STRING] to generate the report.

Returns:
  CommunityReport | None: The generated report for the given community, or None if no report could be produced.

Raises:
  Exception: May raise exceptions propagated from _generate_report and the asynchronous operations involved in generating the report.

## Dependencies

This function calls:

- `graphrag/index/operations/summarize_communities/summarize_communities.py::_generate_report`

