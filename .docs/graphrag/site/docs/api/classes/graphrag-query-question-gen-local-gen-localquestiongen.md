---
sidebar_position: 120
---

# LocalQuestionGen

**File:** `graphrag/query/question_gen/local_gen.py`

## Overview

Generates questions using a local context builder and a language model.

This class coordinates a LocalContextBuilder and a ChatModel to generate questions based on a history of questions and optional context data. It provides asynchronous and synchronous generation methods that return a QuestionResult, and it uses a configurable system prompt.

Attributes:
    model: The language model interface to use (ChatModel).
    context_builder: The builder that constructs context for local question generation (LocalContextBuilder).
    tokenizer: Optional tokenizer to use (Tokenizer | None).
    system_prompt: System prompt for question generation; defaults to QUESTION_SYSTEM_PROMPT (str).
    callbacks: Optional list of callbacks for model events (list[BaseLLMCallback] | None).
    model_params: Optional parameters for the model (dict[str, Any] | None).
    context_builder_params: Optional parameters for the context builder (dict[str, Any] | None).

Args:
    model: ChatModel - The language model interface to use.
    context_builder: LocalContextBuilder - The builder that constructs the context for local question generation.
    tokenizer: Tokenizer | None - Optional tokenizer to use.
    system_prompt: str - System prompt for question generation. Defaults to QUESTION_SYSTEM_PROMPT.
    callbacks: list[BaseLLMCallback] | None - Optional callbacks for model events.
    model_params: dict[str, Any] | None - Optional parameters for the model.
    context_builder_params: dict[str, Any] | None - Optional parameters for the context builder.

Returns:
    QuestionResult - The generated QuestionResult from agenerate or generate.

Raises:
    Exception - If underlying components fail during generation.

## Methods

### `agenerate`

```python
def agenerate(
        self,
        question_history: list[str],
        context_data: str | None,
        question_count: int,
        **kwargs,
    ) -> QuestionResult
```

### `generate`

```python
def generate(
        self,
        question_history: list[str],
        context_data: str | None,
        question_count: int,
        **kwargs,
    ) -> QuestionResult
```

### `__init__`

```python
def __init__(
        self,
        model: ChatModel,
        context_builder: LocalContextBuilder,
        tokenizer: Tokenizer | None = None,
        system_prompt: str = QUESTION_SYSTEM_PROMPT,
        callbacks: list[BaseLLMCallback] | None = None,
        model_params: dict[str, Any] | None = None,
        context_builder_params: dict[str, Any] | None = None,
    )
```

