---
sidebar_position: 283
---

# _create_base_completions

**File:** `graphrag/language_model/providers/litellm/chat_model.py` (lines 48-111)

## Signature

```python
def _create_base_completions(
    model_config: "LanguageModelConfig",
) -> tuple[FixedModelCompletion, AFixedModelCompletion]
```

## Description

Wrap the base litellm completion function with the model configuration.

Args:
    model_config: The configuration for the language model.

Returns:
    A tuple containing the synchronous and asynchronous completion functions.

Raises:
    ValueError

## Called By

This function is called by:

- `graphrag/language_model/providers/litellm/chat_model.py::_create_completions`

