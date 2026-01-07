---
sidebar_position: 316
---

# create_extract_graph_prompt

**File:** `graphrag/prompt_tune/generator/extract_graph_prompt.py` (lines 21-109)

## Signature

```python
def create_extract_graph_prompt(
    entity_types: str | list[str] | None,
    docs: list[str],
    examples: list[str],
    language: str,
    max_token_count: int,
    tokenizer: Tokenizer | None = None,
    json_mode: bool = False,
    output_path: Path | None = None,
    min_examples_required: int = 2,
) -> str
```

## Description

Create a prompt for entity extraction.

Args:
    entity_types (str | list[str] | None): The entity types to extract.
    docs (list[str]): The list of documents to extract entities from.
    examples (list[str]): The list of examples to use for entity extraction.
    language (str): The language of the inputs and outputs.
    max_token_count (int): The maximum number of tokens to use for the prompt.
    tokenizer (Tokenizer | None): The tokenizer to use for encoding and decoding text. If None, a default tokenizer will be used.
    json_mode (bool): Whether to use JSON mode for the prompt. Default is False.
    output_path (Path | None): The path to write the prompt to. Default is None.
    min_examples_required (int): The minimum number of examples required. Default is 2.

Returns:
    str: The entity extraction prompt.

## Dependencies

This function calls:

- `graphrag/tokenizer/get_tokenizer.py::get_tokenizer`

## Called By

This function is called by:

- `graphrag/api/prompt_tune.py::generate_indexing_prompts`

