---
sidebar_position: 311
---

# generate_community_reporter_role

**File:** `graphrag/prompt_tune/generator/community_reporter_role.py` (lines 12-35)

## Signature

```python
def generate_community_reporter_role(
    model: ChatModel, domain: str, persona: str, docs: str | list[str]
) -> str
```

## Description

Generate a community reporter role for GraphRAG prompts.

Args:
    model (ChatModel): The LLM to use for generation
    domain (str): The domain to generate a persona for
    persona (str): The persona to generate a role for
    docs (str | list[str]): Documents to contextualize the persona; if a list, these will be joined into a single string

Returns:
    str: The generated domain prompt response content.

Raises:
    Exception: If the underlying model call fails

## Called By

This function is called by:

- `graphrag/api/prompt_tune.py::generate_indexing_prompts`

