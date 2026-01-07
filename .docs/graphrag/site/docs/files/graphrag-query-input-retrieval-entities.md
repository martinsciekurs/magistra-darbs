---
sidebar_position: 196
---

# graphrag/query/input/retrieval/entities.py

## Overview

Utilities for retrieving and converting Entity objects in Graphrag query processing.

This module exposes helpers to convert Entity objects to a pandas DataFrame and to retrieve entities by attribute, name, or ID. It also includes a small UUID validation utility. The functions are designed to operate on collections of Entity instances with minimal assumptions about entity structure beyond the attributes they inspect.

Exports:
- to_entity_dataframe(entities: list[Entity], include_entity_rank: bool = True, rank_description: str = "number of relationships") -&gt; pandas.DataFrame
- get_entity_by_attribute(entities: Iterable[Entity], attribute_name: str, attribute_value: Any) -&gt; list[Entity]
- is_valid_uuid(value: str) -&gt; bool
- get_entity_by_name(entities: Iterable[Entity], entity_name: str) -&gt; list[Entity]
- get_entity_by_id(entities: dict[str, Entity], value: str) -&gt; Entity | None
- get_entity_by_key(entities: Iterable[Entity], key: str, value: str | int) -&gt; Entity | None

Notes:
- UUID handling: get_entity_by_id and get_entity_by_key recognize both dashed and dashless UUID formats when matching UUID-like values.
- DataFrame representation: to_entity_dataframe returns a tabular view of the provided entities; if include_entity_rank is True, a rank column is included with a header defined by rank_description.

Example:
Usage examples:
df = to_entity_dataframe(entities)
active_entities = get_entity_by_attribute(entities, "status", "active")
assert is_valid_uuid("550e8400-e29b-41d4-a716-446655440000")

Edge cases:
- If entities contain objects without the expected attributes, filtering behavior follows the implementation.

## Functions

- [`to_entity_dataframe`](../api/functions/graphrag-query-input-retrieval-entities-to-entity-dataframe)
- [`get_entity_by_attribute`](../api/functions/graphrag-query-input-retrieval-entities-get-entity-by-attribute)
- [`is_valid_uuid`](../api/functions/graphrag-query-input-retrieval-entities-is-valid-uuid)
- [`get_entity_by_name`](../api/functions/graphrag-query-input-retrieval-entities-get-entity-by-name)
- [`get_entity_by_id`](../api/functions/graphrag-query-input-retrieval-entities-get-entity-by-id)
- [`get_entity_by_key`](../api/functions/graphrag-query-input-retrieval-entities-get-entity-by-key)

