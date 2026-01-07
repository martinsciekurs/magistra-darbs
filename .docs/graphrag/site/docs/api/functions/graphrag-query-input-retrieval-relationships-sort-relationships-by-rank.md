---
sidebar_position: 381
---

# sort_relationships_by_rank

**File:** `graphrag/query/input/retrieval/relationships.py` (lines 81-102)

## Signature

```python
def sort_relationships_by_rank(
    relationships: list[Relationship],
    ranking_attribute: str = "rank",
) -> list[Relationship]
```

## Description

Sort relationships by a ranking_attribute.

This function sorts the provided list of Relationship objects in descending order
based on a ranking attribute. If the ranking_attribute exists as a key in a
Relationship's attributes dictionary, its value is used (converted to int)
for sorting. If not, and ranking_attribute is "rank" or "weight", the
corresponding attributes on the Relationship are used (with a default of 0
or 0.0 when missing). The input list is sorted in place and returned. If the
input list is empty, it is returned unchanged.

Args:
    relationships: List of Relationship objects to be sorted.
    ranking_attribute: Attribute name used for ranking. May be a key in each
        Relationship's attributes, or one of "rank" or "weight". Defaults to
        "rank".

Returns:
    list[Relationship]: The same list object, now sorted in descending order by the
        chosen ranking attribute.

Raises:
    ValueError: If a ranking_attribute value exists in a Relationship.attributes
        dictionary but cannot be converted to int when ranking_attribute is present
        in attribute_names.

## Called By

This function is called by:

- `graphrag/query/input/retrieval/relationships.py::get_in_network_relationships`
- `graphrag/query/input/retrieval/relationships.py::get_out_network_relationships`

