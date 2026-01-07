---
sidebar_position: 89
---

# BasicSearch

**File:** `graphrag/query/structured_search/basic_search/search.py`

## Overview

BasicSearch orchestrates the construction of a single-context-window search context and the generation (or streaming) of an answer for a user query.

Purpose and responsibility:
- Build a single-context-window search context
- Orchestrate a language model (ChatModel) with a BasicContextBuilder to produce results
- Support both full result generation via search and streaming output via stream_search

Key attributes inferred from initialization:
- model: The language model interface used for this basic search.
- context_builder: The builder that constructs the context for the search.
- tokenizer: Optional tokenizer to use.
- system_prompt: System prompt for the search. If None, a default system prompt is used.
- response_type: The type/format of the response. Default is "multiple paragraphs".
- callbacks: Optional list of QueryCallbacks to handle events during search.
- model_params: Additional parameters passed to the model.
- context_builder_params: Additional parameters passed to the context builder.

Args:
model: The language model interface used for this basic search.
context_builder: The builder that constructs the context for the search.
tokenizer: Optional tokenizer to use.
system_prompt: System prompt for the search. If None, the default system prompt is used.
response_type: The type of response formatting. Default is "multiple paragraphs".
callbacks: Optional list of QueryCallbacks to be invoked during search.
model_params: Additional parameters passed to the model.
context_builder_params: Additional parameters passed to the context builder.

Returns:
None: This initializer does not return a value.

Raises:
Exceptions raised by the underlying components (e.g., ChatModel, BasicContextBuilder) may be propagated to the caller.

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

### `stream_search`

```python
def stream_search(
        self,
        query: str,
        conversation_history: ConversationHistory | None = None,
    ) -> AsyncGenerator[str, None]
```

### `__init__`

```python
def __init__(
        self,
        model: ChatModel,
        context_builder: BasicContextBuilder,
        tokenizer: Tokenizer | None = None,
        system_prompt: str | None = None,
        response_type: str = "multiple paragraphs",
        callbacks: list[QueryCallbacks] | None = None,
        model_params: dict[str, Any] | None = None,
        context_builder_params: dict | None = None,
    )
```

