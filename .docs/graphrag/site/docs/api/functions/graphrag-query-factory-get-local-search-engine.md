---
sidebar_position: 341
---

# get_local_search_engine

**File:** `graphrag/query/factory.py` (lines 39-108)

## Signature

```python
def get_local_search_engine(
    config: GraphRagConfig,
    reports: list[CommunityReport],
    text_units: list[TextUnit],
    entities: list[Entity],
    relationships: list[Relationship],
    covariates: dict[str, list[Covariate]],
    response_type: str,
    description_embedding_store: BaseVectorStore,
    system_prompt: str | None = None,
    callbacks: list[QueryCallbacks] | None = None,
) -> LocalSearch
```

## Description

Create a local search engine based on data + configuration.

Args:
    config: GraphRagConfig
        GraphRag configuration object containing local search settings used to configure the search engine and models.
    reports: list[CommunityReport]
        Community reports to be used by the local search engine context.
    text_units: list[TextUnit]
        Text units to be included in the search context.
    entities: list[Entity]
        Entities to be considered in the search context.
    relationships: list[Relationship]
        Relationships to be considered in the search context.
    covariates: dict[str, list[Covariate]]
        Covariates to augment context for the local search.
    response_type: str
        Type of response to return from the search engine.
    description_embedding_store: BaseVectorStore
        Vector store containing description embeddings for entities.
    system_prompt: str | None
        Optional system prompt to guide the local search model.
    callbacks: list[QueryCallbacks] | None
        Optional list of query callbacks to execute during search.

Returns:
    LocalSearch
        A configured LocalSearch instance ready to execute queries.

Raises:
    Exception
        If an error occurs during model initialization or tokenizer setup.

## Dependencies

This function calls:

- `graphrag/language_model/manager.py::ModelManager`
- `graphrag/language_model/providers/fnllm/utils.py::get_openai_model_parameters_from_config`
- `graphrag/query/structured_search/local_search/mixed_context.py::LocalSearchMixedContext`
- `graphrag/query/structured_search/local_search/search.py::LocalSearch`
- `graphrag/tokenizer/get_tokenizer.py::get_tokenizer`

## Called By

This function is called by:

- `graphrag/api/query.py::local_search_streaming`

