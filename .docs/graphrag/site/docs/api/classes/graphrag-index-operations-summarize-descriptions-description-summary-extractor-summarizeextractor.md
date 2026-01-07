---
sidebar_position: 78
---

# SummarizeExtractor

**File:** `graphrag/index/operations/summarize_descriptions/description_summary_extractor.py`

## Overview

SummarizeExtractor orchestrates the summarization of a list of description strings into a single concise description for a target entity by invoking a chat-based language model with a summarization prompt. The class is initialized with a model invoker and configuration and is intended to be called to process descriptions for a given identifier (or pair of identifiers).

This class does not return a value from initialization. __init__ initializes the instance and returns None implicitly.

Args
    model_invoker: The ChatModel used to run prompts.
    max_summary_length: Maximum length of the summary to produce.
    max_input_tokens: Maximum number of input tokens to consider for summarization.
    summarization_prompt: Optional custom prompt to use for summarization.
    on_error: Optional error handler invoked on errors.

Returns
    None

Raises
    Exception: If initialization fails or the underlying LLM call fails or processing encounters an error.

Attributes
    model_invoker: The ChatModel used to run prompts.
    max_summary_length: Maximum length of the summary to produce.
    max_input_tokens: Maximum number of input tokens to consider for summarization.
    summarization_prompt: Optional custom prompt to use for summarization.
    on_error: Optional error handler invoked on errors.

Notes
    The class relies on the top-level constants ENTITY_NAME_KEY, DESCRIPTION_LIST_KEY, and MAX_LENGTH_KEY to structure input payloads for the summarization process. These keys influence how the input data is organized before being sent to the language model but are not modified by SummarizeExtractor.

## Methods

### `_summarize_descriptions_with_llm`

```python
def _summarize_descriptions_with_llm(
        self, id: str | tuple[str, str] | list[str], descriptions: list[str]
    )
```

### `_summarize_descriptions`

```python
def _summarize_descriptions(
        self, id: str | tuple[str, str], descriptions: list[str]
    ) -> str
```

### `__call__`

```python
def __call__(
        self,
        id: str | tuple[str, str],
        descriptions: list[str],
    ) -> SummarizationResult
```

### `__init__`

```python
def __init__(
        self,
        model_invoker: ChatModel,
        max_summary_length: int,
        max_input_tokens: int,
        summarization_prompt: str | None = None,
        on_error: ErrorHandlerFn | None = None,
    )
```

