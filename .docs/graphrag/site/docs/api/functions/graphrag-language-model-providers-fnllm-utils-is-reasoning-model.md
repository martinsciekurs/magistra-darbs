---
sidebar_position: 275
---

# is_reasoning_model

**File:** `graphrag/language_model/providers/fnllm/utils.py` (lines 135-137)

## Signature

```python
def is_reasoning_model(model: str) -> bool
```

## Description

Check if a model name is a known OpenAI reasoning model.

Args:
    model: The name of the model to check.

Returns:
    bool: True if the model is one of the known OpenAI reasoning models (o1, o1-mini, o3-mini); otherwise False.

## Called By

This function is called by:

- `graphrag/language_model/providers/fnllm/utils.py::get_openai_model_parameters_from_dict`

