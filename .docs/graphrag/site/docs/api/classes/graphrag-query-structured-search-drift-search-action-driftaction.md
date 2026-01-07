---
sidebar_position: 5
---

# DriftAction

**File:** `graphrag/query/structured_search/drift_search/action.py`

## Overview

DriftAction represents a single drift action within a structured drift search workflow. It encapsulates a query, an optional answer, and an optional list of follow-up actions, and it carries a score that may be computed later by a scorer.

Args:
  query (str): The query for the action.
  answer (Optional[str]): The answer to the query, if available.
  follow_ups (Optional[List['DriftAction']]): A list of follow-up actions.

Attributes:
  query (str): The action's query string.
  answer (Optional[str]): The answer to the query, if available.
  follow_ups (Optional[List['DriftAction']]): Nested follow-up actions.
  score (Optional[float]): The computed score for this action. May be None before scoring.

Notes:
  score is initialized to None. Use compute_score(scorer) to assign a numeric score based on the query and answer; if the scorer returns None, score remains None.

Notable methods:
  compute_score(scorer): Compute and assign the action's score using the provided scorer.
  __hash__(self) -&gt; int: Return a hash based on the query to enable hashing in graphs. Assumes queries are unique.
  __init__(self, query: str, answer: Optional[str] = None, follow_ups: Optional[List['DriftAction']] = None) -&gt; None: Initialize the action with a query, optional answer, and optional follow-ups.
  serialize(self, include_follow_ups: bool = True) -&gt; dict[str, Any]: Serialize the action to a dict; optionally include serialized follow-ups.
  is_complete(self) -&gt; bool: Return True if an answer is present.
  from_primer_response(cls, query: str, response: str | dict[str, Any] | list[dict[str, Any]]) -&gt; "DriftAction": Create a DriftAction from a DRIFTPrimer response.
  deserialize(cls, data: dict[str, Any]) -&gt; "DriftAction": Deserialize an action from a dict.
  __eq__(self, other: object) -&gt; bool: Equality based on the query.
  search(self, search_engine: Any, global_query: str, scorer: Any = None) -&gt; "DriftAction": Execute an asynchronous search and update the action; if a scorer is provided, compute the score.

## Methods

### `compute_score`

```python
def compute_score(self, scorer: Any)
```

### `__hash__`

```python
def __hash__(self) -> int
```

### `__init__`

```python
def __init__(
        self,
        query: str,
        answer: str | None = None,
        follow_ups: list["DriftAction"] | None = None,
    )
```

### `serialize`

```python
def serialize(self, include_follow_ups: bool = True) -> dict[str, Any]
```

### `is_complete`

```python
def is_complete(self) -> bool
```

### `from_primer_response`

```python
def from_primer_response(
        cls, query: str, response: str | dict[str, Any] | list[dict[str, Any]]
    ) -> "DriftAction"
```

### `deserialize`

```python
def deserialize(cls, data: dict[str, Any]) -> "DriftAction"
```

### `__eq__`

```python
def __eq__(self, other: object) -> bool
```

### `search`

```python
def search(self, search_engine: Any, global_query: str, scorer: Any = None)
```

