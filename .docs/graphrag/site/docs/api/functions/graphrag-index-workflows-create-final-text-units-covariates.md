---
sidebar_position: 233
---

# _covariates

**File:** `graphrag/index/workflows/create_final_text_units.py` (lines 110-118)

## Signature

```python
def _covariates(df: pd.DataFrame) -> pd.DataFrame
```

## Description

Compute covariate IDs for each text unit from the input DataFrame.

Args:
    df: Input DataFrame containing the columns "id" and "text_unit_id".

Returns:
    pd.DataFrame: DataFrame with columns "id" and "covariate_ids"; for each text_unit_id, covariate_ids is the list of unique ids associated with that text unit.

Raises:
    KeyError: If the required columns "id" or "text_unit_id" are missing from df.

## Example 💡 Generated

```python
from mymodule import _covariates
import pandas as pd
df = pd.DataFrame({"id":[1,2,3,4],
                   "text_unit_id":[1,1,2,2]})
res = _covariates(df)
print(res)  # Expect covariate_ids per text_unit_id
# id 1 -> [1,2], id 2 -> [3,4]
```

## Called By

This function is called by:

- `graphrag/index/workflows/create_final_text_units.py::create_final_text_units`

