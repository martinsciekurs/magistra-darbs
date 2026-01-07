---
sidebar_position: 64
---

# BaseQuestionGen

**File:** `graphrag/query/question_gen/base.py`

## Overview

BaseQuestionGen is a base class for generating questions using a language model and context builders.

Purpose:
    Provide a common interface and shared setup for question generation by coordinating a ChatModel with a context_builder (GlobalContextBuilder or LocalContextBuilder) and an optional Tokenizer. Subclasses implement the concrete generation logic.

Args:
    model (ChatModel): The language model interface used for this base question generator.
    context_builder (GlobalContextBuilder | LocalContextBuilder): The builder that constructs the context for the questions.
    tokenizer (Tokenizer | None): Optional tokenizer to use. If None, a tokenizer appropriate for the model will be used.
    model_params (dict[str, Any] | None): Optional parameters for configuring the underlying model.
    context_builder_params (dict[str, Any] | None): Optional parameters for configuring the context builder.

Attributes:
    model: The language model interface used for generation.
    context_builder: The context builder instance used to assemble context data.
    tokenizer: Optional tokenizer instance used to tokenize prompts and outputs.
    model_params: Optional parameters for the model configuration.
    context_builder_params: Optional parameters for the context builder configuration.

Methods:
    generate(question_history: list[str], context_data: str | None, question_count: int, **kwargs) -&gt; QuestionResult:
        Generate questions synchronously.
    agenerate(question_history: list[str], context_data: str | None, question_count: int, **kwargs) -&gt; QuestionResult:
        Generate questions asynchronously.

## Methods

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

### `__init__`

```python
def __init__(
        self,
        model: ChatModel,
        context_builder: GlobalContextBuilder | LocalContextBuilder,
        tokenizer: Tokenizer | None = None,
        model_params: dict[str, Any] | None = None,
        context_builder_params: dict[str, Any] | None = None,
    )
```

