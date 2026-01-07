---
sidebar_position: 374
---

# to_covariate_dataframe

**File:** `graphrag/query/input/retrieval/covariates.py` (lines 27-53)

## Signature

```python
def to_covariate_dataframe(covariates: list[Covariate]) -> pd.DataFrame
```

## Description

Convert a list of covariates to a pandas DataFrame.

Args:
    covariates: list[Covariate] - Covariate objects to convert. Each covariate is expected to have short_id, subject_id, and attributes (a dict). The resulting DataFrame will have columns: id, entity, and one column per attribute key found in the first covariate's attributes (excluding id and entity). Values are strings or empty strings when missing.

Returns:
    pd.DataFrame - DataFrame representation of the covariates. If covariates is empty, returns an empty DataFrame.

Raises:
    AttributeError, TypeError: If covariates do not conform to the expected Covariate interface or if attribute access fails.

## Called By

This function is called by:

- `graphrag/query/context_builder/local_context.py::get_candidate_context`

