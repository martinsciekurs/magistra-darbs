---
sidebar_position: 105
---

# create_row_from_claim_data

**File:** `graphrag/index/operations/extract_covariates/extract_covariates.py` (lines 79-81)

## Signature

```python
def create_row_from_claim_data(row, covariate_data: Covariate, covariate_type: str)
```

## Description

Create a row from claim data and the input row.

Args:
  row: The input row to extend with covariate data.
  covariate_data: Covariate data to be merged into the row (converted to a dict via asdict).
  covariate_type: The covariate type to include in the returned row.

Returns:
  dict: A new dictionary containing the original row data, the covariate data fields, and the covariate_type field.

Raises:
  TypeError: If row is not a mapping that can be expanded with **, or if covariate_data cannot be converted to a dict via asdict.

## Called By

This function is called by:

- `graphrag/index/operations/extract_covariates/extract_covariates.py::run_strategy`

