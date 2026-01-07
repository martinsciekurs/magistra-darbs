---
sidebar_position: 70
---

# OpenAIChatFNLLM

**File:** `graphrag/language_model/providers/fnllm/models.py`

## Overview

OpenAIChatFNLLM provider that integrates FNLLM's OpenAI chat LLM with Graphrag's language-model framework to support chat-based interactions within Graphrag's LLM workflows. It wires FNLLM's OpenAI chat client to Graphrag's API surface, deriving its configuration from a LanguageModelConfig and optionally enabling event callbacks and caching.

Args:
  name (str): The name assigned to this provider instance, used for internal identification and cache naming.
  config (LanguageModelConfig): The configuration used to derive the OpenAI client and related settings (e.g., model, prompts, etc.).
  callbacks (WorkflowCallbacks | None): Optional WorkflowCallbacks for propagating lifecycle events and errors through Graphrag.
  cache (PipelineCache | None): Optional cache to persist responses; when provided, the provider reads from and writes to this cache as part of operation.

Returns:
  None

Raises:
  Exception: Exceptions raised by the underlying FNLLM/OpenAI integrations are propagated to the caller.

Attributes:
  name: Identifier for the provider instance.
  config: The LanguageModelConfig used to configure the OpenAI components.
  callbacks: Optional WorkflowCallbacks for event propagation.
  cache: Optional PipelineCache used for caching model outputs.

Notes:
  If a cache is provided, responses may be cached and reused for repeated prompts; the cache lifecycle and eviction are governed by the PipelineCache implementation.

## Methods

### `chat_stream`

```python
def chat_stream(
        self, prompt: str, history: list | None = None, **kwargs
    ) -> Generator[str, None]
```

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

