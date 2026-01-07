---
sidebar_position: 617
---

# load_communities

**File:** `unified-search-app/app/knowledge_loader/model.py` (lines 62-66)

## Signature

```python
def load_communities(
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

## Called By

This function is called by:

- `unified-search-app/app/knowledge_loader/model.py::load_model`

