---
sidebar_position: 92
---

# graphrag/index/operations/summarize_communities/text_unit_context/sort_context.py

## Overview

Utilities for constructing and sorting context strings from text units used in community summarization.

This module exposes two helpers:
- get_context_string(text_units: list[dict], sub_community_reports: list[dict] | None = None) -&gt; str
- sort_context(local_context: list[dict], tokenizer: Tokenizer, sub_community_reports: list[dict] | None = None, max_context_tokens: int | None = None) -&gt; str

get_context_string concatenates structured data from text units and optional sub-community reports into a single, ordered context string.

sort_context sorts a local context (list of text units) by the total degree of associated nodes in descending order and returns a string, optionally limiting the result to a maximum token budget via a Tokenizer.

Key exports:
- get_context_string
- sort_context

Functions
- get_context_string(text_units: list[dict], sub_community_reports: list[dict] | None = None) -&gt; str
  Args:
    text_units: List of text unit dictionaries to include in the context. Each dictionary should have an "id" key with a non-empty value.
    sub_community_reports: Optional list of dictionaries for sub-community reports to include at the top. Only reports containing a non-empty community id (defined by schemas) are included if provided.
  Returns:
    The concatenated context string.
  Raises:
    ValueError: If any text_unit dictionary is missing an "id" key or has an empty "id".

- sort_context(local_context: list[dict], tokenizer: Tokenizer, sub_community_reports: list[dict] | None = None, max_context_tokens: int | None = None) -&gt; str
  Args:
    local_context: Local context data; a list of dictionaries representing text units.
    tokenizer: Tokenizer used to count tokens when max_context_tokens is provided to enforce length constraints.
    sub_community_reports: Optional list of dictionaries for sub-community reports to include at the top.
    max_context_tokens: Optional maximum number of tokens to include in the returned context.
  Returns:
    A string representing the sorted context, optionally truncated to max_context_tokens.
  Raises:
    ValueError: If inputs are not well-formed (e.g., non-dict items or missing required keys).

## Functions

- [`get_context_string`](../api/functions/graphrag-index-operations-summarize-communities-text-unit-context-sort-context-get-context-string)
- [`sort_context`](../api/functions/graphrag-index-operations-summarize-communities-text-unit-context-sort-context-sort-context)

