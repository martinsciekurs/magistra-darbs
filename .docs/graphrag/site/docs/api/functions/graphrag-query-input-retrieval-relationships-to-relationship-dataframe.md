---
sidebar_position: 383
---

# to_relationship_dataframe

**File:** `graphrag/query/input/retrieval/relationships.py` (lines 105-139)

## Signature

```python
def to_relationship_dataframe(
    relationships: list[Relationship], include_relationship_weight: bool = True
) -> pd.DataFrame
```

## Description

Convert a list of relationships to a pandas dataframe.

Args:
  relationships: list[Relationship] - List of Relationship objects to convert to a pandas DataFrame.
  include_relationship_weight: bool - Whether to include the weight column in the output.

Returns:
  pd.DataFrame - A DataFrame representing the relationships. If the relationships list is empty, an empty DataFrame is returned. The DataFrame contains columns: id, source, target, description, and optionally weight. It also includes any additional attribute columns derived from the first relationship's attributes (excluding any columns already present in the header). The rows reflect each relationship's short_id, source, target, description, weight, and attribute values as strings where available.

## Called By

This function is called by:

- `graphrag/query/context_builder/local_context.py::get_candidate_context`

