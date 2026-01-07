---
sidebar_position: 590
---

# run_global_search_question_generation

**File:** `unified-search-app/app/app_logic.py` (lines 122-145)

## Signature

```python
def run_global_search_question_generation(
    query: str,
    sv: SessionVariables,
) -> SearchResult
```

## Description

Run global search question generation process.

Args:
  query: The search query string used to generate questions from the global search.
  sv: The SessionVariables instance containing configuration and state for the current session.

Returns:
  SearchResult: The result of the global search question generation, including the search_type set to Global, the textual response, and the context data (a dict of context data if available, otherwise an empty dict).

## Dependencies

This function calls:

- `graphrag.api::global_search`

## Called By

This function is called by:

- `unified-search-app/app/app_logic.py::run_generate_questions`

