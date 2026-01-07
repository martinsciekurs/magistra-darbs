---
sidebar_position: 312
---

# generate_domain

**File:** `graphrag/prompt_tune/generator/domain.py` (lines 10-27)

## Signature

```python
def generate_domain(model: ChatModel, docs: str | list[str]) -> str
```

## Description

Generate an LLM persona to use for GraphRAG prompts.

Args:
    model (ChatModel): The LLM to use for generation
    docs (str | list[str]): The domain to generate a persona for

Returns:
    str: The generated domain prompt response.

Raises:
    Exception: If the underlying model call fails.

## Called By

This function is called by:

- `graphrag/api/prompt_tune.py::generate_indexing_prompts`

