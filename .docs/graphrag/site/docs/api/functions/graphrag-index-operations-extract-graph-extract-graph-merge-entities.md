---
sidebar_position: 110
---

# _merge_entities

**File:** `graphrag/index/operations/extract_graph/extract_graph.py` (lines 100-110)

## Signature

```python
def _merge_entities(entity_dfs) -> pd.DataFrame
```

## Description

Merge and aggregate multiple entity DataFrames into a single aggregated entities DataFrame by title and type.

Args:
  entity_dfs: List[pandas.DataFrame] List of DataFrames containing entity information. Each DataFrame is expected to include the columns: "title", "type", "description", and "source_id".

Returns:
  pandas.DataFrame A DataFrame with one row per (title, type) pair containing:
    - title: entity title
    - type: entity type
    - description: list of descriptions for this key
    - text_unit_ids: list of source_id values for this key
    - frequency: number of source_id entries for this key

## Called By

This function is called by:

- `graphrag/index/operations/extract_graph/extract_graph.py::extract_graph`

