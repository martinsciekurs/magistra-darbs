---
sidebar_position: 635
---

# display_search_result

**File:** `unified-search-app/app/ui/search.py` (lines 39-60)

## Signature

```python
def display_search_result(
    container: DeltaGenerator, result: SearchResult, stats: SearchStats | None = None
)
```

## Description

Display search results in the UI and update the corresponding placeholder.

This function formats the search result response with hyperlinks via format_response_hyperlinks, renders it as HTML in the provided Streamlit container, and stores the rendered content in a session_state placeholder derived from the result's search_type (for example, a placeholder named "&lt;search_type&gt;_response_placeholder"). If stats are provided and completion_time is available, it also renders a summary line showing tokens used, LLM calls, and elapsed time.

Args:
    container (DeltaGenerator): The Streamlit container to render the search result into.
    result (SearchResult): The search result data to display, including response and the
        search_type used to derive UI keys and the HTML element id.
    stats (SearchStats | None): Optional statistics about the search operation. When provided
        and completion_time is not None, a formatted stats line is shown.

Returns:
    None

## Dependencies

This function calls:

- `unified-search-app/app/ui/search.py::format_response_hyperlinks`

