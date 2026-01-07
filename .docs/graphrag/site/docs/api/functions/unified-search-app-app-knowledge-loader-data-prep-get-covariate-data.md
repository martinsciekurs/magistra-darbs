---
sidebar_position: 606
---

# get_covariate_data

**File:** `unified-search-app/app/knowledge_loader/data_prep.py` (lines 42-47)

## Signature

```python
def get_covariate_data(dataset: str, _datasource: Datasource) -> pd.DataFrame
```

## Description

Return a dataframe with covariate data from the indexed-data.

Args:
    dataset (str): The dataset identifier to load covariates for.
    _datasource (Datasource): The data source to query for covariates.

Returns:
    pd.DataFrame: A DataFrame containing covariate data loaded for the specified dataset.

Raises:
    Exception: If the underlying data source read operation fails.

