---
sidebar_position: 558
---

# test_get_entity_by_key

**File:** `tests/unit/query/input/retrieval/test_entities.py` (lines 92-167)

## Signature

```python
def test_get_entity_by_key()
```

## Description

Get an Entity by key from a collection.

This helper searches through an iterable of Entity objects and returns the first Entity whose attribute named by key equals the provided value. If value is a string that represents a UUID (with or without dashes), the comparison also considers the same UUID with dashes removed to accommodate both representations.

Parameters:
- entities: Iterable[Entity]. The collection of Entity objects to search.
- key: str. The attribute name on Entity to compare.
- value: str | int. The value to match against the attribute. If value is a UUID string, also compare the undashed form of the UUID.

Returns:
- Entity | None: The first matching Entity if found, otherwise None.

Raises:
- AttributeError: If any item in entities does not have the attribute named by key.

Examples:
- No match returns None:
  get_entity_by_key([Entity(id="id1", short_id="sid1", title="title1")], "id", "00000000-0000-0000-0000-000000000000") -&gt; None
- Match by dashed UUID:
  get_entity_by_key([
    Entity(id="2da37c7a-50a8-44d4-aa2c-fd401e19976c", short_id="sid1", title="title1"),
    Entity(id="c4f93564-4507-4ee4-b102-98add401a965", short_id="sid2", title="title2"),
    Entity(id="7c6f2bc9-47c9-4453-93a3-d2e174a02cd9", short_id="sid3", title="title3"),
  ],
  "id",
  "7c6f2bc9-47c9-4453-93a3-d2e174a02cd9",
) -&gt; Entity(id="7c6f2bc9-47c9-4453-93a3-d2e174a02cd9", short_id="sid3", title="title3")
- Match by undashed UUID:
  get_entity_by_key([
    Entity(id="2da37c7a50a844d4aa2cfd401e19976c", short_id="sid1", title="title1"),
    Entity(id="c4f9356445074ee4b10298add401a965", short_id="sid2", title="title2"),
    Entity(id="7c6f2bc947c9445393a3d2e174a02cd9", short_id="sid3", title="title3"),
  ],
  "id",
  "7c6f2bc947c9445393a3d2e174a02cd9",
) -&gt; Entity(id="7c6f2bc947c9445393a3d2e174a02cd9", short_id="sid3", title="title3")
- Match by numeric rank:
  get_entity_by_key([
    Entity(id="id1", short_id="sid1", title="title1", rank=1),
    Entity(id="id2", short_id="sid2", title="title2a", rank=2),
    Entity(id="id3", short_id="sid3", title="title3", rank=3),
  ],
  "rank",
  2,
) -&gt; Entity(id="id2", short_id="sid2", title="title2a", rank=2)

## Dependencies

This function calls:

- `graphrag/data_model/entity.py::Entity`
- `graphrag/query/input/retrieval/entities.py::get_entity_by_key`

