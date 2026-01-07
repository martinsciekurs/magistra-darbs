---
sidebar_position: 65
---

# CustomEmbeddingModel

**File:** `tests/integration/language_model/test_factory.py`

## Overview

CustomEmbeddingModel provides synchronous and asynchronous embeddings for text inputs, including batch processing. It is stateless and accepts arbitrary keyword arguments at initialization, which are ignored.

Args:
  kwargs: dict[str, Any] - keyword arguments provided to the initializer. They are ignored.

Returns:
  None

Methods:
  aembed_batch(self, text_list: list[str], **kwargs) -&gt; list[list[float]]: Asynchronously compute embeddings for a batch of input texts.
    Returns: A list of embeddings, where each embedding is a list of floats corresponding to the input texts.
    Raises: Exceptions from the underlying embedding process may propagate.
  aembed(self, text: str, **kwargs) -&gt; list[float]: Asynchronously generate an embedding for the input text.
    Returns: A list of floats representing the embedding.
    Raises: Exceptions from the underlying embedding process may propagate.
  embed_batch(self, text_list: list[str], **kwargs) -&gt; list[list[float]]: Compute embeddings for a batch of input texts.
    Returns: A list of embeddings corresponding to the input texts.
    Raises: Exceptions from the underlying embedding process may propagate.
  embed(self, text: str, **kwargs) -&gt; list[float]: Generate an embedding for the input text.
    Returns: A list of floats representing the embedding.
    Raises: Exceptions from the underlying embedding process may propagate.
  __init__(self, **kwargs): Initialize the instance with arbitrary keyword arguments; no initialization is performed.
    Returns: None
    Raises: None

## Methods

### `aembed_batch`

```python
def aembed_batch(
            self, text_list: list[str], **kwargs
        ) -> list[list[float]]
```

### `aembed`

```python
def aembed(self, text: str, **kwargs) -> list[float]
```

### `embed_batch`

```python
def embed_batch(self, text_list: list[str], **kwargs) -> list[list[float]]
```

### `embed`

```python
def embed(self, text: str, **kwargs) -> list[float]
```

### `__init__`

```python
def __init__(self, **kwargs)
```

