---
sidebar_position: 339
---

# build_text_unit_context

**File:** `graphrag/query/context_builder/source_context.py` (lines 21-79)

## Signature

```python
def build_text_unit_context(
    text_units: list[TextUnit],
    tokenizer: Tokenizer | None = None,
    column_delimiter: str = "|",
    shuffle_data: bool = True,
    max_context_tokens: int = 8000,
    context_name: str = "Sources",
    random_state: int = 86,
) -> tuple[str, dict[str, pd.DataFrame]]
```

## Description

Prepare text-unit data table as context data for system prompt.

Args:
    text_units: list[TextUnit]
        Text units to include in the context.
    tokenizer: Tokenizer | None
        Tokenizer used to count tokens; if None, a tokenizer is retrieved with get_tokenizer().
    column_delimiter: str
        Delimiter used to separate fields in the context rows.
    shuffle_data: bool
        Whether to shuffle text_units before building the context.
    max_context_tokens: int
        Maximum number of tokens allowed for the generated context.
    context_name: str
        Name of the context section included in the header.
    random_state: int
        Seed used to shuffle when shuffle_data is True.
Returns:
    tuple[str, dict[str, pd.DataFrame]]
        The generated text context and a dictionary mapping the context name (lowercased) to a pandas DataFrame containing the context rows.

## Dependencies

This function calls:

- `graphrag/tokenizer/get_tokenizer.py::get_tokenizer`

## Called By

This function is called by:

- `graphrag/query/structured_search/local_search/mixed_context.py::LocalSearchMixedContext._build_text_unit_context`

