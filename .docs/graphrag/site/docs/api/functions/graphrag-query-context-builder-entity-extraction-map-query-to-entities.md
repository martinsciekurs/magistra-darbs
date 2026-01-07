---
sidebar_position: 331
---

# map_query_to_entities

**File:** `graphrag/query/context_builder/entity_extraction.py` (lines 37-92)

## Signature

```python
def map_query_to_entities(
    query: str,
    text_embedding_vectorstore: BaseVectorStore,
    text_embedder: EmbeddingModel,
    all_entities_dict: dict[str, Entity],
    embedding_vectorstore_key: str = EntityVectorStoreKey.ID,
    include_entity_names: list[str] | None = None,
    exclude_entity_names: list[str] | None = None,
    k: int = 10,
    oversample_scaler: int = 2,
) -> list[Entity]
```

## Description

Extracts entities that match a given query using semantic similarity between the query and entity descriptions, with optional explicit inclusion or exclusion of entities.

Args:
    query: str. The query string to search for relevant entities. If empty, top-ranked entities by rank are returned.
    text_embedding_vectorstore: BaseVectorStore. The vector store used to perform semantic similarity search over entity descriptions.
    text_embedder: EmbeddingModel. The embedding model used to encode text for similarity search.
    all_entities_dict: dict[str, Entity]. Mapping of entity IDs to Entity objects.
    embedding_vectorstore_key: str. Key used to extract the corresponding field from embedding results (e.g., "id" or "title"). Default EntityVectorStoreKey.ID.
    include_entity_names: list[str] | None. Names of entities to explicitly include. If provided, those entities are retrieved and prepended to the final results.
    exclude_entity_names: list[str] | None. Names of entities to exclude from the matched results portion.
    k: int. Number of top results to consider when a non-empty query is provided (before exclusions/inclusions). When the query is empty, this caps the number of top-ranked entities.
    oversample_scaler: int. Multiplier to oversample results to account for potential exclusions.

Returns:
    list[Entity]. The selected entities, with explicitly included entities first, followed by the matched or top-ranked entities. Note that included entities are not filtered by exclude_entity_names, and duplicates between the two groups may occur.

Raises:
    AttributeError: May be raised by underlying retrieval helpers if an expected attribute is missing on an Entity or in a retrieved result. This behavior is not guaranteed by the function's signature.

## Dependencies

This function calls:

- `graphrag/query/input/retrieval/entities.py::get_entity_by_id`
- `graphrag/query/input/retrieval/entities.py::get_entity_by_key`
- `graphrag/query/input/retrieval/entities.py::get_entity_by_name`

## Called By

This function is called by:

- `graphrag/query/structured_search/local_search/mixed_context.py::LocalSearchMixedContext.build_context`
- `tests/unit/query/context_builder/test_entity_extraction.py::test_map_query_to_entities`

