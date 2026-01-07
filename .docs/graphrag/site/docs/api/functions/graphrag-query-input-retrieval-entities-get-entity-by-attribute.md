---
sidebar_position: 376
---

# get_entity_by_attribute

**File:** `graphrag/query/input/retrieval/entities.py` (lines 45-54)

## Signature

```python
def get_entity_by_attribute(
    entities: Iterable[Entity], attribute_name: str, attribute_value: Any
) -> list[Entity]
```

## Description

Get entities by attribute.

Args:
    entities: Iterable[Entity], the collection of entities to search.
    attribute_name: str, the name of the attribute to match.
    attribute_value: Any, the value to match for the given attribute.

Returns:
    list[Entity], a list of entities whose attributes contain attribute_name with the given attribute_value.

Raises:
    TypeError: if entities is not an iterable.
    AttributeError: if an element in entities does not have an attributes attribute.

