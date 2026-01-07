---
sidebar_position: 111
---

# _merge_relationships

**File:** `graphrag/index/operations/extract_graph/extract_graph.py` (lines 113-123)

## Signature

```python
def _merge_relationships(relationship_dfs) -> pd.DataFrame
```

## Description

Merge multiple relationship DataFrames into a single aggregated DataFrame by source and target.

Args:
    relationship_dfs: Iterable of pandas.DataFrame. Each DataFrame should contain at least the columns
        'source', 'target', 'description', 'source_id', and 'weight'.

Returns:
    pd.DataFrame: A DataFrame grouped by 'source' and 'target' with the following aggregated columns:
        - description: list of descriptions for each (source, target) pair
        - text_unit_ids: list of source_id values within the group
        - weight: sum of weights within the group
    The result has 'source' and 'target' as columns with the index reset.

Raises:
    TypeError: If relationship_dfs is not a suitable iterable of DataFrames.
    KeyError: If required columns are missing from any input DataFrame.

## Called By

This function is called by:

- `graphrag/index/operations/extract_graph/extract_graph.py::extract_graph`

