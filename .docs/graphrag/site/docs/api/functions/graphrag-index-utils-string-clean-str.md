---
sidebar_position: 215
---

# clean_str

**File:** `graphrag/index/utils/string.py` (lines 11-19)

## Signature

```python
def clean_str(input: Any) -> str
```

## Description

Clean an input string by removing HTML escapes, control characters, and other unwanted characters.

Args:
    input: Any
        The value to sanitize. If the value is not a string, it is returned unchanged.

Returns:
    str
        The sanitized string if the input is a string; otherwise, the original value is returned unchanged.

## Called By

This function is called by:

- `graphrag/index/operations/extract_graph/graph_extractor.py::GraphExtractor._process_results`

