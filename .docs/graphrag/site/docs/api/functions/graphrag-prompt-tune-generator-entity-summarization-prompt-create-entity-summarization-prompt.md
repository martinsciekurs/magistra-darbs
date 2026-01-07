---
sidebar_position: 314
---

# create_entity_summarization_prompt

**File:** `graphrag/prompt_tune/generator/entity_summarization_prompt.py` (lines 15-39)

## Signature

```python
def create_entity_summarization_prompt(
    persona: str,
    language: str,
    output_path: Path | None = None,
) -> str
```

## Description

Create a prompt for entity summarization.

The generated prompt is created by formatting ENTITY_SUMMARIZATION_PROMPT with the provided persona and language. If output_path is provided, the prompt is written to a file named summarize_descriptions.txt within output_path, creating directories as needed.

Args:
    persona (str): The persona to use for the entity summarization prompt
    language (str): The language to use for the entity summarization prompt
    output_path (Path | None): The path to write the prompt to. Default is None.

Returns:
    str: The generated prompt.

Raises:
    OSError: If the prompt cannot be written to output_path.

## Example 💡 Generated

```python
from module import create_entity_summarization_prompt
from pathlib import Path
persona = "academic researcher"; language = "English"
out = Path("/tmp/prompts")
prompt = create_entity_summarization_prompt(
    persona, language, out
)
print(prompt)  # shows result; writes file to out
```

## Called By

This function is called by:

- `graphrag/api/prompt_tune.py::generate_indexing_prompts`

