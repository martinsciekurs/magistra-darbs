---
sidebar_position: 226
---

# _prep_nodes

**File:** `graphrag/index/workflows/create_community_reports.py` (lines 140-158)

## Signature

```python
def _prep_nodes(input: pd.DataFrame) -> pd.DataFrame
```

## Description

Populate node descriptions and create NODE_DETAILS without filtering.

This function fills missing descriptions with "No Description" and creates a new
NODE_DETAILS column by aggregating SHORT_ID, TITLE, DESCRIPTION, and NODE_DEGREE
for each node. No rows are filtered; the operation mutates the input DataFrame in
place and returns the same object.

Args:
    input (pd.DataFrame): Input nodes DataFrame. Must contain the columns
        DESCRIPTION, SHORT_ID, TITLE, and NODE_DEGREE (as defined by the data model).

Returns:
    pd.DataFrame: The same input DataFrame, mutated in place with the new NODE_DETAILS column.

Raises:
    KeyError: If any required column (DESCRIPTION, SHORT_ID, TITLE, NODE_DEGREE) is
        missing from the input DataFrame.

## Called By

This function is called by:

- `graphrag/index/workflows/create_community_reports.py::create_community_reports`

