---
sidebar_position: 333
---

# build_covariates_context

**File:** `graphrag/query/context_builder/local_context.py` (lines 93-155)

## Signature

```python
def build_covariates_context(
    selected_entities: list[Entity],
    covariates: list[Covariate],
    tokenizer: Tokenizer | None = None,
    max_context_tokens: int = 8000,
    column_delimiter: str = "|",
    context_name: str = "Covariates",
) -> tuple[str, pd.DataFrame]
```

## Description

Prepare covariate data tables as context data for system prompt.

Args:
  selected_entities (list[Entity]): Entities to include in the covariate context.
  covariates (list[Covariate]): Covariates from which to build context for the entities.
  tokenizer (Tokenizer | None): Tokenizer to count tokens; if None, get_tokenizer() is used.
  max_context_tokens (int): Maximum allowed tokens for the generated context text. Parsing stops when adding a new covariate would exceed this limit.
  column_delimiter (str): Delimiter used to join fields in the context rows (default "|").
  context_name (str): Name used to label the context section in the output (default "Covariates").

Returns:
  tuple[str, pd.DataFrame]: A tuple containing:
    - current_context_text (str): The assembled context text including a header and covariate rows.
    - record_df (pd.DataFrame): A DataFrame of the covariate records (excluding the header). If no covariates were added, this is an empty DataFrame.

## Dependencies

This function calls:

- `graphrag/tokenizer/get_tokenizer.py::get_tokenizer`

## Called By

This function is called by:

- `graphrag/query/structured_search/local_search/mixed_context.py::LocalSearchMixedContext._build_local_context`

