---
sidebar_position: 634
---

# display_graph_citations

**File:** `unified-search-app/app/ui/search.py` (lines 267-284)

## Signature

```python
def display_graph_citations(
    entities: pd.DataFrame, relationships: pd.DataFrame, citation_type: str
)
```

## Description

Display graph citations into the UI.

Args:
  entities: pd.DataFrame — AI-extracted entities to render in the UI.
  relationships: pd.DataFrame — AI-extracted relationships to render in the UI.
  citation_type: str — The type used when rendering the HTML tables (passed to render_html_table).

Returns:
  None — This function does not return a value.

## Dependencies

This function calls:

- `unified-search-app/app/ui/search.py::render_html_table`

