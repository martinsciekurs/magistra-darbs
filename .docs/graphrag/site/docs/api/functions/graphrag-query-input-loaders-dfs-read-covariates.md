---
sidebar_position: 357
---

# read_covariates

**File:** `graphrag/query/input/loaders/dfs.py` (lines 117-146)

## Signature

```python
def read_covariates(
    df: pd.DataFrame,
    id_col: str = "id",
    short_id_col: str | None = "human_readable_id",
    subject_col: str = "subject_id",
    covariate_type_col: str | None = "type",
    text_unit_ids_col: str | None = "text_unit_ids",
    attributes_cols: list[str] | None = None,
) -> list[Covariate]
```

## Description

Read covariates from a dataframe using pre-converted records.

Args:
    df (pd.DataFrame): The DataFrame to process.
    id_col (str): Column name for the covariate identifier. Default 'id'.
    short_id_col (str | None): Column name for a short/human-readable id. If None, uses the index-derived id.
    subject_col (str): Column name for the subject identifier. Default 'subject_id'.
    covariate_type_col (str | None): Column name for covariate type. If None, defaults to 'claim'.
    text_unit_ids_col (str | None): Column name for text_unit_ids. Default 'text_unit_ids'.
    attributes_cols (list[str] | None): Optional list of additional attribute column names to include in Covariate.attributes.

Returns:
    list[Covariate]: A list of Covariate objects constructed from the dataframe.

Raises:
    ValueError: If a required column name is None or missing in a row.
    TypeError: If the value for text_unit_ids_col cannot be interpreted as a list (as required by to_optional_list).

## Dependencies

This function calls:

- `graphrag/data_model/covariate.py::Covariate`
- `graphrag/query/input/loaders/dfs.py::_prepare_records`
- `graphrag/query/input/loaders/utils.py::to_optional_list`
- `graphrag/query/input/loaders/utils.py::to_optional_str`
- `graphrag/query/input/loaders/utils.py::to_str`

## Called By

This function is called by:

- `graphrag/query/indexer_adapters.py::read_indexer_covariates`

