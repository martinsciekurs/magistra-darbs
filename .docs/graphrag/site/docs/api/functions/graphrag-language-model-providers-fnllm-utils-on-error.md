---
sidebar_position: 277
---

# on_error

**File:** `graphrag/language_model/providers/fnllm/utils.py` (lines 43-52)

## Signature

```python
def on_error(
        error: BaseException | None = None,
        stack: str | None = None,
        details: dict | None = None,
    ) -> None
```

## Description

Log an error that occurred while invoking the LLM.

Args:
    error (BaseException | None): The exception to log; passed to exc_info in logger.error.
    stack (str | None): Optional stack trace or contextual information; included in the log's extra under "stack".
    details (dict | None): Optional additional details; included in the log's extra under "details".

Returns:
    None: This function does not return a value.

Raises:
    None: This function does not raise exceptions.

