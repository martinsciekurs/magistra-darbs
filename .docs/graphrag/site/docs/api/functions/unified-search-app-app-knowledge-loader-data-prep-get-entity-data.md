---
sidebar_position: 604
---

# get_entity_data

**File:** `unified-search-app/app/knowledge_loader/data_prep.py` (lines 23-29)

## Signature

```python
def get_entity_data(dataset: str, _datasource: Datasource) -> pd.DataFrame
```

## Description

Return a dataframe with entity data from the indexed data.

Reads entity data from the configured table via the provided data source (config.entity_table). The function prints the number of entity records and the dataset name as a side effect and is cached with Streamlit's cache_data decorator using TTL from config.default_ttl.

Args:
    dataset: The dataset name to load.
    _datasource: The data source used to read the entity data from the indexed data.

Returns:
    pd.DataFrame: A dataframe containing the entity data loaded from the indexed data.

Raises:
    Exception: If reading from the data source fails.

