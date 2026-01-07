---
sidebar_position: 176
---

# graphrag/prompt_tune/generator/entity_types.py

## Overview

Utilities for generating entity type categories from documents using a chat-based language model.

This module exposes the generate_entity_types function, which constructs prompts using a domain and persona, sends the documents to a ChatModel, and returns the generated entity types. Output can be a Python list of strings or a JSON-encoded string, controlled by the json_mode flag.

Exports:
- generate_entity_types

Args:
- model (ChatModel): The chat model to use for generation.
- domain (str): The domain context to tailor prompts.
- persona (str): The system persona content used as the initial system prompt.
- docs (str | list[str]): A single string or a list of strings containing the documents to extract entity types from.
- task (str): Optional task prompt to guide the generation; defaults to DEFAULT_TASK.
- json_mode (bool): If True, return a JSON-encoded string; otherwise return a list of entity type strings.

Returns:
- str: If json_mode is True, a JSON-encoded string.
- list[str]: If json_mode is False, the list of entity type strings.

Raises:
- TypeError: If any input parameter has an incorrect type.
- ValueError: If docs is empty or otherwise invalid.
- RuntimeError: If the underlying generation process fails.

Notes:
- This function relies on prompts defined in graphrag.prompt_tune.prompt.entity_types, including ENTITY_TYPE_GENERATION_JSON_PROMPT and ENTITY_TYPE_GENERATION_PROMPT.

## Functions

- [`generate_entity_types`](../api/functions/graphrag-prompt-tune-generator-entity-types-generate-entity-types)

