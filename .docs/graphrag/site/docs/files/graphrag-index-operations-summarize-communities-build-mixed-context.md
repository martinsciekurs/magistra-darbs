---
sidebar_position: 83
---

# graphrag/index/operations/summarize_communities/build_mixed_context.py

## Overview

Module to construct the mixed parent context for summarized communities.

Purpose
- Provide utilities to aggregate sub-community contexts into a single parent context while respecting a token limit. If the combined contexts would exceed max_context_tokens, a fallback mechanism uses sub-community reports to keep within the limit.

Exports
- build_mixed_context(context: list[dict], tokenizer: Tokenizer, max_context_tokens: int) -&gt; str

Summary
- The main function iterates over provided sub-community contexts, concatenates their textual representations, counts tokens via the provided Tokenizer, and ensures the result does not exceed max_context_tokens. When necessary, a concise fallback version based on sub-community reports is returned.

Dependencies
- pandas as pd
- graphrag.data_model.schemas as schemas
- graphrag.index.operations.summarize_communities.graph_context.sort_context
- graphrag.tokenizer.tokenizer.Tokenizer

Parameters
- context: list[dict]
    List of sub-community contexts to process.
- tokenizer: Tokenizer
    Tokenizer used to count tokens to enforce max_context_tokens.
- max_context_tokens: int
    Maximum number of tokens allowed in the resulting parent context.

Returns
- str
    The constructed mixed parent context text.

Raises
- ValueError
    If context is not a list or contains invalid items, or if max_context_tokens &lt;= 0.
- TypeError
    If tokenizer is not an instance of Tokenizer.

## Functions

- [`build_mixed_context`](../api/functions/graphrag-index-operations-summarize-communities-build-mixed-context-build-mixed-context)

