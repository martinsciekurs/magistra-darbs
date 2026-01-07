---
sidebar_position: 342
---

# get_global_search_engine

**File:** `graphrag/query/factory.py` (lines 111-192)

## Signature

```python
def get_global_search_engine(
    config: GraphRagConfig,
    reports: list[CommunityReport],
    entities: list[Entity],
    communities: list[Community],
    response_type: str,
    dynamic_community_selection: bool = False,
    map_system_prompt: str | None = None,
    reduce_system_prompt: str | None = None,
    general_knowledge_inclusion_prompt: str | None = None,
    callbacks: list[QueryCallbacks] | None = None,
) -> GlobalSearch
```

## Description

Create a global search engine based on data + configuration.

Args:
    config (GraphRagConfig): GraphRag configuration object containing global search settings used to configure the global search engine and models.
    reports (list[CommunityReport]): Community reports to be used by the global search context.
    entities (list[Entity]): Entities to be included in the global search context.
    communities (list[Community]): Communities to be included in the global search context.
    response_type (str): Response type to be used by the global search engine.
    dynamic_community_selection (bool): Whether to enable dynamic community selection for the global search.
    map_system_prompt (str | None): Optional system prompt used for mapping in the global search.
    reduce_system_prompt (str | None): Optional system prompt used to reduce content for the global search.
    general_knowledge_inclusion_prompt (str | None): Optional prompt to include general knowledge in the global search.
    callbacks (list[QueryCallbacks] | None): Optional callbacks to handle query events during global search.

Returns:
    GlobalSearch: A GlobalSearch instance configured with the provided data and settings.

## Dependencies

This function calls:

- `graphrag/language_model/manager.py::ModelManager`
- `graphrag/language_model/providers/fnllm/utils.py::get_openai_model_parameters_from_config`
- `graphrag/query/structured_search/global_search/community_context.py::GlobalCommunityContext`
- `graphrag/query/structured_search/global_search/search.py::GlobalSearch`
- `graphrag/tokenizer/get_tokenizer.py::get_tokenizer`

## Called By

This function is called by:

- `graphrag/api/query.py::global_search_streaming`

