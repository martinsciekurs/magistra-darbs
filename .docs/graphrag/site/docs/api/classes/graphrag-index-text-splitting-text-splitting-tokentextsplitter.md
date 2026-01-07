---
sidebar_position: 27
---

# TokenTextSplitter

**File:** `graphrag/index/text_splitting/text_splitting.py`

## Overview

TokenTextSplitter splits input text into chunks using a token-based tokenizer.

Args:
    tokenizer: Tokenizer | None
        Tokenizer to use for tokenization. If None, a default tokenizer is obtained via get_tokenizer().
    **kwargs: Any
        Additional keyword arguments forwarded to the base class initializer via super().__init__(**kwargs).

Attributes:
    tokenizer: Tokenizer | None
        Tokenizer used for tokenization. If None, a default tokenizer is obtained via get_tokenizer().

Returns:
    None
        The constructor does not return a value; it initializes the instance.

Raises:
    Exception: If get_tokenizer() or the base class initializer raise an exception.

## Methods

### `num_tokens`

```python
def num_tokens(self, text: str) -> int
```

### `split_text`

```python
def split_text(self, text: str | list[str]) -> list[str]
```

### `__init__`

```python
def __init__(
        self,
        tokenizer: Tokenizer | None = None,
        **kwargs: Any,
    )
```

