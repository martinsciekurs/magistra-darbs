---
sidebar_position: 354
---

# read_text_units

**File:** `graphrag/query/input/loaders/dfs.py` (lines 229-261)

## Signature

```python
def read_text_units(
    df: pd.DataFrame,
    id_col: str = "id",
    text_col: str = "text",
    entities_col: str | None = "entity_ids",
    relationships_col: str | None = "relationship_ids",
    covariates_col: str | None = "covariate_ids",
    tokens_col: str | None = "n_tokens",
    document_ids_col: str | None = "document_ids",
    attributes_cols: list[str] | None = None,
) -> list[TextUnit]
```

## Description

Read text units from a dataframe using pre-converted records.

Args:
  df (pd.DataFrame): The DataFrame to process.
  id_col (str): Column name for the text unit identifier. Default 'id'.
  text_col (str): Column name containing the text of the unit. Default 'text'.
  entities_col (str | None): Column name for entity_ids, or None to omit. Default 'entity_ids'.
  relationships_col (str | None): Column name for relationship_ids, or None. Default 'relationship_ids'.
  covariates_col (str | None): Column name for covariate_ids, or None. Default 'covariate_ids'.
  tokens_col (str | None): Column name for the token count. Default 'n_tokens'.
  document_ids_col (str | None): Column name for document_ids, or None. Default 'document_ids'.
  attributes_cols (list[str] | None): Additional per-row attributes to include in the TextUnit. If None, no extra attributes are captured. Default None.

Returns:
  list[TextUnit]: A list of TextUnit objects constructed from the dataframe rows.

Raises:
  ValueError: If column_name is None or the column is missing from data during value extraction (as enforced by to_str).
  TypeError: If a value in a column cannot be converted to the expected type by the helper utilities (as raised by to_optional_list, to_optional_dict, or to_optional_int).

## Dependencies

This function calls:

- `graphrag/data_model/text_unit.py::TextUnit`
- `graphrag/query/input/loaders/dfs.py::_prepare_records`
- `graphrag/query/input/loaders/utils.py::to_optional_dict`
- `graphrag/query/input/loaders/utils.py::to_optional_int`
- `graphrag/query/input/loaders/utils.py::to_optional_list`
- `graphrag/query/input/loaders/utils.py::to_str`

## Called By

This function is called by:

- `graphrag/query/indexer_adapters.py::read_indexer_text_units`

