---
sidebar_position: 157
---

# sort_context

**File:** `graphrag/index/operations/summarize_communities/text_unit_context/sort_context.py` (lines 58-85)

## Signature

```python
def sort_context(
    local_context: list[dict],
    tokenizer: Tokenizer,
    sub_community_reports: list[dict] | None = None,
    max_context_tokens: int | None = None,
) -> str
```

## Description

Sort local context (list of text units) by total degree of associated nodes in descending order.

Args:
    local_context: list[dict] - Local context data; a list of dictionaries representing text units.
    tokenizer: Tokenizer - Tokenizer used to count tokens for max_context_tokens to enforce length constraints.
    sub_community_reports: list[dict] | None - Optional list of dictionaries for sub-community reports to include at the top of the resulting context string.
    max_context_tokens: int | None - Maximum number of tokens allowed in the resulting context string; if provided, text units are added until the limit would be exceeded.

Returns:
    str: The context string built from the selected text units; if max_context_tokens is provided, the string includes as many units as fit within the token limit; otherwise, the full sorted context is returned, including sub_community_reports if present.

## Dependencies

This function calls:

- `graphrag/index/operations/summarize_communities/text_unit_context/sort_context.py::get_context_string`

## Called By

This function is called by:

- `graphrag/index/operations/summarize_communities/text_unit_context/context_builder.py::build_local_context`
- `graphrag/index/operations/summarize_communities/text_unit_context/context_builder.py::build_level_context`

