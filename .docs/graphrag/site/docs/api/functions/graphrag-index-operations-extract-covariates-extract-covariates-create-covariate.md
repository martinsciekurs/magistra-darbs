---
sidebar_position: 104
---

# create_covariate

**File:** `graphrag/index/operations/extract_covariates/extract_covariates.py` (lines 140-153)

## Signature

```python
def create_covariate(item: dict[str, Any]) -> Covariate
```

## Description

Create a Covariate instance from the provided item.

Args:
    item: dict[str, Any]
        The dictionary containing covariate fields. The function reads
        keys such as subject_id, object_id, type, status, start_date, end_date,
        description, source_text, record_id, and id to construct the Covariate.

Returns:
    Covariate
        The Covariate object created from the item.

## Dependencies

This function calls:

- `graphrag/index/operations/extract_covariates/typing.py::Covariate`

## Called By

This function is called by:

- `graphrag/index/operations/extract_covariates/extract_covariates.py::run_extract_claims`

