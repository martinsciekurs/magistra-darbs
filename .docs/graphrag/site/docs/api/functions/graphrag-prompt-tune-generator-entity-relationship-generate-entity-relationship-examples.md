---
sidebar_position: 313
---

# generate_entity_relationship_examples

**File:** `graphrag/prompt_tune/generator/entity_relationship.py` (lines 18-65)

## Signature

```python
def generate_entity_relationship_examples(
    model: ChatModel,
    persona: str,
    entity_types: str | list[str] | None,
    docs: str | list[str],
    language: str,
    json_mode: bool = False,
) -> list[str]
```

## Description

Generate a list of entity/relationships examples for use in generating an entity configuration.

Args:
    model: ChatModel to use for generating responses.
    persona: Persona content used to seed the system history for the chat.
    entity_types: Optional entity types to guide generation. Can be a string or a list of strings; if None, untyped prompts are generated.
    docs: Documentation text to base the examples on. Can be a string or a list of strings.
    language: Target language for the prompts.
    json_mode: Whether to format the output as JSON (True) or as a tuple_delimiter format (False).

Returns:
    list[str]: The generated examples as strings. If json_mode is True, each string is a JSON-formatted example; otherwise the examples are in tuple_delimiter format. Up to MAX_EXAMPLES items (5).

Raises:
    Exceptions raised by the underlying model interactions (e.g., model.achat) may propagate to the caller.

## Called By

This function is called by:

- `graphrag/api/prompt_tune.py::generate_indexing_prompts`

