---
sidebar_position: 355
---

# read_entities

**File:** `graphrag/query/input/loaders/dfs.py` (lines 35-74)

## Signature

```python
def read_entities(
    df: pd.DataFrame,
    id_col: str = "id",
    short_id_col: str | None = "human_readable_id",
    title_col: str = "title",
    type_col: str | None = "type",
    description_col: str | None = "description",
    name_embedding_col: str | None = "name_embedding",
    description_embedding_col: str | None = "description_embedding",
    community_col: str | None = "community_ids",
    text_unit_ids_col: str | None = "text_unit_ids",
    rank_col: str | None = "degree",
    attributes_cols: list[str] | None = None,
) -> list[Entity]
```

## Description

Read entities from a dataframe using pre-converted records.

This function prepares the input DataFrame by resetting the index and converting it to a list of dictionaries, then constructs Entity objects from each record.

Args:
  df (pd.DataFrame): The DataFrame to process.
  id_col (str): Column name for the entity identifier. Default id.
  short_id_col (str | None): Column name for a short/human readable id. If None, uses the index value. Default human_readable_id.
  title_col (str): Column name for the entity title. Default title.
  type_col (str | None): Column name for the entity type. If None, the type is omitted. Default type.
  description_col (str | None): Column name for the entity description. If None, the description is omitted. Default description.
  name_embedding_col (str | None): Column name for the name embedding vector. If None, omitted. Default name_embedding.
  description_embedding_col (str | None): Column name for the description embedding vector. If None, omitted. Default description_embedding.
  community_col (str | None): Column name for the list of community IDs. If None, omitted. Default community_ids.
  text_unit_ids_col (str | None): Column name for the list of text unit IDs. If None, omitted. Default text_unit_ids.
  rank_col (str | None): Column name for the rank/degree. If None, omitted. Default degree.
  attributes_cols (list[str] | None): Optional list of additional attribute column names to include in the resulting Entity.attributes. If None, no extra attributes are included.

Returns:
  list[Entity]: A list of Entity objects created from the dataframe records.

Raises:
  ValueError, TypeError: If required data is missing or has invalid type for the expected columns, as raised by the underlying conversion helpers (e.g., to_str, to_optional_str, to_optional_list, to_optional_int).

## Dependencies

This function calls:

- `graphrag/data_model/entity.py::Entity`
- `graphrag/query/input/loaders/dfs.py::_prepare_records`
- `graphrag/query/input/loaders/utils.py::to_optional_int`
- `graphrag/query/input/loaders/utils.py::to_optional_list`
- `graphrag/query/input/loaders/utils.py::to_optional_str`
- `graphrag/query/input/loaders/utils.py::to_str`

## Called By

This function is called by:

- `graphrag/query/indexer_adapters.py::read_indexer_entities`

