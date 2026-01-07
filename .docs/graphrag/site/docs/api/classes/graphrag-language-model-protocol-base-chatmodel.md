---
sidebar_position: 36
---

# ChatModel

**File:** `graphrag/language_model/protocol/base.py`

## Overview

ChatModel protocol for chat-based language model interfaces.

Purpose
    Abstract protocol that defines how chat-based language models should generate responses
    from prompts, with optional history, and support both synchronous and streaming interfaces
    via four methods: achat, chat, chat_stream, and achat_stream.

Attributes
    config: LanguageModelConfig
        The configuration for the language model, including model name and generation options
        that implementations may use to control behavior.

Methods
    achat(self, prompt: str, history: list | None = None, **kwargs: Any) -&gt; ModelResponse
        Generate a synchronous, non-streaming response for the given prompt.
        Args:
            prompt: The text to generate a response for.
            history: Optional list of prior messages in the conversation.
            **kwargs: Additional keyword arguments (e.g., model parameters, generation controls).
        Returns:
            ModelResponse: The generated response wrapped in a ModelResponse.
        Raises:
            Exception: If an error occurs during generation.

    chat(self, prompt: str, history: list | None = None, **kwargs: Any) -&gt; ModelResponse
        Generate a synchronous, non-streaming response using the standard chat interface.
        Args:
            prompt: The text to generate a response for.
            history: Optional list of prior messages in the conversation.
            **kwargs: Additional keyword arguments (e.g., model parameters, generation controls).
        Returns:
            ModelResponse: The generated response.
        Raises:
            Exception: If an error occurs during generation.

    chat_stream(self, prompt: str, history: list | None = None, **kwargs: Any) -&gt; Generator[str, None]
        Streaming interface that yields partial strings as the model generates a response.
        Args:
            prompt: The text to generate a response for.
            history: Optional list of prior messages in the conversation.
            **kwargs: Additional keyword arguments (e.g., model parameters, streaming controls).
        Returns:
            Generator[str, None]: A generator that yields strings composing the final response.
        Raises:
            Exception: If an error occurs during generation.

    achat_stream(self, prompt: str, history: list | None = None, **kwargs: Any) -&gt; AsyncGenerator[str, None]
        Asynchronous streaming interface that yields partial strings over time as the model progresses.
        Args:
            prompt: The text to generate a response for.
            history: Optional list of prior messages in the conversation.
            **kwargs: Additional keyword arguments (e.g., model parameters, streaming controls).
        Returns:
            AsyncGenerator[str, None]: An async generator yielding strings for the final response.
        Raises:
            Exception: If an error occurs during generation.

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

