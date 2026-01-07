---
sidebar_position: 309
---

# generate_community_report_rating

**File:** `graphrag/prompt_tune/generator/community_report_rating.py` (lines 12-35)

## Signature

```python
def generate_community_report_rating(
    model: ChatModel, domain: str, persona: str, docs: str | list[str]
) -> str
```

## Description

Generate a community report rating description using a language model.

Args:
    model (ChatModel): The LLM to use for generation
    domain (str): The domain to generate a rating for
    persona (str): The persona to generate a rating for
    docs (str | list[str]): Documents used to contextualize the rating

Returns:
    str: The generated rating description prompt response.

Raises:
    Exception: If the underlying chat model call fails.

## Called By

This function is called by:

- `graphrag/api/prompt_tune.py::generate_indexing_prompts`

