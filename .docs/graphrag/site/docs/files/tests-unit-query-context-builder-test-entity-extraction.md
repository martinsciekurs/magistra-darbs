---
sidebar_position: 263
---

# tests/unit/query/context_builder/test_entity_extraction.py

## Overview

Tests for entity extraction and context-building in queries.

Purpose:
Verify that map_query_to_entities correctly maps a user’s query to Entity instances by performing a semantic similarity search over a mock vector store and translating the results back into Entity records. This is exercised via EntityVectorStoreKey and related utilities in graphrag.query.context_builder.entity_extraction.

Key exports:
- MockBaseVectorStore: A lightweight, in-memory vector store used for testing. Public methods: connect, filter_by_id, similarity_search_by_text, load_documents, similarity_search_by_vector, search_by_id.
- EntityVectorStoreKey: Utility used in tests to construct vector store keys for entity-related lookups.
- map_query_to_entities: Function under test that maps a query to a list of Entity objects by querying the mock vector store and mapping documents to entities.

Brief summary:
The tests rely on deterministic VectorStoreDocument and VectorStoreSearchResult instances and predefined constants to ensure consistent behavior when mapping from query to entities.

## Classes

- [`MockBaseVectorStore`](../api/classes/tests-unit-query-context-builder-test-entity-extraction-mockbasevectorstore)

## Functions

- [`connect`](../api/functions/tests-unit-query-context-builder-test-entity-extraction-connect)
- [`__init__`](../api/functions/tests-unit-query-context-builder-test-entity-extraction-init)
- [`filter_by_id`](../api/functions/tests-unit-query-context-builder-test-entity-extraction-filter-by-id)
- [`similarity_search_by_text`](../api/functions/tests-unit-query-context-builder-test-entity-extraction-similarity-search-by-text)
- [`load_documents`](../api/functions/tests-unit-query-context-builder-test-entity-extraction-load-documents)
- [`similarity_search_by_vector`](../api/functions/tests-unit-query-context-builder-test-entity-extraction-similarity-search-by-vector)
- [`search_by_id`](../api/functions/tests-unit-query-context-builder-test-entity-extraction-search-by-id)
- [`test_map_query_to_entities`](../api/functions/tests-unit-query-context-builder-test-entity-extraction-test-map-query-to-entities)

