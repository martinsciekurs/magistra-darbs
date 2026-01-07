---
sidebar_position: 186
---

# graphrag/query/context_builder/entity_extraction.py

## Overview

Graphrag query context: entity extraction utilities for mapping user queries to Entity objects using vector stores and a relationship graph.

Overview
This module provides utilities to extract entities from a user query and map them to Entity objects within Graphrag's query context. It defines an EntityVectorStoreKey Enum to identify how entity vectors are stored in a vector store, and top-level constants ID and TITLE for compatibility. The utilities rely on the Entity and Relationship data models, an EmbeddingModel protocol, a BaseVectorStore interface, and helper retrieval helpers (get_entity_by_id, get_entity_by_key, get_entity_by_name).

Exports
- EntityVectorStoreKey: Enum defining how entity vectors are addressed in a vector store (ID and TITLE).
- ID: string constant for the "id" key.
- TITLE: string constant for the "title" key.
- from_string(value: str) -&gt; EntityVectorStoreKey: convert a string key to the corresponding enum member.
- find_nearest_neighbors_by_entity_rank(entity_name: str, all_entities: list[Entity], all_relationships: list[Relationship], exclude_entity_names: list[str] | None = None, k: int | None = 10) -&gt; list[Entity]: retrieve entities directly connected to the target entity, ranked, with optional exclusions.
- map_query_to_entities(query: str, text_embedding_vectorstore: BaseVectorStore, text_embedder: EmbeddingModel, all_entities_dict: dict[str, Entity], embedding_vectorstore_key: str = EntityVectorStoreKey.ID, include_entity_names: list[str] | None = None, exclude_entity_names: list[str] | None = None, k: int = 10, oversample_scaler: int = 2) -&gt; list[Entity]: obtain entities matching a query via semantic similarity with optional inclusion/exclusion filters and oversampling.

Key concepts
- EntityVectorStoreKey Enum vs top-level ID/TITLE constants: the enum provides a programmatic way to reference the vector key, while the ID and TITLE constants offer straightforward string values for external usage. Use embedding_vectorstore_key to select which field to search against in the vector store.
- Edge cases: an empty query may return top-ranked entities by rank; exclusion lists remove specified names from results; include lists restrict results to a subset; oversample_scaler controls candidate expansion for robustness. Functions raise appropriate exceptions for invalid inputs (e.g., invalid keys, non-positive k or oversample values).

Usage example
- Convert a key string to enum: from_string("id") -&gt; EntityVectorStoreKey.ID.
- Find neighbors: find_nearest_neighbors_by_entity_rank("Invoice", all_entities, all_relationships, k=5).
- Map a query to entities: map_query_to_entities("find all related products", vectorstore, embedder, entities_by_id, embedding_vectorstore_key=EntityVectorStoreKey.TITLE, k=8).

## Classes

- [`EntityVectorStoreKey`](../api/classes/graphrag-query-context-builder-entity-extraction-entityvectorstorekey)

## Functions

- [`from_string`](../api/functions/graphrag-query-context-builder-entity-extraction-from-string)
- [`find_nearest_neighbors_by_entity_rank`](../api/functions/graphrag-query-context-builder-entity-extraction-find-nearest-neighbors-by-entity-rank)
- [`map_query_to_entities`](../api/functions/graphrag-query-context-builder-entity-extraction-map-query-to-entities)

