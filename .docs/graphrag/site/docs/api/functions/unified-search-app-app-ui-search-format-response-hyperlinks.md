---
sidebar_position: 632
---

# format_response_hyperlinks

**File:** `unified-search-app/app/ui/search.py` (lines 100-118)

## Signature

```python
def format_response_hyperlinks(str_response: str, search_type: str = "")
```

## Description

Format response to show hyperlinks inside the response UI.

Args:
    str_response (str): The response string to process.
    search_type (str): The search type value; used to build the hyperlink href. Optional.
Returns:
    str: The response string with the matched citation numbers converted to hyperlinks.

## Dependencies

This function calls:

- `unified-search-app/app/ui/search.py::format_response_hyperlinks_by_key`

## Called By

This function is called by:

- `unified-search-app/app/ui/search.py::display_search_result`

