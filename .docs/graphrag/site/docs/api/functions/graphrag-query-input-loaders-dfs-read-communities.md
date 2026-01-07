---
sidebar_position: 359
---

# read_communities

**File:** `graphrag/query/input/loaders/dfs.py` (lines 149-188)

## Signature

```python
def read_communities(
    df: pd.DataFrame,
    id_col: str = "id",
    short_id_col: str | None = "community",
    title_col: str = "title",
    level_col: str = "level",
    entities_col: str | None = "entity_ids",
    relationships_col: str | None = "relationship_ids",
    text_units_col: str | None = "text_unit_ids",
    covariates_col: str | None = "covariate_ids",
    parent_col: str | None = "parent",
    children_col: str | None = "children",
    attributes_cols: list[str] | None = None,
) -> list[Community]
```

## Description

Read communities from a dataframe using pre-converted records.

Args:
  df: The DataFrame to process.
  id_col: Column name for the community identifier.
  short_id_col: Column name for the short identifier; if None, uses the index as a fallback.
  title_col: Title column name.
  level_col: Level column name.
  entities_col: Column name for the list of entity_ids associated with the community.
  relationships_col: Column name for the list of relationship_ids associated with the community.
  text_units_col: Column name for the list of text_unit_ids.
  covariates_col: Column name for the dictionary of covariate_ids.
  parent_col: Column name for the parent identifier.
  children_col: Column name for the children list.
  attributes_cols: Optional list of additional attribute columns to include in the Community attributes; None to skip.

Returns:
  list[Community]: A list of Community objects constructed from the dataframe.

Raises:
  ValueError: If a required column is None or missing from a row during conversion.
  TypeError: If a value is not of an expected type.

## Dependencies

This function calls:

- `graphrag/data_model/community.py::Community`
- `graphrag/query/input/loaders/dfs.py::_prepare_records`
- `graphrag/query/input/loaders/utils.py::to_list`
- `graphrag/query/input/loaders/utils.py::to_optional_dict`
- `graphrag/query/input/loaders/utils.py::to_optional_list`
- `graphrag/query/input/loaders/utils.py::to_optional_str`
- `graphrag/query/input/loaders/utils.py::to_str`

## Called By

This function is called by:

- `graphrag/query/indexer_adapters.py::read_indexer_communities`

