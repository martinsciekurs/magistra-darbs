---
sidebar_position: 593
---

# run_local_search

**File:** `unified-search-app/app/app_logic.py` (lines 148-199)

## Signature

```python
def run_local_search(
    query: str,
    sv: SessionVariables,
) -> SearchResult
```

## Description

Run local search.

Args:
    query: str
        The search query string used to perform the local search.
    sv: SessionVariables
        The SessionVariables instance containing configuration and state for the current session.

Returns:
    SearchResult
        The result of the local search, including the search_type (Local), the textual response, and the context data.

Raises:
    Exception
        If an error occurs during local search execution (e.g., API call or UI state access).

## Dependencies

This function calls:

- `graphrag.api::local_search`

## Called By

This function is called by:

- `unified-search-app/app/app_logic.py::run_all_searches`

