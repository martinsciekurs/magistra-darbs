---
sidebar_position: 336
---

# build_relationship_context

**File:** `graphrag/query/context_builder/local_context.py` (lines 158-229)

## Signature

```python
def build_relationship_context(
    selected_entities: list[Entity],
    relationships: list[Relationship],
    tokenizer: Tokenizer | None = None,
    include_relationship_weight: bool = False,
    max_context_tokens: int = 8000,
    top_k_relationships: int = 10,
    relationship_ranking_attribute: str = "rank",
    column_delimiter: str = "|",
    context_name: str = "Relationships",
) -> tuple[str, pd.DataFrame]
```

## Description

Prepare relationship context data tables as context data for system prompt.

Args:
  selected_entities (list[Entity]): The selected entities for which to build the relationship context.
  relationships (list[Relationship]): The pool of relationships to filter to generate context from.
  tokenizer (Tokenizer | None): Tokenizer to count tokens; if None, get_tokenizer() is used.
  include_relationship_weight (bool): Whether to include the relationship weight in the generated context.
  max_context_tokens (int): Maximum allowed tokens for the generated context text. Parsing stops when adding a new relationship would exceed this limit.
  top_k_relationships (int): Number of top relationships to consider when building the context.
  relationship_ranking_attribute (str): Attribute name used for ranking relationships.
  column_delimiter (str): Delimiter used to separate columns in the generated text.
  context_name (str): Name used in the header block of the context.

Returns:
  tuple[str, pd.DataFrame]: The generated context text and a DataFrame containing the records (excluding the header). If no relevant entities or relationships exist, returns an empty string and an empty DataFrame.

## Dependencies

This function calls:

- `graphrag/query/context_builder/local_context.py::_filter_relationships`
- `graphrag/tokenizer/get_tokenizer.py::get_tokenizer`

## Called By

This function is called by:

- `graphrag/query/structured_search/local_search/mixed_context.py::LocalSearchMixedContext._build_local_context`

