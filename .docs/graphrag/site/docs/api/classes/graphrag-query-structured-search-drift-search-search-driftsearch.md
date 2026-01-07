---
sidebar_position: 11
---

# DRIFTSearch

**File:** `graphrag/query/structured_search/drift_search/search.py`

## Overview

DRIFTSearch orchestrates the DRIFT-style search workflow for structured queries by coordinating a language model, a DRIFT context builder, and local search components to iteratively refine results.

Purpose:
- Manage the end-to-end DRIFT search lifecycle, including initialization, prompt construction, local search steps, result aggregation, and optional streaming.

Key responsibilities:
- Wire together the language model interface, DRIFT context handling, tokenization, and the query lifecycle.
- Expose methods to initialize local search, perform search steps, and stream results.
- Coordinate reduction of model responses into a final answer and intermediate actions.

Key attributes (inferred from constructor and methods):
- model: The ChatModel used to interact with the language model.
- context_builder: DRIFTSearchContextBuilder housing configuration and DRIFT context.
- tokenizer: Optional Tokenizer used for token handling and prompting/streaming.
- query_state: Optional QueryState tracking the current query status and results.
- callbacks: Optional list[QueryCallbacks] for query lifecycle events.

Notes:
- This class delegates most operational logic to specialized components (e.g., LocalSearch, DRIFTPrimer) to implement the DRIFT workflow.

Raises:
- None. This class does not raise exceptions; errors from underlying components may propagate to callers.

## Methods

### `_reduce_response`

```python
def _reduce_response(
        self,
        responses: str | dict[str, Any],
        query: str,
        llm_calls: dict[str, int],
        prompt_tokens: dict[str, int],
        output_tokens: dict[str, int],
        **llm_kwargs,
    ) -> str
```

### `_process_primer_results`

```python
def _process_primer_results(
        self, query: str, search_results: SearchResult
    ) -> DriftAction
```

### `_search_step`

```python
def _search_step(
        self, global_query: str, search_engine: LocalSearch, actions: list[DriftAction]
    ) -> list[DriftAction]
```

### `_reduce_response_streaming`

```python
def _reduce_response_streaming(
        self,
        responses: str | dict[str, Any],
        query: str,
        model_params: dict[str, Any],
    ) -> AsyncGenerator[str, None]
```

### `__init__`

```python
def __init__(
        self,
        model: ChatModel,
        context_builder: DRIFTSearchContextBuilder,
        tokenizer: Tokenizer | None = None,
        query_state: QueryState | None = None,
        callbacks: list[QueryCallbacks] | None = None,
    )
```

### `init_local_search`

```python
def init_local_search(self) -> LocalSearch
```

### `search`

```python
def search(
        self,
        query: str,
        conversation_history: Any = None,
        reduce: bool = True,
        **kwargs,
    ) -> SearchResult
```

### `stream_search`

```python
def stream_search(
        self, query: str, conversation_history: ConversationHistory | None = None
    ) -> AsyncGenerator[str, None]
```

