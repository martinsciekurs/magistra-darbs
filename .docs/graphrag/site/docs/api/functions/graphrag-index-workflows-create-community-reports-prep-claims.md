---
sidebar_position: 224
---

# _prep_claims

**File:** `graphrag/index/workflows/create_community_reports.py` (lines 180-196)

## Signature

```python
def _prep_claims(input: pd.DataFrame) -> pd.DataFrame
```

## Description

Prepare claims data by filling missing descriptions and constructing the CLAIM_DETAILS field.

Args:
    input: The input DataFrame containing claims data. Missing DESCRIPTION values are filled with "No Description" and a new CLAIM_DETAILS column is created from SHORT_ID, CLAIM_SUBJECT, TYPE, CLAIM_STATUS, and DESCRIPTION.

Returns:
    pd.DataFrame: The input DataFrame augmented with a CLAIM_DETAILS column and with missing DESCRIPTION filled as "No Description".

## Called By

This function is called by:

- `graphrag/index/workflows/create_community_reports.py::create_community_reports`

