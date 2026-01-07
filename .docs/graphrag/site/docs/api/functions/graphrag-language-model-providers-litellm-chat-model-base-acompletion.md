---
sidebar_position: 282
---

# _base_acompletion

**File:** `graphrag/language_model/providers/litellm/chat_model.py` (lines 103-109)

## Signature

```python
def _base_acompletion(**kwargs: Any) -> ModelResponse | CustomStreamWrapper
```

## Description

Merge base_args with provided keyword arguments and invoke the asynchronous litellm acompletion.

Args:
  kwargs: Any
      Additional keyword arguments to merge with base_args and pass to acompletion after removing the "name" key if present.

Returns:
  ModelResponse | CustomStreamWrapper
      The result from the underlying acompletion call.

Raises:
  Exception
      Exceptions raised by the underlying acompletion.

