---
sidebar_position: 592
---

# run_drift_search

**File:** `unified-search-app/app/app_logic.py` (lines 254-304)

## Signature

```python
def run_drift_search(
    query: str,
    sv: SessionVariables,
) -> SearchResult
```

## Description

Run drift search.

Execute a drift-based search using the Drift search engine, calling the Drift API with the
configuration and session data provided, and return a SearchResult containing the response and
associated context data for display.

Args:
    query: The search query string to send to the Drift search API.
    sv: SessionVariables containing configuration and data used to perform the drift search
        (graphrag_config, entities, communities, community_reports, text_units, relationships,
        and dataset_config with community_level).

Returns:
    SearchResult: The drift search result containing the response and its context data.

## Dependencies

This function calls:

- `graphrag.api::drift_search`

## Called By

This function is called by:

- `unified-search-app/app/app_logic.py::run_all_searches`

