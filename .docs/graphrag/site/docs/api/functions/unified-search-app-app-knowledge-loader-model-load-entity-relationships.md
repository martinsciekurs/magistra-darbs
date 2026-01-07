---
sidebar_position: 616
---

# load_entity_relationships

**File:** `unified-search-app/app/knowledge_loader/model.py` (lines 39-44)

## Signature

```python
def load_entity_relationships(
    dataset: str,
    _datasource: Datasource,
) -> pd.DataFrame
```

## Description

Return a DataFrame containing the entity-relationship data loaded from the given dataset and datasource.

Args:
  dataset: str — The dataset identifier to load the entity-relationship data from.
  _datasource: Datasource — The Datasource descriptor used to access the data.

Returns:
  pd.DataFrame — DataFrame containing the relationship data as produced by get_relationship_data. The specific columns depend on the underlying data_prep implementation.

Raises:
  Exception — Propagates any exceptions raised by get_relationship_data.

## Called By

This function is called by:

- `unified-search-app/app/knowledge_loader/model.py::load_model`

