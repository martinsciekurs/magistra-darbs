---
sidebar_position: 629
---

# format_response_hyperlinks_by_key

**File:** `unified-search-app/app/ui/search.py` (lines 121-148)

## Signature

```python
def format_response_hyperlinks_by_key(
    str_response: str, key: str, anchor: str, search_type: str = ""
)
```

## Description

Format response to show hyperlinks inside the response UI by key.

Args:
    str_response: The response string to process.
    key: The key label in the response to locate citation patterns (e.g., "Entities").
    anchor: The anchor component used to construct hyperlink targets.
    search_type: The search type value; used to build the hyperlink href. Optional.

Returns:
    str: The response string with the matched citation numbers converted to hyperlinks.

## Called By

This function is called by:

- `unified-search-app/app/ui/search.py::format_response_hyperlinks`

