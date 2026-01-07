---
sidebar_position: 14
---

# MockChatLLM

**File:** `tests/mock_provider.py`

## Overview

MockChatLLM is a configurable mock chat language model provider used for testing. It cycles through a predefined sequence of responses and can emit them synchronously via chat() or asynchronously via achat_stream(). It supports an optional LanguageModelConfig override and a json flag to indicate that responses should be treated as JSON where applicable.

Args:
- responses: List[str | BaseModel] | None. A list of responses to return in sequence. Each item can be a string or a BaseModel.
- config: LanguageModelConfig | None. Optional configuration. If provided and it has a responses attribute, those will be used instead of the responses argument.
- json: bool. If True, responses are interpreted as JSON content where applicable when constructing outputs.
- kwargs: Any. Additional keyword arguments forwarded to the underlying chat handler.

Returns:
- None. Initializes a MockChatLLM instance.

Raises:
- NotImplementedError: If chat_stream is called since this streaming interface is not yet implemented.

Notes:
- If config is provided and exposes a responses attribute, those responses are used in place of the explicit responses argument.
- The non-streaming chat() method returns the next response in the configured sequence, cycling through via modulo arithmetic. If no responses are configured, an empty content response is returned. The streaming interface for this mock is provided via achat_stream(), which yields each configured response in order and ignores the input prompt and history. The chat_stream() method is not implemented and will raise NotImplementedError if invoked.

Examples:
- Basic usage with string responses: create MockChatLLM(responses=["Hi","Hello"]) and call chat() to retrieve responses in order, cycling when the end is reached.

## Methods

### `achat`

```python
def achat(
        self,
        prompt: str,
        history: list | None = None,
        **kwargs,
    ) -> ModelResponse
```

### `__init__`

```python
def __init__(
        self,
        responses: list[str | BaseModel] | None = None,
        config: LanguageModelConfig | None = None,
        json: bool = False,
        **kwargs: Any,
    )
```

### `achat_stream`

```python
def achat_stream(
        self,
        prompt: str,
        history: list | None = None,
        **kwargs,
    ) -> AsyncGenerator[str, None]
```

### `chat`

```python
def chat(
        self,
        prompt: str,
        history: list | None = None,
        **kwargs,
    ) -> ModelResponse
```

### `chat_stream`

```python
def chat_stream(
        self,
        prompt: str,
        history: list | None = None,
        **kwargs,
    ) -> Generator[str, None]
```

