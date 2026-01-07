---
sidebar_position: 390
---

# try_parse_json_object

**File:** `graphrag/query/llm/text_utils.py` (lines 45-103)

## Signature

```python
def try_parse_json_object(input: str, verbose: bool = True) -> tuple[str, dict]
```

## Description

JSON cleaning and formatting utilities for strings that may contain JSON or JSON-like content produced by an LLM.

Args:
- input: str. The raw string to parse and clean.
- verbose: bool. If True, log warnings or exceptions encountered during parsing.

Returns:
- tuple[str, dict]. The input string (potentially cleaned) and the parsed JSON object as a dict. If parsing ultimately fails, the dict will be empty.

## Called By

This function is called by:

- `graphrag/query/context_builder/rate_relevancy.py::rate_relevancy`
- `graphrag/query/structured_search/drift_search/action.py::DriftAction.search`
- `graphrag/query/structured_search/global_search/search.py::GlobalSearch._parse_search_response`

