---
sidebar_position: 332
---

# build_entity_context

**File:** `graphrag/query/context_builder/local_context.py` (lines 30-90)

## Signature

```python
def build_entity_context(
    selected_entities: list[Entity],
    tokenizer: Tokenizer | None = None,
    max_context_tokens: int = 8000,
    include_entity_rank: bool = True,
    rank_description: str = "number of relationships",
    column_delimiter: str = "|",
    context_name="Entities",
) -> tuple[str, pd.DataFrame]
```

## Description

Prepare entity data table as context data for system prompt.

Args:
    selected_entities (list[Entity]): Entities to include in the context.
    tokenizer (Tokenizer | None): Tokenizer to measure token counts; if None, get_tokenizer() is used.
    max_context_tokens (int): Maximum allowed tokens for the generated context text. Parsing stops when adding a new entity would exceed this limit.
    include_entity_rank (bool): Whether to include the entity's rank in the context row.
    rank_description (str): Label for the rank column (e.g., "number of relationships").
    column_delimiter (str): Delimiter to join fields in the context text.
    context_name (str): Name of the context section used in the header, default "Entities".

Returns:
    tuple[str, pd.DataFrame]: A tuple containing:
        - current_context_text: The textual context including header and entity rows (up to max_context_tokens).
        - record_df: A DataFrame of the context records (excluding the header). If no entities were processed, this is an empty DataFrame.

## Dependencies

This function calls:

- `graphrag/tokenizer/get_tokenizer.py::get_tokenizer`

## Called By

This function is called by:

- `graphrag/query/structured_search/local_search/mixed_context.py::LocalSearchMixedContext._build_local_context`

