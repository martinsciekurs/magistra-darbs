---
sidebar_position: 597
---

# run_all_searches

**File:** `unified-search-app/app/app_logic.py` (lines 68-103)

## Signature

```python
def run_all_searches(query: str, sv: SessionVariables) -> list[SearchResult]
```

## Description

Run all enabled search engines and return the results.

Args:
    query: str
        The search query string used by the enabled searches.
    sv: SessionVariables
        The SessionVariables instance containing configuration and state used to determine which searches to run.

Returns:
    list[SearchResult]
        The results from the enabled searches.

Raises:
    Exception
        If an error occurs during the execution of any of the searches.

## Dependencies

This function calls:

- `unified-search-app/app/app_logic.py::run_basic_search`
- `unified-search-app/app/app_logic.py::run_drift_search`
- `unified-search-app/app/app_logic.py::run_global_search`
- `unified-search-app/app/app_logic.py::run_local_search`

