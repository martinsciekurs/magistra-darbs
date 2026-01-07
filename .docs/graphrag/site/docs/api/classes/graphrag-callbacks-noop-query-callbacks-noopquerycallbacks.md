---
sidebar_position: 8
---

# NoopQueryCallbacks

**File:** `graphrag/callbacks/noop_query_callbacks.py`

## Overview

NoopQueryCallbacks is a no-op implementation of the QueryCallbacks interface used for query callback events. It deliberately performs no actions and maintains no internal state.

Args:
  None: This class has no constructor parameters.

Returns:
  None: The class does not return a value.

Raises:
  None: This class does not raise exceptions by itself.

Attributes:
  None: This class maintains no internal state.

## Methods

### `on_map_response_start`

```python
def on_map_response_start(self, map_response_contexts: list[str]) -> None
```

### `on_llm_new_token`

```python
def on_llm_new_token(self, token)
```

### `on_context`

```python
def on_context(self, context: Any) -> None
```

### `on_reduce_response_start`

```python
def on_reduce_response_start(
        self, reduce_response_context: str | dict[str, Any]
    ) -> None
```

### `on_map_response_end`

```python
def on_map_response_end(self, map_response_outputs: list[SearchResult]) -> None
```

### `on_reduce_response_end`

```python
def on_reduce_response_end(self, reduce_response_output: str) -> None
```

