---
sidebar_position: 627
---

# render_html_table

**File:** `unified-search-app/app/ui/search.py` (lines 192-264)

## Signature

```python
def render_html_table(df: pd.DataFrame, search_type: str, key: str)
```

## Description

Render HTML table into the UI.

Builds an HTML fragment representing the given DataFrame as a table with a header and body. It applies per-cell formatting: strings may be truncated for display, and if a string value starts with a JSON-like object (for example, a dictionary in string form), the code attempts to extract the "summary" field from that JSON. It also generates per-row HTML ids to enable UI interactions; ids are constructed from the lowercased and stripped search_type and key with the row's id when available, otherwise using the row index. The function returns the HTML string suitable for insertion into the UI (for example via Streamlit's st.markdown with unsafe_allow_html=True).

Args:
- df (pd.DataFrame): DataFrame to render as HTML table for UI display.
- search_type (str): Type of search; used to generate the per-row HTML id (lowercased and stripped).
- key (str): Key associated with the search type; used in ID generation when an id column exists.

Returns:
- str: HTML string representing the rendered table.

Raises:
- json.JSONDecodeError: If a string value that begins with '&#123;' cannot be parsed as JSON to extract a summary.
- AttributeError or TypeError: If a row contains an id value that is not a string or otherwise cannot be stripped, or if input types are incompatible.
- ValueError: If inputs are of an unexpected type or contain invalid data for rendering.

## Called By

This function is called by:

- `unified-search-app/app/ui/search.py::display_citations`
- `unified-search-app/app/ui/search.py::display_graph_citations`

