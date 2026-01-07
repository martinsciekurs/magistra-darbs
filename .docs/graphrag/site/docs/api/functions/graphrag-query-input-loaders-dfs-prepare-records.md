---
sidebar_position: 353
---

# _prepare_records

**File:** `graphrag/query/input/loaders/dfs.py` (lines 25-32)

## Signature

```python
def _prepare_records(df: pd.DataFrame) -> list[dict]
```

## Description

Reset the index of the DataFrame, rename the reset index column to 'Index', and convert the result to a list of dictionaries.

Args:
    df: The DataFrame to process.

Returns:
    list[dict]: A list of dictionaries representing the DataFrame rows. Each dictionary includes an 'Index' key for the original row index.

## Called By

This function is called by:

- `graphrag/query/input/loaders/dfs.py::read_entities`
- `graphrag/query/input/loaders/dfs.py::read_relationships`
- `graphrag/query/input/loaders/dfs.py::read_covariates`
- `graphrag/query/input/loaders/dfs.py::read_communities`
- `graphrag/query/input/loaders/dfs.py::read_community_reports`
- `graphrag/query/input/loaders/dfs.py::read_text_units`

