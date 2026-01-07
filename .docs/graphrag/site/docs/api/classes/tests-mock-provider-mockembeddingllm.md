---
sidebar_position: 61
---

# MockEmbeddingLLM

**File:** `tests/mock_provider.py`

## Overview

# TODO: Document this class

## Methods

### `aembed_batch`

```python
def aembed_batch(
        self, text_list: list[str], **kwargs: Any
    ) -> list[list[float]]
```

### `embed_batch`

```python
def embed_batch(self, text_list: list[str], **kwargs: Any) -> list[list[float]]
```

### `aembed`

```python
def aembed(self, text: str, **kwargs: Any) -> list[float]
```

### `embed`

```python
def embed(self, text: str, **kwargs: Any) -> list[float]
```

### `__init__`

```python
def __init__(self, **kwargs: Any)
```

