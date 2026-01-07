---
sidebar_position: 628
---

# convert_numbered_list_to_array

**File:** `unified-search-app/app/ui/search.py` (lines 158-169)

## Signature

```python
def convert_numbered_list_to_array(numbered_list_str)
```

## Description

Convert a numbered-list string into an array of extracted items.

Args:
    numbered_list_str: str-like
        A string-like object containing a numbered list. Each line that matches a numeric dot pattern (one or more digits followed by a dot and optional whitespace) will have the text after the marker extracted as an item. Non-matching lines are ignored. The order of extracted items matches their appearance in the input.

Returns:
    list[str]
        A list of extracted items in the input order.

Raises:
    AttributeError
        If numbered_list_str does not support strip or split (i.e., is not a string-like object).

## Called By

This function is called by:

- `unified-search-app/app/ui/search.py::format_suggested_questions`

