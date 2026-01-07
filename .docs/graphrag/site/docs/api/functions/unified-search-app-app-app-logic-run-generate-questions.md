---
sidebar_position: 595
---

# run_generate_questions

**File:** `unified-search-app/app/app_logic.py` (lines 106-119)

## Signature

```python
def run_generate_questions(query: str, sv: SessionVariables)
```

## Description

Run global search to generate questions for the dataset.

Args:
  query (str): The search query string used to generate questions from the global search.
  sv (SessionVariables): The SessionVariables instance containing configuration and state for the current session.

Returns:
  tuple[SearchResult, ...]: The results of the global search question generation tasks, in the order they were added.

Raises:
  Exception: Exceptions raised by the inner coroutines may propagate.

## Dependencies

This function calls:

- `unified-search-app/app/app_logic.py::run_global_search_question_generation`

