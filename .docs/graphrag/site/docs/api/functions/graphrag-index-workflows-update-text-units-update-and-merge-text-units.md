---
sidebar_position: 270
---

# _update_and_merge_text_units

**File:** `graphrag/index/workflows/update_text_units.py` (lines 60-92)

## Signature

```python
def _update_and_merge_text_units(
    old_text_units: pd.DataFrame,
    delta_text_units: pd.DataFrame,
    entity_id_mapping: dict,
) -> pd.DataFrame
```

## Description

Update and merge text units.

Args:
  old_text_units: pd.DataFrame
      The old text units.
  delta_text_units: pd.DataFrame
      The delta text units.
  entity_id_mapping: dict
      The entity id mapping.

Returns:
  pd.DataFrame
  The updated text units.

Raises:
  KeyError: If required columns are missing from the input dataframes (e.g., 'entity_ids' or 'human_readable_id').

## Called By

This function is called by:

- `graphrag/index/workflows/update_text_units.py::_update_text_units`

