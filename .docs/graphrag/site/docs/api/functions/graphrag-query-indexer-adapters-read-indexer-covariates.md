---
sidebar_position: 350
---

# read_indexer_covariates

**File:** `graphrag/query/indexer_adapters.py` (lines 45-60)

## Signature

```python
def read_indexer_covariates(final_covariates: pd.DataFrame) -> list[Covariate]
```

## Description

Read in the Covariates from the raw indexing outputs.

This function converts the id column to a string and delegates to read_covariates to construct Covariate objects using the input DataFrame with id cast to string, short_id_col set to human_readable_id, attributes_cols set to object_id, status, start_date, end_date, and description, and text_unit_ids_col set to None.

Args:
  final_covariates (pd.DataFrame): DataFrame containing covariate records produced by the indexing process. Must include an id column (which will be cast to string) and a human_readable_id column used as the short identifier. The covariate attributes to export are object_id, status, start_date, end_date, and description.

Returns:
  list[Covariate]: A list of Covariate objects parsed from the covariates DataFrame.

Raises:
  KeyError: If required columns are missing from final_covariates.
  ValueError: If data in columns cannot be coerced to the expected types.
  Exception: Propagates exceptions raised by read_covariates.

## Dependencies

This function calls:

- `graphrag/query/input/loaders/dfs.py::read_covariates`

## Called By

This function is called by:

- `graphrag/api/query.py::local_search_streaming`

