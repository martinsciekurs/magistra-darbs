---
sidebar_position: 263
---

# _merge_covariates

**File:** `graphrag/index/workflows/update_covariates.py` (lines 58-82)

## Signature

```python
def _merge_covariates(
    old_covariates: pd.DataFrame, delta_covariates: pd.DataFrame
) -> pd.DataFrame
```

## Description

Merge the covariates.

This function merges the existing old covariates with the delta covariates. The delta covariates are mutated in-place to assign new human_readable_id values that are consecutive and start from max(old_covariates.human_readable_id) + 1. The function then concatenates the old covariates and the mutated delta covariates using ignore_index=True and returns the resulting DataFrame.

Args:
    old_covariates (pd.DataFrame): The old covariates.
    delta_covariates (pd.DataFrame): The delta covariates to be merged into the old covariates. This DataFrame is mutated in-place to assign new IDs.

Returns:
    pd.DataFrame: The merged covariates, with old_covariates preceding delta_covariates and a reset index (ignore_index=True).

## Called By

This function is called by:

- `graphrag/index/workflows/update_covariates.py::_update_covariates`

