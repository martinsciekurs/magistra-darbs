---
sidebar_position: 356
---

# read_relationships

**File:** `graphrag/query/input/loaders/dfs.py` (lines 77-114)

## Signature

```python
def read_relationships(
    df: pd.DataFrame,
    id_col: str = "id",
    short_id_col: str | None = "human_readable_id",
    source_col: str = "source",
    target_col: str = "target",
    description_col: str | None = "description",
    rank_col: str | None = "combined_degree",
    description_embedding_col: str | None = "description_embedding",
    weight_col: str | None = "weight",
    text_unit_ids_col: str | None = "text_unit_ids",
    attributes_cols: list[str] | None = None,
) -> list[Relationship]
```

## Description

Read relationships from a dataframe using pre-converted records.

Args:
    df: The DataFrame to process.
    id_col: Column name for the relationship identifier.
    short_id_col: Column name for a short/human-readable id. If None, uses the index-derived id.
    source_col: Column name for the relationship source.
    target_col: Column name for the relationship target.
    description_col: Optional column with a textual description of the relationship.
    rank_col: Optional column with the rank (degree) of the relationship.
    description_embedding_col: Optional column containing a description embedding as a list of floats.
    weight_col: Optional column with the weight of the relationship.
    text_unit_ids_col: Optional column with text unit identifiers as a list of strings.
    attributes_cols: Optional list of additional attribute column names to include in the attributes dict.

Returns:
    list[Relationship]: A list of Relationship objects constructed from the dataframe records.

Raises:
    ValueError: If a required column name is None or missing from the input data when converting values.
    TypeError: If a value cannot be converted to the expected type (e.g., incorrect list element types or mismatched types in conversions).

## Dependencies

This function calls:

- `graphrag/data_model/relationship.py::Relationship`
- `graphrag/query/input/loaders/dfs.py::_prepare_records`
- `graphrag/query/input/loaders/utils.py::to_optional_float`
- `graphrag/query/input/loaders/utils.py::to_optional_int`
- `graphrag/query/input/loaders/utils.py::to_optional_list`
- `graphrag/query/input/loaders/utils.py::to_optional_str`
- `graphrag/query/input/loaders/utils.py::to_str`

## Called By

This function is called by:

- `graphrag/query/indexer_adapters.py::read_indexer_relationships`

