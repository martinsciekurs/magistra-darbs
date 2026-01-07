---
sidebar_position: 117
---

# PrimerQueryProcessor

**File:** `graphrag/query/structured_search/drift_search/primer.py`

## Overview

PrimerQueryProcessor expands a user query using a randomly selected community report template and computes its embedding with the provided models. It processes a single query per call.

Args:
    chat_model (ChatModel): The language model used to expand the query into an augmented form via a randomized template.
    text_embedder (EmbeddingModel): The embedding model used to compute the dense vector for the expanded query.
    reports (list[CommunityReport]): A list of CommunityReport instances used as templates for expansion.
    tokenizer (Tokenizer | None): Optional tokenizer to count tokens during expansion and embedding.

Returns:
    None

Raises:
    ValueError, TypeError, RuntimeError: If inputs are invalid or underlying models fail.

Methods:
    __call__(self, query: str) -&gt; tuple[list[float], dict[str, int]]
        Process a single query by expanding it (via expand_query) and then computing its embedding.
        Returns:
            embedding (list[float]): The embedding vector produced by text_embedder.
            token_usage (dict[str, int]): Token usage details from the expansion/embedding process (e.g., llm_calls, prompt_tokens, output_tokens).

    expand_query(self, query: str) -&gt; tuple[str, dict[str, int]]
        Expand the input query using a randomly selected community report template.
        Returns:
            expanded_query (str): The expanded query text.
            token_usage (dict[str, int]): Token usage details from the expansion step (e.g., llm_calls, prompt_tokens, output_tokens).

## Methods

### `__call__`

```python
def __call__(self, query: str) -> tuple[list[float], dict[str, int]]
```

### `expand_query`

```python
def expand_query(self, query: str) -> tuple[str, dict[str, int]]
```

### `__init__`

```python
def __init__(
        self,
        chat_model: ChatModel,
        text_embedder: EmbeddingModel,
        reports: list[CommunityReport],
        tokenizer: Tokenizer | None = None,
    )
```

