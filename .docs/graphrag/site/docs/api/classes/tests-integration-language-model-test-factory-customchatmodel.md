---
sidebar_position: 57
---

# CustomChatModel

**File:** `tests/integration/language_model/test_factory.py`

## Overview

Lightweight test-oriented chat model that provides synchronous, streaming, and asynchronous chat interfaces.

Purpose:
    Simulate basic chat interactions for tests by offering predictable responses across methods. It does not maintain internal state between calls and ignores any initialization keyword arguments.

Attributes:
    None - the class does not store internal state.

Args:
    kwargs: dict[str, Any] - Optional keyword arguments provided to the initializer. They are ignored.

Returns:
    None

## Methods

### `achat`

```python
def achat(
            self, prompt: str, history: list | None = None, **kwargs: Any
        ) -> ModelResponse
```

### `chat`

```python
def chat(
            self, prompt: str, history: list | None = None, **kwargs: Any
        ) -> ModelResponse
```

### `chat_stream`

```python
def chat_stream(
            self, prompt: str, history: list | None = None, **kwargs: Any
        ) -> Generator[str, None]
```

### `achat_stream`

```python
def achat_stream(
            self, prompt: str, history: list | None = None, **kwargs: Any
        ) -> AsyncGenerator[str, None]
```

### `__init__`

```python
def __init__(self, **kwargs)
```

