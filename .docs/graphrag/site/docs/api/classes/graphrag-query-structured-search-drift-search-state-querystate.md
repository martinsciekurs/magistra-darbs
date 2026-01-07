---
sidebar_position: 9
---

# QueryState

**File:** `graphrag/query/structured_search/drift_search/state.py`

## Overview

Represents the state of a drift search query as a graph of DriftAction nodes.

Args:
    self: The instance being initialized. This class is instantiated without external parameters.

Returns:
    None

Raises:
    None

Purpose/responsibility:
    Manage a directed graph of DriftAction nodes, enabling addition of actions, linking follow-ups, serialization/deserialization, and ranking of incomplete actions during structured drift search.

Key attributes:
    graph (nx.DiGraph): The directed graph storing DriftAction nodes and their relationships. Each node carries metadata with keys 'llm_calls', 'prompt_tokens', and 'output_tokens'.

## Methods

### `action_token_ct`

```python
def action_token_ct(self) -> dict[str, int]
```

### `__init__`

```python
def __init__(self)
```

### `serialize`

```python
def serialize(
        self, include_context: bool = True
    ) -> dict[str, Any] | tuple[dict[str, Any], dict[str, Any], str]
```

### `find_incomplete_actions`

```python
def find_incomplete_actions(self) -> list[DriftAction]
```

### `add_action`

```python
def add_action(self, action: DriftAction, metadata: dict[str, Any] | None = None)
```

### `add_all_follow_ups`

```python
def add_all_follow_ups(
        self,
        action: DriftAction,
        follow_ups: list[DriftAction] | list[str],
        weight: float = 1.0,
    )
```

### `deserialize`

```python
def deserialize(self, data: dict[str, Any])
```

### `relate_actions`

```python
def relate_actions(
        self, parent: DriftAction, child: DriftAction, weight: float = 1.0
    )
```

### `rank_incomplete_actions`

```python
def rank_incomplete_actions(
        self, scorer: Callable[[DriftAction], float] | None = None
    ) -> list[DriftAction]
```

