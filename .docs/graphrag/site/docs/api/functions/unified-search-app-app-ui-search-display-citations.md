---
sidebar_position: 633
---

# display_citations

**File:** `unified-search-app/app/ui/search.py` (lines 63-97)

## Signature

```python
def display_citations(
    container: DeltaGenerator | None = None, result: SearchResult | None = None
)
```

## Description

Display citations into the UI.

Args:
  container: DeltaGenerator | None = None — The UI container to render citations into. If None, citations will not be rendered.
  result: SearchResult | None = None — The SearchResult containing the context data to display as citations. If provided, the context data will be processed and displayed.

Returns:
  None.

## Dependencies

This function calls:

- `unified-search-app/app/ui/search.py::render_html_table`

