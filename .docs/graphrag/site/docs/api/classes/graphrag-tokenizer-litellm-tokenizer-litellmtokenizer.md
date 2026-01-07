---
sidebar_position: 116
---

# LitellmTokenizer

**File:** `graphrag/tokenizer/litellm_tokenizer.py`

## Overview

LitellmTokenizer provides text-to-token and token-to-text conversions using a Litellm model.

It wraps the Litellm encode and decode functions to operate on a single model identified by model_name.

Args:
    model_name (str): The name of the Litellm model to use for tokenization.

Returns:
    None: This initializer does not return a value.

Raises:
    Exception: If initialization fails due to an underlying error.

Attributes:
    model_name (str): The name of the Litellm model used for tokenization.

## Methods

### `decode`

```python
def decode(self, tokens: list[int]) -> str
```

### `__init__`

```python
def __init__(self, model_name: str) -> None
```

### `encode`

```python
def encode(self, text: str) -> list[int]
```

