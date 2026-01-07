---
sidebar_position: 74
---

# graphrag/index/operations/finalize_entities.py

## Overview

Module to finalize entity records by constructing graphs from relationships and applying optional embedding and layout.

This module exposes the finalize_entities function, which orchestrates graph-based transformations to produce final entity records from input entities and relationships. It builds a graph from the provided relationships, optionally embeds the graph, applies a layout when requested, and attaches unique identifiers to each entity. The function returns a pandas DataFrame representing the final entities.

Exports:
  finalize_entities: Finalizes input entities into the final entity records by building a graph from relationships and applying embedding and layout as configured.

## Functions

- [`finalize_entities`](../api/functions/graphrag-index-operations-finalize-entities-finalize-entities)

