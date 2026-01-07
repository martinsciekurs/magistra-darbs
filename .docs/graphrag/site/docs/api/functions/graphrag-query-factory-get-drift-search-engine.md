---
sidebar_position: 340
---

# get_drift_search_engine

**File:** `graphrag/query/factory.py` (lines 195-247)

## Signature

```python
def get_drift_search_engine(
    config: GraphRagConfig,
    reports: list[CommunityReport],
    text_units: list[TextUnit],
    entities: list[Entity],
    relationships: list[Relationship],
    description_embedding_store: BaseVectorStore,
    response_type: str,
    local_system_prompt: str | None = None,
    reduce_system_prompt: str | None = None,
    callbacks: list[QueryCallbacks] | None = None,
) -> DRIFTSearch
```

## Description

Create a local drift search engine based on data + configuration.

Args:
    config: GraphRagConfig
        GraphRag configuration object containing drift_search settings used to configure the search engine and models.
    reports: list[CommunityReport]
        Community reports to be used by the search context.
    text_units: list[TextUnit]
        Text units to be included in the search context.
    entities: list[Entity]
        Entities to be included in the search context.
    relationships: list[Relationship]
        Relationships to be included in the search context.
    description_embedding_store: BaseVectorStore
        Vector store of text embeddings for entity descriptions.
    response_type: str
        Type of response to generate.
    local_system_prompt: str | None
        Optional system prompt to be used locally for prompt construction.
    reduce_system_prompt: str | None
        Optional reduced system prompt for shorter prompts.
    callbacks: list[QueryCallbacks] | None
        Optional query callbacks to handle search events.

Returns:
    DRIFTSearch
        A configured DRIFTSearch instance ready to execute drift-based searches.

Raises:
    None

## Dependencies

This function calls:

- `graphrag/language_model/manager.py::ModelManager`
- `graphrag/query/structured_search/drift_search/drift_context.py::DRIFTSearchContextBuilder`
- `graphrag/query/structured_search/drift_search/search.py::DRIFTSearch`
- `graphrag/tokenizer/get_tokenizer.py::get_tokenizer`

## Called By

This function is called by:

- `graphrag/api/query.py::drift_search_streaming`

