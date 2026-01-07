---
sidebar_position: 310
---

# create_community_summarization_prompt

**File:** `graphrag/prompt_tune/generator/community_report_summarization.py` (lines 15-50)

## Signature

```python
def create_community_summarization_prompt(
    persona: str,
    role: str,
    report_rating_description: str,
    language: str,
    output_path: Path | None = None,
) -> str
```

## Description

Create a prompt for community summarization. If output_path is provided, write the prompt to a file.

Args:
    persona (str): The persona to use for the community summarization prompt.
    role (str): The role to use for the community summarization prompt.
    report_rating_description (str): Description of the report rating to incorporate into the prompt.
    language (str): The language to use for the community summarization prompt.
    output_path (Path | None): The path to write the prompt to. If None, the prompt is not written to a file. Defaults to None.
Returns:
    str: The community summarization prompt.

## Example 💡 Generated

```python
from module import create_community_summarization_prompt
prompt = create_community_summarization_prompt(
    "community advocate",
    "moderator",
    "rating: 4.2/5; highlights",
    "en",
    None,
)  # prompt ready
```

## Called By

This function is called by:

- `graphrag/api/prompt_tune.py::generate_indexing_prompts`

