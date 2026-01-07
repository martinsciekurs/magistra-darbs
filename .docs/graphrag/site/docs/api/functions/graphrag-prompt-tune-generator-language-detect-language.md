---
sidebar_position: 317
---

# detect_language

**File:** `graphrag/prompt_tune/generator/language.py` (lines 10-27)

## Signature

```python
def detect_language(model: ChatModel, docs: str | list[str]) -> str
```

## Description

Detect input language to use for GraphRAG prompts.

Parameters
    model (ChatModel): The language model to use for language detection
    docs (str | list[str]): The docs to detect language from

Returns
    str: The detected language.

Raises
    Exception: If the underlying model API raises an error during language detection.

## Called By

This function is called by:

- `graphrag/api/prompt_tune.py::generate_indexing_prompts`

