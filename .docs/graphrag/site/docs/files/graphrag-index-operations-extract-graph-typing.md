---
sidebar_position: 72
---

# graphrag/index/operations/extract_graph/typing.py

## Overview

Typing utilities for the extract_graph operation in Graphrag.

This module provides lightweight, runtime-agnostic type aliases and an enumeration used to describe how entities and relationships are extracted and represented within Graphrag's graph index workflow. It is intended for static typing and for clearly documenting the interfaces consumed by the extraction pipeline.

Exports:
- ExtractedEntity (dict[str, Any]): A dictionary representing an extracted entity with arbitrary fields.
- ExtractedRelationship (dict[str, Any]): A dictionary representing an extracted relationship with arbitrary fields.
- StrategyConfig (dict[str, Any]): Configuration for an extraction strategy (parameters, flags, etc.).
- EntityTypes (list[str]): A list of known entity type names.
- EntityExtractStrategy (Callable[[dict[str, Any], PipelineCache], Awaitable[ExtractedEntity]]): A function signature for an entity extraction strategy that receives a source record and a PipelineCache and returns, asynchronously, an ExtractedEntity.
- ExtractEntityStrategyType (Enum): An enumeration of available extraction strategies for entities. Members reference specific strategies used by the extraction workflow.

Notes:
- This is a typing-only module and contains no runtime logic beyond type definitions.
- The actual values for ExtractEntityStrategyType members are defined in the implementation; this docstring describes their purpose and usage.

## Classes

- [`ExtractEntityStrategyType`](../api/classes/graphrag-index-operations-extract-graph-typing-extractentitystrategytype)

## Functions

- [`__repr__`](../api/functions/graphrag-index-operations-extract-graph-typing-repr)

