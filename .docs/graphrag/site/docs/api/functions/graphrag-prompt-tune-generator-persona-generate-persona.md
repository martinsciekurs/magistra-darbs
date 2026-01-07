---
sidebar_position: 318
---

# generate_persona

**File:** `graphrag/prompt_tune/generator/persona.py` (lines 11-27)

## Signature

```python
def generate_persona(
    model: ChatModel, domain: str, task: str = DEFAULT_TASK
) -> str
```

## Description

Generate an LLM persona to use for GraphRAG prompts.

Args:
    model (ChatModel): The LLM to use for generation
    domain (str): The domain to generate a persona for
    task (str): The task to generate a persona for. Default is DEFAULT_TASK

Returns:
    str: The generated persona string

Raises:
    Exception: If the underlying model call fails

## Called By

This function is called by:

- `graphrag/api/prompt_tune.py::generate_indexing_prompts`

