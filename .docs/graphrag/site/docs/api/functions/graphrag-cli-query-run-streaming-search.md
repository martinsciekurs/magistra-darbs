---
sidebar_position: 33
---

# run_streaming_search

**File:** `graphrag/cli/query.py` (lines 438-460)

## Signature

```python
def run_streaming_search()
```

## Description

Run a streaming search and collect the full response while printing streamed chunks.

Args:
- None: The function does not take any parameters.

Returns:
- tuple[str, dict[str, Any]]: The full streaming response string and the context data captured during streaming.

Raises:
- Exceptions raised by the underlying streaming API or asyncio operations may propagate to the caller.

## Dependencies

This function calls:

- `graphrag.api::basic_search_streaming`
- `graphrag/callbacks/noop_query_callbacks.py::NoopQueryCallbacks`

## Called By

This function is called by:

- `graphrag/cli/query.py::run_global_search`
- `graphrag/cli/query.py::run_local_search`
- `graphrag/cli/query.py::run_drift_search`
- `graphrag/cli/query.py::run_basic_search`

