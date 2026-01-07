---
sidebar_position: 132
---

# build_mixed_context

**File:** `graphrag/index/operations/summarize_communities/build_mixed_context.py` (lines 14-73)

## Signature

```python
def build_mixed_context(
    context: list[dict], tokenizer: Tokenizer, max_context_tokens: int
) -> str
```

## Description

Builds the parent context by concatenating all sub-communities' contexts, with a fallback to sub-community reports if the combined context would exceed the token limit.

Args:
    context: list[dict]
        List of sub-community contexts to process.
    tokenizer: Tokenizer
        Tokenizer used to count tokens to enforce max_context_tokens.
    max_context_tokens: int
        Maximum number of tokens allowed for the resulting context.

Returns:
    str
        The resulting context as a string; may be a concatenation of local contexts, or a CSV of substitute reports if limits are reached.

## Dependencies

This function calls:

- `graphrag/index/operations/summarize_communities/graph_context/sort_context.py::sort_context`

## Called By

This function is called by:

- `graphrag/index/operations/summarize_communities/graph_context/context_builder.py::_build_mixed_context`
- `graphrag/index/operations/summarize_communities/text_unit_context/context_builder.py::build_level_context`

