---
sidebar_position: 618
---

# load_covariates

**File:** `unified-search-app/app/knowledge_loader/model.py` (lines 48-50)

## Signature

```python
def load_covariates(dataset: str, _datasource: Datasource) -> pd.DataFrame
```

## Description

Load covariate data as a DataFrame for the given dataset and datasource.

Args:
  dataset: str - The dataset identifier to load covariates for.
  _datasource: Datasource - The data source to query for covariates.

Returns:
  pd.DataFrame - A DataFrame containing covariate data loaded for the specified dataset.

Raises:
  Propagates any exceptions raised by get_covariate_data.

## Called By

This function is called by:

- `unified-search-app/app/knowledge_loader/model.py::load_model`

