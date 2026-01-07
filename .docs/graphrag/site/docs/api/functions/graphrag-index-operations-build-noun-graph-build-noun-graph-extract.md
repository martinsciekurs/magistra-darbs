---
sidebar_position: 62
---

# extract

**File:** `graphrag/index/operations/build_noun_graph/build_noun_graph.py` (lines 59-67)

## Signature

```python
def extract(row)
```

## Description

Extract noun phrases from a row's text using a cache-backed analyzer.

Args:
  row: dict[str, Any] or pandas.Series: A mapping with a "text" key containing the input text to analyze.

Returns:
  list[str]: The noun phrases extracted from the text, or the cached result if available.

Raises:
  KeyError: If the input row does not contain the required "text" key, or if a required key is missing during hashing in gen_sha512_hash.

## Dependencies

This function calls:

- `graphrag/index/utils/hashing.py::gen_sha512_hash`

