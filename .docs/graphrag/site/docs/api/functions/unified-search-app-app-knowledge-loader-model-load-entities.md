---
sidebar_position: 615
---

# load_entities

**File:** `unified-search-app/app/knowledge_loader/model.py` (lines 30-35)

## Signature

```python
def load_entities(
    dataset: str,
    _datasource: Datasource,
) -> pd.DataFrame
```

## Description

Return a DataFrame of Entity data loaded from the given dataset and datasource.

Args:
    dataset: The dataset identifier to load entities from.
    _datasource: The Datasource descriptor used to access the data.

Returns:
    pd.DataFrame: DataFrame containing the loaded Entity data.

Raises:
    Exception: Propagates any exceptions raised by get_entity_data.

## Called By

This function is called by:

- `unified-search-app/app/knowledge_loader/model.py::load_model`

