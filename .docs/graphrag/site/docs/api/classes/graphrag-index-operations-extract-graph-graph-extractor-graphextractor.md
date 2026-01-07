---
sidebar_position: 98
---

# GraphExtractor

**File:** `graphrag/index/operations/extract_graph/graph_extractor.py`

## Overview

GraphExtractor orchestrates graph extraction from text using a language model and structured prompts, accumulating results into graphs and supporting iterative gleaning via continuation prompts when configured.

Key attributes include: model_invoker (the ChatModel used for prompt execution) and configuration for delimiter/prompt keys (tuple_delimiter_key, record_delimiter_key, input_text_key, entity_types_key, completion_delimiter_key), as well as optional prompt, join_descriptions, max_gleanings, and on_error.

Args:
  model_invoker: The model invoker used to run the extraction prompts against the language model.
  tuple_delimiter_key: Prompt variable key for the delimiter between tuples.
  record_delimiter_key: Prompt variable key for the delimiter between records.
  input_text_key: Prompt variable key for the input text content.
  entity_types_key: Prompt variable key for the entity types to extract.
  completion_delimiter_key: Prompt variable key for the delimiter that marks completion of an extraction loop.
  prompt: Optional prompt template to override defaults.
  join_descriptions: Flag indicating whether to join entity descriptions in the results.
  max_gleanings: Maximum number of gleaning iterations allowed.
  on_error: Error handler to be invoked on errors during processing.

Returns:
  GraphExtractionResult: The result of running graph extraction on the input texts.

Raises:
  Exception: Exceptions may be raised by the underlying model invocation or processing, which may be handled by the on_error callback.

## Methods

### `__call__`

```python
def __call__(
        self, texts: list[str], prompt_variables: dict[str, Any] | None = None
    ) -> GraphExtractionResult
```

### `_process_document`

```python
def _process_document(
        self, text: str, prompt_variables: dict[str, str]
    ) -> str
```

### `__init__`

```python
def __init__(
        self,
        model_invoker: ChatModel,
        tuple_delimiter_key: str | None = None,
        record_delimiter_key: str | None = None,
        input_text_key: str | None = None,
        entity_types_key: str | None = None,
        completion_delimiter_key: str | None = None,
        prompt: str | None = None,
        join_descriptions=True,
        max_gleanings: int | None = None,
        on_error: ErrorHandlerFn | None = None,
    )
```

### `_process_results`

```python
def _process_results(
        self,
        results: dict[int, str],
        tuple_delimiter: str,
        record_delimiter: str,
    ) -> nx.Graph
```

