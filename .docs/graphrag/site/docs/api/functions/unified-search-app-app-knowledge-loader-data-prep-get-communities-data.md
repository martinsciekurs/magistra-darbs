---
sidebar_position: 602
---

# get_communities_data

**File:** `unified-search-app/app/knowledge_loader/data_prep.py` (lines 71-75)

## Signature

```python
def get_communities_data(
    _datasource: Datasource,
) -> pd.DataFrame
```

## Description

Return a dataframe with communities data from the indexed-data.

Args:
    _datasource: Datasource to read the communities data from the indexed-data.

Returns:
    A dataframe with communities data loaded from the indexed-data.

Raises:
    Exception: If the underlying data source read operation fails.

