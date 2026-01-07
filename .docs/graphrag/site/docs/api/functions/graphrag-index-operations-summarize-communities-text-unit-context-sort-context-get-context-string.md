---
sidebar_position: 156
---

# get_context_string

**File:** `graphrag/index/operations/summarize_communities/text_unit_context/sort_context.py` (lines 16-55)

## Signature

```python
def get_context_string(
    text_units: list[dict],
    sub_community_reports: list[dict] | None = None,
) -> str
```

## Description

Concatenate structured data into a context string.

Args:
    text_units (list[dict]): List of text unit dictionaries to include in the context. Each dictionary should have an "id" key with a non-empty value.
    sub_community_reports (list[dict] | None): Optional list of dictionaries for sub-community reports to include at the top. Only reports containing a non-empty community id (defined by schemas.COMMUNITY_ID) are considered.

Returns:
    str: The context string built by optionally including a reports section followed by a sources section, separated by blank lines.

Raises:
    None: This function does not raise exceptions.

## Called By

This function is called by:

- `graphrag/index/operations/summarize_communities/text_unit_context/sort_context.py::sort_context`

