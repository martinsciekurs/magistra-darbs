---
sidebar_position: 24
---

# QueryCallbacks

**File:** `graphrag/callbacks/query_callbacks.py`

## Overview

QueryCallbacks is a base class that defines callback hooks used during a query processing workflow involving map and reduce operations and interactions with a language model.

Purpose:
    Provide default, overridable callback methods for lifecycle events such as starting and ending map and reduce operations, handling new tokens from the LLM, and processing context data.

Key attributes:
    None documented. This class does not define persistent state in the provided data.

Summary:
    The class declares the following callback methods:
    - on_reduce_response_start(reduce_response_context: str | dict[str, Any]) -&gt; None
    - on_llm_new_token(token) -&gt; None
    - on_map_response_end(map_response_outputs: list[SearchResult]) -&gt; None
    - on_map_response_start(map_response_contexts: list[str]) -&gt; None
    - on_context(context: Any) -&gt; None
    - on_reduce_response_end(reduce_response_output: str) -&gt; None

    Subclasses may override these methods to implement custom side effects. In particular, on_map_response_end and on_context describe no-op default behavior.

## Methods

### `on_reduce_response_start`

```python
def on_reduce_response_start(
        self, reduce_response_context: str | dict[str, Any]
    ) -> None
```

### `on_llm_new_token`

```python
def on_llm_new_token(self, token) -> None
```

### `on_map_response_end`

```python
def on_map_response_end(self, map_response_outputs: list[SearchResult]) -> None
```

### `on_map_response_start`

```python
def on_map_response_start(self, map_response_contexts: list[str]) -> None
```

### `on_context`

```python
def on_context(self, context: Any) -> None
```

### `on_reduce_response_end`

```python
def on_reduce_response_end(self, reduce_response_output: str) -> None
```

