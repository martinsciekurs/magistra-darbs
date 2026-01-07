---
sidebar_position: 8
---

# graphrag/callbacks/query_callbacks.py

## Overview

Base API for callback hooks used during a query processing workflow involving map and reduce operations and interactions with a language model.

This module defines the QueryCallbacks class with default, no-op implementations that can be subclassed to customize behavior during map/reduce phases, token generation by the language model, and context data handling.

Key exports:
- QueryCallbacks: A base class that defines callback hooks used during a query processing workflow involving map and reduce operations and interactions with a language model. Purpose: Provide default, overridable callback methods for lifecycle events such as starting and ending map and reduce operations, handling new tokens from the LLM, and processing context data.

Public methods:
- on_reduce_response_start(self, reduce_response_context: str | dict[str, Any]) -&gt; None: Handle the start of reduce operation.
- on_llm_new_token(self, token) -&gt; None: Handle when a new token is generated.
- on_map_response_end(self, map_response_outputs: list[SearchResult]) -&gt; None: End of map operation callback. This default implementation is a no-op and does not mutate state or produce side effects. Subclasses may override this method to handle the map outputs as needed.
- on_map_response_start(self, map_response_contexts: list[str]) -&gt; None: Handle the start of map response operation.
- on_context(self, context: Any) -&gt; None: Handle when context data is constructed. This implementation performs no operations on it.
- on_reduce_response_end(self, reduce_response_output: str) -&gt; None: Handle the end of reduce operation.

Brief summary:
This module provides a base, overridable callback interface for the map/reduce query workflow and related LLM interactions.

## Classes

- [`QueryCallbacks`](../api/classes/graphrag-callbacks-query-callbacks-querycallbacks)

## Functions

- [`on_reduce_response_start`](../api/functions/graphrag-callbacks-query-callbacks-on-reduce-response-start)
- [`on_llm_new_token`](../api/functions/graphrag-callbacks-query-callbacks-on-llm-new-token)
- [`on_map_response_end`](../api/functions/graphrag-callbacks-query-callbacks-on-map-response-end)
- [`on_map_response_start`](../api/functions/graphrag-callbacks-query-callbacks-on-map-response-start)
- [`on_context`](../api/functions/graphrag-callbacks-query-callbacks-on-context)
- [`on_reduce_response_end`](../api/functions/graphrag-callbacks-query-callbacks-on-reduce-response-end)

