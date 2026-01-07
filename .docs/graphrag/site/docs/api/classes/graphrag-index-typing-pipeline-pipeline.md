---
sidebar_position: 118
---

# Pipeline

**File:** `graphrag/index/typing/pipeline.py`

## Overview

Pipeline stores and manages an ordered sequence of named Workflow objects, exposing operations to inspect and mutate the pipeline.

Purpose
- Provide a lightweight container for (name, Workflow) pairs that preserves order.
- Enable removal of all entries with a given name, iteration over the current entries, and retrieval of names.

Attributes
- workflows: list[tuple[str, Workflow]]
  Internal storage of the pipeline as (name, Workflow) pairs.

Methods
- __init__(self, workflows: list[tuple[str, Workflow]])
  Initialize the Pipeline with the provided (name, Workflow) pairs. Returns None.

- remove(self, name: str) -&gt; None
  Remove all workflows from the pipeline that have the given name. This mutates the internal state
  by removing every workflow whose first element (the name) equals the provided value. All
  matching entries are removed; not just the first match.
  Complexity: O(n) where n is the number of entries. If no entries match, the pipeline remains unchanged.

- run(self) -&gt; Generator[tuple[str, Workflow], None, None]
  Yield a generator of (name, workflow) pairs from the pipeline. The items yielded come from
  self.workflows and are tuples of (name, Workflow), i.e., each yield is a pair containing the
  workflow's name (str) and the corresponding Workflow object.

- names(self) -&gt; list[str]
  Return the names of the workflows in the pipeline, in the same order as stored in
  self.workflows.

Notes
- Iteration reflects the current state of the pipeline; modifications after obtaining a generator
  may not affect items that have already been yielded.
- Edge cases: multiple entries with the same name are all removed by remove.

## Methods

### `remove`

```python
def remove(self, name: str) -> None
```

### `__init__`

```python
def __init__(self, workflows: list[Workflow])
```

### `run`

```python
def run(self) -> Generator[Workflow]
```

### `names`

```python
def names(self) -> list[str]
```

