---
sidebar_position: 38
---

# graphrag/data_model/entity.py

## Overview

GraphRag Entity data model.

Purpose
Defines the Entity data model used to represent a graph entity in the GraphRag data model. It includes the Entity class and a from_dict classmethod to deserialize an Entity from a dictionary with configurable key mappings for identifiers, metadata, embeddings, and related data.

Exports
- Entity: The data model class representing a graph entity with identifying information, metadata, embeddings, and relationships to related data such as text units and communities.
- Entity.from_dict: Classmethod to construct an Entity instance from a dictionary using configurable key names for id, short_id, title, type, description, description_embedding, name_embedding, community, text_unit_ids, degree, and attributes.

Summary
The Entity class encapsulates the essential identifiers and descriptive metadata for a graph entity, and from_dict provides a flexible deserialization path from dictionaries.

## Classes

- [`Entity`](../api/classes/graphrag-data-model-entity-entity)

## Functions

- [`from_dict`](../api/functions/graphrag-data-model-entity-from-dict)

