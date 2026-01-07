---
sidebar_position: 556
---

# test_map_query_to_entities

**File:** `tests/unit/query/context_builder/test_entity_extraction.py` (lines 66-190)

## Signature

```python
def test_map_query_to_entities()
```

## Description

Maps a user query to the corresponding Entity objects by performing a semantic similarity search over a vector store of entity descriptions and mapping the retrieved documents back to Entity records.

Args:
- query: str. The query string to search for relevant entities. If empty, the function returns the top-k entities ordered by rank (see oversample_scaler for behavior when non-empty).
- text_embedding_vectorstore: BaseVectorStore. The vector store used to perform semantic similarity search over entity descriptions.
- text_embedder: EmbeddingModel. The model used to encode the query into an embedding for similarity search.
- all_entities_dict: dict[str, Entity]. Mapping from the vector-store document identifiers (as determined by embedding_vectorstore_key) to the corresponding Entity objects.
- embedding_vectorstore_key: str. Key indicating how documents in text_embedding_vectorstore identify an entity (for example, EntityVectorStoreKey.ID or EntityVectorStoreKey.TITLE).
- include_entity_names: list[str] | None. Optional list of entity titles/names to explicitly include in the results.
- exclude_entity_names: list[str] | None. Optional list of entity titles/names to exclude from the results.
- k: int. Maximum number of entities to return. If query is empty, up to k entities are returned, ordered by rank with the highest rank first.
- oversample_scaler: int. Multiplier controlling how many candidate documents to fetch beyond k to improve robustness of the top-k selection. A value of 1 disables oversampling; higher values fetch more candidates. Default in the implementation is 2, but tests may override this.

Returns:
- list[Entity]. The matched Entity objects, in the order determined by the search and ranking, up to length k.

Raises:
- ValueError: If k &lt;= 0 or oversample_scaler &lt; 1.
- KeyError: If a retrieved document’s identifier cannot be found in all_entities_dict.
- TypeError: If argument types are invalid.

Notes:
- Vector-store to-entity mapping depends on embedding_vectorstore_key. When embedding_vectorstore_key is ID, documents store the Entity.id; when TITLE, documents store the Entity.title. This mapping is how the function resolves a document back to an Entity.
- Edge cases:
  - Empty query returns the top-k entities by rank (highest numeric rank first).
  - If no candidates are produced or all candidates are filtered out, an empty list is returned.

Example notes:
- If embedding_vectorstore_key is EntityVectorStoreKey.ID and a document has id equal to an Entity.id, map_query_to_entities will return the corresponding Entity from all_entities_dict.
- If embedding_vectorstore_key is EntityVectorStoreKey.TITLE and a document has id equal to an Entity.title, the function will resolve to that Entity via all_entities_dict.

## Dependencies

This function calls:

- `graphrag/data_model/entity.py::Entity`
- `graphrag/language_model/manager.py::ModelManager`
- `graphrag/query/context_builder/entity_extraction.py::map_query_to_entities`
- `graphrag/vector_stores/base.py::VectorStoreDocument`

