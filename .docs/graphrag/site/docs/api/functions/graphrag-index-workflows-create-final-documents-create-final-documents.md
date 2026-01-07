---
sidebar_position: 231
---

# create_final_documents

**File:** `graphrag/index/workflows/create_final_documents.py` (lines 36-77)

## Signature

```python
def create_final_documents(
    documents: pd.DataFrame, text_units: pd.DataFrame
) -> pd.DataFrame
```

## Description

Transforms input documents and text units into final documents.

Args:
    documents: pd.DataFrame
        Input documents data frame. Expected to contain at least the columns referenced by DOCUMENTS_FINAL_COLUMNS.
    text_units: pd.DataFrame
        Input text units data frame. Expected to contain an 'document_ids' column indicating related document ids.

Returns:
    pd.DataFrame
        Final documents data frame with columns defined by DOCUMENTS_FINAL_COLUMNS. The function ensures a metadata column exists and assigns a human_readable_id based on the row index.

Raises:
    Exception: Propagates exceptions raised by pandas operations or data frame manipulations if inputs are invalid.

## Called By

This function is called by:

- `graphrag/index/workflows/create_final_documents.py::run_workflow`

