---
sidebar_position: 347
---

# read_indexer_text_units

**File:** `graphrag/query/indexer_adapters.py` (lines 36-42)

## Signature

```python
def read_indexer_text_units(final_text_units: pd.DataFrame) -> list[TextUnit]
```

## Description

Read in the Text Units from the raw indexing outputs.

Args:
  final_text_units (pd.DataFrame): The DataFrame containing the final text units produced by indexing outputs.

Returns:
  list[TextUnit]: A list of TextUnit objects parsed from the input DataFrame.

## Dependencies

This function calls:

- `graphrag/query/input/loaders/dfs.py::read_text_units`

## Called By

This function is called by:

- `graphrag/api/query.py::local_search_streaming`
- `graphrag/api/query.py::drift_search_streaming`
- `graphrag/api/query.py::basic_search_streaming`

