---
sidebar_position: 180
---

# _update_and_merge_relationships

**File:** `graphrag/index/update/relationships.py` (lines 14-85)

## Signature

```python
def _update_and_merge_relationships(
    old_relationships: pd.DataFrame, delta_relationships: pd.DataFrame
) -> pd.DataFrame
```

## Description

Update and merge relationships.

Args:
    old_relationships: pd.DataFrame The old relationships.
    delta_relationships: pd.DataFrame The delta relationships.

Returns:
    pd.DataFrame The updated relationships, containing the final columns as defined by RELATIONSHIPS_FINAL_COLUMNS.

Raises:
    KeyError: If required columns are missing from the input DataFrames.
    TypeError: If the inputs are not pandas DataFrames.

## Called By

This function is called by:

- `graphrag/index/workflows/update_entities_relationships.py::_update_entities_and_relationships`

