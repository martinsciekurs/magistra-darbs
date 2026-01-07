---
sidebar_position: 264
---

# tests/unit/query/input/retrieval/test_entities.py

## Overview

Utilities for retrieving Entity objects by identifier.

This module provides helpers to locate Entity instances from a collection by either
their id or by a specified attribute key. It supports robust lookups, including
special handling for UUID strings (matching with or without dashes).

Exports:
- get_entity_by_id(entities: dict[str, Entity], value: str) -&gt; Entity | None
  Args:
    entities: Mapping of entity IDs to Entity objects.
    value: The id value to look up. If value is a valid UUID, also try the same value
      with dashes removed.
  Returns:
    Entity | None: The matching Entity if found, otherwise None.
  Raises:
    None

- get_entity_by_key(entities: Iterable[Entity], key: str, value: str) -&gt; Entity | None
  Args:
    entities: Iterable of Entity objects.
    key: The attribute name to compare.
    value: The value to compare against. If value is a UUID string, also compare its
      dashed-removed form.
  Returns:
    Entity | None: The first matching Entity if found, otherwise None.
  Raises:
    None

Summary:
These utilities enable robust entity lookups by id or by a specified attribute, with
support for UUID representations that may include or omit dashes.

## Functions

- [`test_get_entity_by_id`](../api/functions/tests-unit-query-input-retrieval-test-entities-test-get-entity-by-id)
- [`test_get_entity_by_key`](../api/functions/tests-unit-query-input-retrieval-test-entities-test-get-entity-by-key)

