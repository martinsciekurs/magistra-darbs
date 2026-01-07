---
sidebar_position: 281
---

# _base_completion

**File:** `graphrag/language_model/providers/litellm/chat_model.py` (lines 95-101)

## Signature

```python
def _base_completion(**kwargs: Any) -> ModelResponse | CustomStreamWrapper
```

## Description

Merge base arguments with provided keyword arguments and invoke the litellm completion.

Args:
  kwargs: Any
      Additional keyword arguments to merge with base_args and pass to completion after removing the "name" key if present.

Returns:
  ModelResponse | CustomStreamWrapper
      The result from the underlying completion call.

Raises:
  Exception
      Exceptions raised by the underlying completion call.

