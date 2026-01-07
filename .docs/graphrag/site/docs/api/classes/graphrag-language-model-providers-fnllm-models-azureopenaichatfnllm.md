---
sidebar_position: 100
---

# AzureOpenAIChatFNLLM

**File:** `graphrag/language_model/providers/fnllm/models.py`

## Overview

Azure OpenAI Chat LLM provider using FNLLM.

Responsible for interfacing with Azure OpenAI's chat endpoints through FNLLM wrappers, exposing both synchronous and streaming chat interfaces, supporting optional conversation history, and integrating caching and error handling via optional callbacks.

Args:
    name (str): The name to assign to the internal cache provider and model instance.
    config (LanguageModelConfig): The configuration used to derive the OpenAI configuration.
    callbacks (WorkflowCallbacks | None): Optional WorkflowCallbacks; if provided, an error handler will be created to log issues.
    cache (PipelineCache | None): Optional PipelineCache used for caching responses and model state.

Returns:
    None

Raises:
    Exception: Exceptions raised by the underlying model initialization or by auxiliary utilities may propagate.

## Methods

### `achat`

```python
def achat(
        self, prompt: str, history: list | None = None, **kwargs
    ) -> ModelResponse
```

### `achat_stream`

```python
def achat_stream(
        self, prompt: str, history: list | None = None, **kwargs
    ) -> AsyncGenerator[str, None]
```

### `chat_stream`

```python
def chat_stream(
        self, prompt: str, history: list | None = None, **kwargs
    ) -> Generator[str, None]
```

### `chat`

```python
def chat(self, prompt: str, history: list | None = None, **kwargs) -> ModelResponse
```

### `__init__`

```python
def __init__(
        self,
        *,
        name: str,
        config: LanguageModelConfig,
        callbacks: WorkflowCallbacks | None = None,
        cache: PipelineCache | None = None,
    ) -> None
```

