---
sidebar_position: 273
---

# _create_error_handler

**File:** `graphrag/language_model/providers/fnllm/utils.py` (lines 40-54)

## Signature

```python
def _create_error_handler(callbacks: WorkflowCallbacks) -> ErrorHandlerFn
```

## Description

Create an error handler for LLM invocation errors.

Internal helper that returns an ErrorHandlerFn which logs errors using the
configured logger. The returned handler does not invoke any callbacks.

Args:
    callbacks: WorkflowCallbacks
        A container of optional callbacks. This parameter is currently unused by
        the error handler.

Returns:
    ErrorHandlerFn
        A function that accepts error: BaseException | None, stack: str | None, and
        details: dict | None, and logs an error with the message "Error Invoking LLM",
        including the exception information and any extra context.

Raises:
    None

## Example 💡 Generated

```python
from module import _create_error_handler
class CW: pass
callbacks = CW()
handler = _create_error_handler(callbacks)
handler(Exception("boom"),
        "trace", {"k":"v"})  # logs "Error Invoking LLM"
```

## Called By

This function is called by:

- `graphrag/language_model/providers/fnllm/models.py::OpenAIChatFNLLM.__init__`
- `graphrag/language_model/providers/fnllm/models.py::OpenAIEmbeddingFNLLM.__init__`
- `graphrag/language_model/providers/fnllm/models.py::AzureOpenAIChatFNLLM.__init__`
- `graphrag/language_model/providers/fnllm/models.py::AzureOpenAIEmbeddingFNLLM.__init__`

