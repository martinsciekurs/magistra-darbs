---
sidebar_position: 18
---

# _register_signal_handlers

**File:** `graphrag/cli/index.py` (lines 25-39)

## Signature

```python
def _register_signal_handlers()
```

## Description

Register signal handlers for graceful shutdown of the CLI.

This function defines a signal handler that logs the received signal, cancels all asyncio tasks, and logs that all tasks have been cancelled. It registers the handler for SIGINT and, on non-Windows platforms, SIGHUP.

Returns:
    None

## Called By

This function is called by:

- `graphrag/cli/index.py::_run_index`

