---
sidebar_position: 344
---

# _filter_under_community_level

**File:** `graphrag/query/indexer_adapters.py` (lines 238-244)

## Signature

```python
def _filter_under_community_level(
    df: pd.DataFrame, community_level: int
) -> pd.DataFrame
```

## Description

Filter a DataFrame by community level.

Args:
    df: pandas DataFrame that must contain a column named level used for filtering.
    community_level: int threshold; keep rows where level &lt;= community_level.

Returns:
    pandas.DataFrame with rows where level &lt;= community_level.

Raises:
    AttributeError: if the input DataFrame does not have a level column.

## Called By

This function is called by:

- `graphrag/query/indexer_adapters.py::read_indexer_reports`
- `graphrag/query/indexer_adapters.py::read_indexer_entities`

