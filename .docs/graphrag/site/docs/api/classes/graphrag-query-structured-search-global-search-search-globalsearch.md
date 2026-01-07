---
sidebar_position: 32
---

# GlobalSearch

**File:** `graphrag/query/structured_search/global_search/search.py`

## Overview

GlobalSearch orchestrates a multi-step global search by querying multiple batches of community reports in parallel and reducing the results into a final answer.

Purpose:
Perform a structured global search by running parallel language model calls on batches of short summaries and then combining those results to produce a final answer.

Key attributes:
- model: ChatModel - The language model interface used for this global search.
- context_builder: GlobalContextBuilder - The builder that constructs the context for the search.
- tokenizer: Tokenizer | None - Optional tokenizer to use; if None, a default tokenizer will be used.
- map_system_prompt: str | None - System prompt for the mapping stage.
- reduce_system_prompt: str | None - System prompt for the reducing stage.
- response_type: str - The response format; default "multiple paragraphs".
- allow_general_knowledge: bool - Whether general knowledge is allowed during responses.
- general_knowledge_inclusion_prompt: str | None - Prompt to include general knowledge in responses.
- json_mode: bool - If True, use JSON-based parsing for responses.
- callbacks: list[QueryCallbacks] | None - Callbacks invoked during processing.
- max_data_tokens: int - Maximum tokens used for data pieces.
- map_llm_params: dict[str, Any] | None - Parameters for map phase LLM calls.
- reduce_llm_params: dict[str, Any] | None - Parameters for reduce phase LLM calls.
- map_max_length: int - Maximum length for map outputs.
- reduce_max_length: int - Maximum length for reduce outputs.
- context_builder_params: dict[str, Any] | None - Parameters for the context builder.
- concurrent_coroutines: int - Number of concurrent coroutines to run.

Args:
- model: ChatModel - The language model interface used for this global search.
- context_builder: GlobalContextBuilder - The builder that constructs the context for the search.
- tokenizer: Tokenizer | None - Optional tokenizer to use; if None, a default tokenizer will be used.
- map_system_prompt: str | None - System prompt for the mapping stage.
- reduce_system_prompt: str | None - System prompt for the reducing stage.
- response_type: str - The response format; default "multiple paragraphs".
- allow_general_knowledge: bool - Whether general knowledge is allowed during responses.
- general_knowledge_inclusion_prompt: str | None - Prompt to include general knowledge in responses.
- json_mode: bool - Whether to parse responses as JSON.
- callbacks: list[QueryCallbacks] | None - Callbacks invoked during processing.
- max_data_tokens: int - Maximum tokens used for data pieces.
- map_llm_params: dict[str, Any] | None - Parameters for map phase LLM calls.
- reduce_llm_params: dict[str, Any] | None - Parameters for reduce phase LLM calls.
- map_max_length: int - Maximum length for map outputs.
- reduce_max_length: int - Maximum length for reduce outputs.
- context_builder_params: dict[str, Any] | None - Parameters for the context builder.
- concurrent_coroutines: int - Number of concurrent coroutines to run.

Returns:
None.

Raises:
Exceptions raised by underlying components (e.g., ChatModel, GlobalContextBuilder, Tokenizer) may propagate.

## Methods

### `__init__`

```python
def __init__(
        self,
        model: ChatModel,
        context_builder: GlobalContextBuilder,
        tokenizer: Tokenizer | None = None,
        map_system_prompt: str | None = None,
        reduce_system_prompt: str | None = None,
        response_type: str = "multiple paragraphs",
        allow_general_knowledge: bool = False,
        general_knowledge_inclusion_prompt: str | None = None,
        json_mode: bool = True,
        callbacks: list[QueryCallbacks] | None = None,
        max_data_tokens: int = 8000,
        map_llm_params: dict[str, Any] | None = None,
        reduce_llm_params: dict[str, Any] | None = None,
        map_max_length: int = 1000,
        reduce_max_length: int = 2000,
        context_builder_params: dict[str, Any] | None = None,
        concurrent_coroutines: int = 32,
    )
```

### `search`

```python
def search(
        self,
        query: str,
        conversation_history: ConversationHistory | None = None,
        **kwargs: Any,
    ) -> GlobalSearchResult
```

### `_map_response_single_batch`

```python
def _map_response_single_batch(
        self,
        context_data: str,
        query: str,
        max_length: int,
        **llm_kwargs,
    ) -> SearchResult
```

### `_stream_reduce_response`

```python
def _stream_reduce_response(
        self,
        map_responses: list[SearchResult],
        query: str,
        max_length: int,
        **llm_kwargs,
    ) -> AsyncGenerator[str, None]
```

### `stream_search`

```python
def stream_search(
        self,
        query: str,
        conversation_history: ConversationHistory | None = None,
    ) -> AsyncGenerator[str, None]
```

### `_reduce_response`

```python
def _reduce_response(
        self,
        map_responses: list[SearchResult],
        query: str,
        **llm_kwargs,
    ) -> SearchResult
```

### `_parse_search_response`

```python
def _parse_search_response(self, search_response: str) -> list[dict[str, Any]]
```

