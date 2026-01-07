---
sidebar_position: 631
---

# format_suggested_questions

**File:** `unified-search-app/app/ui/search.py` (lines 151-155)

## Signature

```python
def format_suggested_questions(questions: str)
```

## Description

Format suggested questions to the UI.

Args:
    questions: str
        A string containing suggested questions. The function removes square-bracketed citations (patterns like [ ... ]) and then converts the remaining text into an array by parsing a numbered list.

Returns:
    list[str]
        A list of extracted questions obtained from the remaining numbered-list text.

## Dependencies

This function calls:

- `unified-search-app/app/ui/search.py::convert_numbered_list_to_array`

