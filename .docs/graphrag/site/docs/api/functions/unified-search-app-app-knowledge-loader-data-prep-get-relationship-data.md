---
sidebar_position: 605
---

# get_relationship_data

**File:** `unified-search-app/app/knowledge_loader/data_prep.py` (lines 33-38)

## Signature

```python
def get_relationship_data(dataset: str, _datasource: Datasource) -> pd.DataFrame
```

## Description

Return a dataframe with entity-entity relationship data from the indexed-data.

Reads relationship data from the configured table via the provided _datasource (config.relationship_table). The function prints the number of relationship records and the dataset name as a side effect and is cached with Streamlit's cache_data decorator using TTL from config.default_ttl.

Args:
    dataset: str — The dataset name to load.
    _datasource: Datasource — The Datasource descriptor used to access the data from the configured relationship table.

Returns:
    pd.DataFrame — DataFrame containing the relationship data.

Raises:
    Exception — If reading from the data source fails.

