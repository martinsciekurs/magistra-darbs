---
sidebar_position: 324
---

# _get_header

**File:** `graphrag/query/context_builder/community_context.py` (lines 54-63)

## Signature

```python
def _get_header(attributes: list[str]) -> list[str]
```

## Description

Builds the header row for the community context data table based on the given attributes and surrounding configuration.

Args:
    attributes: List[str] - Attributes to include in the header (after removing the default id and title duplicates).

Returns:
    List[str] - The constructed header list, starting with "id" and "title", followed by filtered attributes, then either "summary" or "content" depending on use_community_summary, and optionally the rank name if include_community_rank is True. The exact behavior may depend on surrounding configuration variables such as include_community_weight, community_weight_name, and community_rank_name.

## Called By

This function is called by:

- `graphrag/query/context_builder/community_context.py::build_community_context`

