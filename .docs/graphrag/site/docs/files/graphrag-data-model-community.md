---
sidebar_position: 34
---

# graphrag/data_model/community.py

## Overview

Module providing the Community data model for graphrag.

This module defines the Community dataclass, which represents a Community in the graph data model and extends Named to provide identity and naming semantics, as well as community-specific metadata and relationships. It encapsulates identity, hierarchical placement, and associations to entities, relationships, text units, and covariates.

Exports:
- Community: Dataclass representing a Community, subclassing Named.
- from_dict: Classmethod to create a Community from a dictionary, with configurable keys (id_key, title_key, short_id_key, level_key, entities_key, relationships_key, text_units_key, covariates_key, parent_key, children_key, attributes_key, size_key, period_key).

## Classes

- [`Community`](../api/classes/graphrag-data-model-community-community)

## Functions

- [`from_dict`](../api/functions/graphrag-data-model-community-from-dict)

