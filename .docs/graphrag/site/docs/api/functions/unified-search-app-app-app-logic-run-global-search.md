---
sidebar_position: 591
---

# run_global_search

**File:** `unified-search-app/app/app_logic.py` (lines 202-251)

## Signature

```python
def run_global_search(query: str, sv: SessionVariables) -> SearchResult
```

## Description

Run global search.

Args:
    query: str
        The search query string used to perform the global search.
    sv: SessionVariables
        The SessionVariables instance containing configuration and state for the current session.

Returns:
    SearchResult
        The result of the global search, including the search_type (Global), the textual response, and the context data.

Raises:
    Exception
        If an error occurs during the global search process.

## Dependencies

This function calls:

- `graphrag.api::global_search`

## Called By

This function is called by:

- `unified-search-app/app/app_logic.py::run_all_searches`

