---
sidebar_position: 99
---

# EmbeddingModel

**File:** `graphrag/language_model/protocol/base.py`

## Overview

EmbeddingModel protocol for generating text embeddings.

Purpose:
    Defines the interface for producing embedding vectors from text, including asynchronous and synchronous single-item and batch operations.

Args:
    text_list (list[str]): The list of strings to generate embeddings for. Used by aembed_batch and embed_batch.
    text (str): The text to generate an embedding for. Used by aembed and embed.
    kwargs (Any): Additional keyword arguments (e.g., model parameters) supplied to embedding methods.

Returns:
    For aembed_batch and embed_batch: list[list[float]] (a batch of embedding vectors).
    For aembed and embed: list[float] (a single embedding vector).

Raises:
    Exception: If an error occurs during embedding generation.

## Methods

### `aembed_batch`

```python
def aembed_batch(
        self, text_list: list[str], **kwargs: Any
    ) -> list[list[float]]
```

### `embed`

```python
def embed(self, text: str, **kwargs: Any) -> list[float]
```

### `embed_batch`

```python
def embed_batch(self, text_list: list[str], **kwargs: Any) -> list[list[float]]
```

### `aembed`

```python
def aembed(self, text: str, **kwargs: Any) -> list[float]
```

