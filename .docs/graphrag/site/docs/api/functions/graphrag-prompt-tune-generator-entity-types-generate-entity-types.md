---
sidebar_position: 315
---

# generate_entity_types

**File:** `graphrag/prompt_tune/generator/entity_types.py` (lines 22-59)

## Signature

```python
def generate_entity_types(
    model: ChatModel,
    domain: str,
    persona: str,
    docs: str | list[str],
    task: str = DEFAULT_TASK,
    json_mode: bool = False,
) -> str | list[str]
```

## Description

Generate entity type categories from a given set of documents.

Args:
    model: ChatModel. The chat model to use for generation.
    domain: str. The domain context to tailor prompts.
    persona: str. The system persona content used as the initial system prompt.
    docs: str | list[str]. A single string or a list of strings containing the documents to extract entity types from.
    task: str. Task specification to format with domain; defaults to DEFAULT_TASK.
    json_mode: bool. If True, parse the response as JSON using EntityTypesResponse and return a list of entity types; otherwise return the raw text output.

Returns:
    str | list[str]. When json_mode is True, returns a list of entity types extracted from the documents (or empty list on failure). When json_mode is False, returns the raw string output from the model.

Raises:
    Exception. If the underlying model call fails or returns an unexpected structure.

## Called By

This function is called by:

- `graphrag/api/prompt_tune.py::generate_indexing_prompts`

