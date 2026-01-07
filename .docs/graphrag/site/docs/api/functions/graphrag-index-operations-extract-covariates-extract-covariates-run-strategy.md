---
sidebar_position: 107
---

# run_strategy

**File:** `graphrag/index/operations/extract_covariates/extract_covariates.py` (lines 53-66)

## Signature

```python
def run_strategy(row)
```

## Description

Run the strategy on a single input row to asynchronously extract covariates from text.

Args:
  row: The input row to process. The text to analyze is read from row[column].

Returns:
  List[dict[str, Any]]: A list of rows augmented with covariate data. Each item is produced by merging the original row with the corresponding covariate data (converted to a dict) and including a covariate_type field set to covariate_type.

Raises:
  Exception: Propagates exceptions raised during claim extraction or row construction.

## Dependencies

This function calls:

- `graphrag/index/operations/extract_covariates/extract_covariates.py::create_row_from_claim_data`
- `graphrag/index/operations/extract_covariates/extract_covariates.py::run_extract_claims`

