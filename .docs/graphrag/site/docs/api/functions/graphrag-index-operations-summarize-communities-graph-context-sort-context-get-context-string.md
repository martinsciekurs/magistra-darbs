---
sidebar_position: 144
---

# _get_context_string

**File:** `graphrag/index/operations/summarize_communities/graph_context/sort_context.py` (lines 27-54)

## Signature

```python
def _get_context_string(
        entities: list[dict],
        edges: list[dict],
        claims: list[dict],
        sub_community_reports: list[dict] | None = None,
    ) -> str
```

## Description

Concatenate structured data into a context string.

Args:
    entities: List of entity dictionaries to include in the context.
    edges: List of edge/relationship dictionaries to include in the context.
    claims: List of claim dictionaries to include in the context.
    sub_community_reports: Optional list of dictionaries for sub-community reports to include at the top.

Returns:
    str: The concatenated context string with optional reports and sections for Entities, Claims, and Relationships, formatted as CSV blocks.

## Called By

This function is called by:

- `graphrag/index/operations/summarize_communities/graph_context/sort_context.py::sort_context`

