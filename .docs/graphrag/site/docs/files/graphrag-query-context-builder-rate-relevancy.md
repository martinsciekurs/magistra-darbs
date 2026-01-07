---
sidebar_position: 188
---

# graphrag/query/context_builder/rate_relevancy.py

## Overview

Utilities to rate the relevancy between a query and a community description for context construction in Graphrag.

Purpose
Provide a function to rate the relevancy between a user query and a community description using a language model. This helps quantify how well a given description matches a query when building contextual data.

Key exports
- rate_relevancy(query: str, description: str, model: ChatModel, tokenizer: Tokenizer, rate_query: str = RATE_QUERY, num_repeats: int = 1, semaphore: asyncio.Semaphore | None = None, **model_params: Any) -&gt; dict[str, Any]

Brief summary
The rate_relevancy function formats a prompt with RATE_QUERY, invokes the supplied ChatModel via the given Tokenizer, and returns a dictionary with the rating and related metadata (on a scale from 0 to 10). It relies on try_parse_json_object for parsing model outputs and supports optional concurrency control and additional model parameters.

## Functions

- [`rate_relevancy`](../api/functions/graphrag-query-context-builder-rate-relevancy-rate-relevancy)

