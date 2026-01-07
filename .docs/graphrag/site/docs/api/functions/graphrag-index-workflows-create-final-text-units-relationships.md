---
sidebar_position: 236
---

# _relationships

**File:** `graphrag/index/workflows/create_final_text_units.py` (lines 98-107)

## Signature

```python
def _relationships(df: pd.DataFrame) -> pd.DataFrame
```

## Description

Compute mapping of text units to the relationship IDs that reference them.

Args:
    df: pd.DataFrame containing the columns "id" and "text_unit_ids".

Returns:
    pd.DataFrame: DataFrame with columns "id" and "relationship_ids"; for each text_unit_id, relationship_ids is the list of unique ids referencing that text unit.

Raises:
    KeyError: If the required columns "id" or "text_unit_ids" are missing from df.

## Called By

This function is called by:

- `graphrag/index/workflows/create_final_text_units.py::create_final_text_units`

