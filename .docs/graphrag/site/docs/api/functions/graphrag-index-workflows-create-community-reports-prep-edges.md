---
sidebar_position: 225
---

# _prep_edges

**File:** `graphrag/index/workflows/create_community_reports.py` (lines 161-177)

## Signature

```python
def _prep_edges(input: pd.DataFrame) -> pd.DataFrame
```

## Description

Prepare edges data by filling missing descriptions and constructing the EDGE_DETAILS field.

Args:
    input: pd.DataFrame. The input DataFrame containing edge data. Missing DESCRIPTION values are filled with "No Description" and a new EDGE_DETAILS column is created from SHORT_ID, EDGE_SOURCE, EDGE_TARGET, DESCRIPTION, and EDGE_DEGREE.

Returns:
    pd.DataFrame: The input DataFrame augmented with an EDGE_DETAILS column. The function mutates the input in place.

Raises:
    KeyError: If input is missing any of the required columns: SHORT_ID, EDGE_SOURCE, EDGE_TARGET, DESCRIPTION, or EDGE_DEGREE.

## Called By

This function is called by:

- `graphrag/index/workflows/create_community_reports.py::create_community_reports`

