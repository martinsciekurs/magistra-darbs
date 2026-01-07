---
sidebar_position: 22
---

# LocalSearch

**File:** `graphrag/query/structured_search/local_search/search.py`

## Overview

LocalSearch orchestrates local search operations by building a compact context and querying a language model to generate an answer for a user query. It coordinates the context builder, optional tokenizer, system prompt, and callbacks to produce a structured search result or a streaming output.

Purpose:
- Build a local search context that fits a single context window and generates an answer for the user query.

Args:
    model: The language model interface used for this local search.
    context_builder: The builder that constructs the context for the local search.
    tokenizer: Optional tokenizer to use.
    system_prompt: System prompt for the local search. If None, uses the default system prompt.
    response_type: The format of the response produced by the search.
    callbacks: The query callbacks to be invoked during search.
    model_params: Parameters for the underlying language model.
    context_builder_params: Parameters for the context builder.

Returns:
- LocalSearch: An initialized LocalSearch instance.

Raises:
- Exceptions from the underlying components (model, tokenizer, context builder) may propagate to the caller.

## Methods

### `search`

```python
def search(
        self,
        query: str,
        conversation_history: ConversationHistory | None = None,
        **kwargs,
    ) -> SearchResult
```

### `__init__`

```python
def __init__(
        self,
        model: ChatModel,
        context_builder: LocalContextBuilder,
        tokenizer: Tokenizer | None = None,
        system_prompt: str | None = None,
        response_type: str = "multiple paragraphs",
        callbacks: list[QueryCallbacks] | None = None,
        model_params: dict[str, Any] | None = None,
        context_builder_params: dict | None = None,
    )
```

### `stream_search`

```python
def stream_search(
        self,
        query: str,
        conversation_history: ConversationHistory | None = None,
    ) -> AsyncGenerator
```

