---
sidebar_position: 325
---

# _compute_community_weights

**File:** `graphrag/query/context_builder/community_context.py` (lines 189-225)

## Signature

```python
def _compute_community_weights(
    community_reports: list[CommunityReport],
    entities: list[Entity] | None,
    weight_attribute: str = "occurrence",
    normalize: bool = True,
) -> list[CommunityReport]
```

## Description

Compute weights for communities based on the number of text units associated with entities in each community.

Args:
  community_reports: List[CommunityReport]
      Reports for communities to assign weights to.
  entities: list[Entity] | None
      Entities that reference community_ids and contain text_unit_ids. Text units are aggregated by community_id across all entities.
  weight_attribute: str
      Name of the attribute stored on each CommunityReport's attributes dictionary to hold the computed weight. Defaults to "occurrence".
  normalize: bool
      If True, normalize weights by the maximum weight across all reports so weights lie in [0, 1].

Returns:
  list[CommunityReport]
      The updated list of CommunityReport objects with the computed weight stored under the specified weight_attribute in report.attributes. Weights are normalized when normalize is True.

## Called By

This function is called by:

- `graphrag/query/context_builder/community_context.py::build_community_context`

