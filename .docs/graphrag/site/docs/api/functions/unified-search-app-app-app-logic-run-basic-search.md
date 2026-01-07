---
sidebar_position: 594
---

# run_basic_search

**File:** `unified-search-app/app/app_logic.py` (lines 307-351)

## Signature

```python
def run_basic_search(
    query: str,
    sv: SessionVariables,
) -> SearchResult
```

## Description

Run basic search.

Args:
    query: str
        The search query string used to perform the basic search.
    sv: SessionVariables
        The SessionVariables instance containing configuration and state for the current session.

Returns:
    SearchResult
        The result of the basic search, including the search_type (Basic), the textual response, and the context data.

Raises:
    Exception
        If an error occurs during the basic search process (e.g., API call failure).

## Dependencies

This function calls:

- `graphrag.api::basic_search`

## Called By

This function is called by:

- `unified-search-app/app/app_logic.py::run_all_searches`

