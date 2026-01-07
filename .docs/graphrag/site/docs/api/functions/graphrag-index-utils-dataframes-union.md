---
sidebar_position: 181
---

# union

**File:** `graphrag/index/utils/dataframes.py` (lines 46-48)

## Signature

```python
def union(*frames: pd.DataFrame) -> pd.DataFrame
```

## Description

Perform a union operation on the given set of dataframes.

Args:
    frames: A variable number of pandas.DataFrame objects to union.

Returns:
    pd.DataFrame: The concatenated DataFrame containing the union of all input frames.

Raises:
    ValueError: If no frames are provided.

## Example 💡 Generated

```python
from module import union
import pandas as pd
valid_context_df = pd.DataFrame({"a":[1], "b":[3]})
invalid_context_df = pd.DataFrame({"a":[5], "b":[6]})
result = union(valid_context_df, invalid_context_df)
print(result)
# expected: two rows (1,3) and (5,6)
```

## Called By

This function is called by:

- `graphrag/index/operations/summarize_communities/graph_context/context_builder.py::build_level_context`

