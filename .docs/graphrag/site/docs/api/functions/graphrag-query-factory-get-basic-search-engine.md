---
sidebar_position: 343
---

# get_basic_search_engine

**File:** `graphrag/query/factory.py` (lines 250-303)

## Signature

```python
def get_basic_search_engine(
    text_units: list[TextUnit],
    text_unit_embeddings: BaseVectorStore,
    config: GraphRagConfig,
    system_prompt: str | None = None,
    response_type: str = "multiple paragraphs",
    callbacks: list[QueryCallbacks] | None = None,
) -> BasicSearch
```

## Description

Create a basic search engine based on data + configuration.

Args:
    text_units (list[TextUnit]): Text units to be included in the search context.
    text_unit_embeddings (BaseVectorStore): Vector store for text unit embeddings.
    config (GraphRagConfig): GraphRag configuration containing basic_search settings.
    system_prompt (str | None): Optional system prompt to override the default prompt.
    response_type (str): Type of response to generate. Default: "multiple paragraphs".
    callbacks (list[QueryCallbacks] | None): Optional callbacks for query handling.

Returns:
    BasicSearch: A configured BasicSearch instance.

## Dependencies

This function calls:

- `graphrag/language_model/manager.py::ModelManager`
- `graphrag/language_model/providers/fnllm/utils.py::get_openai_model_parameters_from_config`
- `graphrag/query/structured_search/basic_search/basic_context.py::BasicSearchContext`
- `graphrag/query/structured_search/basic_search/search.py::BasicSearch`
- `graphrag/tokenizer/get_tokenizer.py::get_tokenizer`

## Called By

This function is called by:

- `graphrag/api/query.py::basic_search_streaming`

