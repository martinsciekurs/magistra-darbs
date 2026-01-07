---
sidebar_position: 375
---

# to_entity_dataframe

**File:** `graphrag/query/input/retrieval/entities.py` (lines 57-92)

## Signature

```python
def to_entity_dataframe(
    entities: list[Entity],
    include_entity_rank: bool = True,
    rank_description: str = "number of relationships",
) -> pd.DataFrame
```

## Description

Convert a list of entities to a pandas DataFrame.

Args:
    entities: list[Entity]
        The list of Entity objects to convert to a dataframe.
    include_entity_rank: bool
        If True, include a column for the entity rank. The header for this column uses rank_description.
    rank_description: str
        The header name for the rank column when include_entity_rank is True.

Returns:
    pd.DataFrame
        A dataframe with one row per entity. Columns start with "id", "entity", "description", and, if include_entity_rank is True, a rank column with the header given by rank_description. Additional columns are derived from the keys of the first entity's attributes (excluding any header names). Each row contains the corresponding values as strings where possible; empty strings are used for missing values.

Raises:
    None

## Example 💡 Generated

```python
from module import to_entity_dataframe
from types import SimpleNamespace
e1 = SimpleNamespace(short_id="E1", title="Entity One",
  description="First ent.", attributes={"t":"A"}, rank=5)
e2 = SimpleNamespace(short_id="E2", title="Entity Two",
  description="Second ent.", attributes={"t":"B"}, rank=2)
entities = [e1, e2]
df = to_entity_dataframe(entities, include_entity_rank=True, rank_description="rank")
print(df)  # id, entity, desc, rank, attrs
```

## Called By

This function is called by:

- `graphrag/query/context_builder/local_context.py::get_candidate_context`

