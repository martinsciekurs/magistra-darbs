---
sidebar_position: 6
---

# graphrag/callbacks/noop_query_callbacks.py

## Overview

No-op query callbacks module for graphrag.

Purpose:
Provide a no-op implementation of the QueryCallbacks interface for query callback events. The NoopQueryCallbacks class deliberately performs no actions and maintains no internal state.

Key exports:
- NoopQueryCallbacks: A no-op implementation of the QueryCallbacks interface with all callback methods defined as no-ops.

Summary:
This module serves as a placeholder callback handler, suitable for testing or scenarios where side effects are not desired.

Args:
- None: This module does not require any arguments.

Returns:
- None: This module does not return a value.

Raises:
- None: This module does not raise exceptions by itself.

## Classes

- [`NoopQueryCallbacks`](../api/classes/graphrag-callbacks-noop-query-callbacks-noopquerycallbacks)

## Functions

- [`on_map_response_start`](../api/functions/graphrag-callbacks-noop-query-callbacks-on-map-response-start)
- [`on_llm_new_token`](../api/functions/graphrag-callbacks-noop-query-callbacks-on-llm-new-token)
- [`on_context`](../api/functions/graphrag-callbacks-noop-query-callbacks-on-context)
- [`on_reduce_response_start`](../api/functions/graphrag-callbacks-noop-query-callbacks-on-reduce-response-start)
- [`on_map_response_end`](../api/functions/graphrag-callbacks-noop-query-callbacks-on-map-response-end)
- [`on_reduce_response_end`](../api/functions/graphrag-callbacks-noop-query-callbacks-on-reduce-response-end)

