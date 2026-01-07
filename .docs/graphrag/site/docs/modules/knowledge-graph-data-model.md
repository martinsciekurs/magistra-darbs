---
sidebar_position: 5
---

# Knowledge Graph Data Model

Core data structures and schemas that represent documents, entities, relationships, communities, and associated metadata in the knowledge graph.

## Overview

Knowledge Graph Data Model

Architectural purpose:
Core data structures and schemas that represent documents, entities, relationships, communities, and associated metadata in the knowledge graph, enabling serialization/deserialization and consistent data modeling across the GraphRag domain.

Key components and responsibilities:
- graphrag/data_model/document.py: Document dataclass model; factory to build Document instances from dictionaries with configurable key mappings; exports Document and from_dict.
- graphrag/data_model/entity.py: Entity dataclass; from_dict for deserializing Entity from dictionaries with configurable key mappings for identifiers, metadata, embeddings, and more.
- graphrag/data_model/relationship.py: Relationship dataclass; from_dict constructor to instantiate from external data formats; public API includes Relationship and from_dict.
- graphrag/data_model/community.py: Community dataclass; extends Named; represents a Community with identity, naming semantics, metadata and relationships.
- graphrag/data_model/community_report.py: CommunityReport dataclass; inherits Named; from_dict constructor for building instances representing community reports.
- graphrag/data_model/text_unit.py: TextUnit dataclass; encapsulates a unit of text with associated identifiers linking to entities, relationships, covariates, and related documents; inherits from Id...
- graphrag/data_model/schemas.py and graphrag/data_model/types.py: Schema and type definitions that underpin the data models.

Main entry points / public APIs:
- Document.from_dict
- Entity.from_dict
- Relationship.from_dict
- Community.from_dict
- CommunityReport.from_dict
- TextUnit.from_dict
- The Document, Entity, Relationship, Community, CommunityReport, and TextUnit dataclasses

Notes:
- This module aggregates the core data models used to represent graph constructs and their metadata in the GraphRag system.

## Files in this Module

- [`graphrag/data_model/document.py`](../files/graphrag-data-model-document)
- [`graphrag/data_model/entity.py`](../files/graphrag-data-model-entity)
- [`graphrag/data_model/relationship.py`](../files/graphrag-data-model-relationship)
- [`graphrag/data_model/community.py`](../files/graphrag-data-model-community)
- [`graphrag/data_model/community_report.py`](../files/graphrag-data-model-community-report)
- [`graphrag/data_model/text_unit.py`](../files/graphrag-data-model-text-unit)
- [`graphrag/data_model/schemas.py`](../files/graphrag-data-model-schemas)
- [`graphrag/data_model/types.py`](../files/graphrag-data-model-types)
