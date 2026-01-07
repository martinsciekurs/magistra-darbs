---
sidebar_position: 28
---

# BaseSearch

**File:** `graphrag/query/structured_search/base.py`

## Overview

Abstract base class for structured searches using a language model and contextual builders.

This ABC defines the interface and provides common configuration for search implementations that operate with a ChatModel, a context builder, and an optional tokenizer. It also holds optional parameter dictionaries for both the model and the context builder.

Key attributes:
  model: The language model interface used for this base search.
  context_builder: The builder that constructs the context for the search (generic type T).
  tokenizer: Optional tokenizer to use. If None, a tokenizer is selected via get_tokenizer().
  model_params: Optional dictionary of parameters to configure the language model.
  context_builder_params: Optional dictionary of parameters to configure the context builder.

Args:
  model: The language model interface used for this base search.
  context_builder: The builder that constructs the context for the search.
  tokenizer: Optional tokenizer to use. If None, a tokenizer is selected via get_tokenizer().
  model_params: Optional dictionary of parameters to configure the language model.
  context_builder_params: Optional dictionary of parameters to configure the context builder.

Raises:
  NotImplementedError: Subclasses must implement the abstract methods search and stream_search.

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
        context_builder: T,
        tokenizer: Tokenizer | None = None,
        model_params: dict[str, Any] | None = None,
        context_builder_params: dict[str, Any] | None = None,
    )
```

