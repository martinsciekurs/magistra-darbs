---
sidebar_position: 234
---

# _entities

**File:** `graphrag/index/workflows/create_final_text_units.py` (lines 86-95)

## Signature

```python
def _entities(df: pd.DataFrame) -> pd.DataFrame
```

## Description

Compute mapping of text units to the entity IDs that reference them.

Args:
    df: pd.DataFrame containing the columns "id" and "text_unit_ids".

Returns:
    pd.DataFrame: DataFrame with columns "id" and "entity_ids"; for each text_unit_id, entity_ids is the list of unique ids referencing that text unit.

Raises:
    KeyError: If the required columns "id" or "text_unit_ids" are missing from df.

## Example 💡 Generated

```python
from module import _entities
import pandas as pd
df = pd.DataFrame([[1,[10,11]],
                   [2,[11]],
                   [3,[12,10]]],
                  columns=["id","text_unit_ids"])
res = _entities(df)
print(res)  # Expected: id=text_unit_ids, entity_ids
```

## Called By

This function is called by:

- `graphrag/index/workflows/create_final_text_units.py::create_final_text_units`

