---
sidebar_position: 279
---

# get_openai_model_parameters_from_config

**File:** `graphrag/language_model/providers/fnllm/utils.py` (lines 140-144)

## Signature

```python
def get_openai_model_parameters_from_config(
    config: LanguageModelConfig,
) -> dict[str, Any]
```

## Description

Get the OpenAI API parameters for a given language model config.

Args:
    config (LanguageModelConfig): The language model configuration. This is converted to a dictionary via model_dump() and then used to derive OpenAI API parameters, with adjustments for reasoning models handled by get_openai_model_parameters_from_dict.

Returns:
    dict[str, Any]: A dictionary of OpenAI API parameters derived from the input config, including 'n' and model-specific fields such as 'max_tokens', 'temperature', 'max_completion_tokens', etc., depending on whether the model is a reasoning model.

## Dependencies

This function calls:

- `graphrag/language_model/providers/fnllm/utils.py::get_openai_model_parameters_from_dict`

## Called By

This function is called by:

- `graphrag/language_model/providers/fnllm/utils.py::_create_openai_config`
- `graphrag/query/factory.py::get_local_search_engine`
- `graphrag/query/factory.py::get_global_search_engine`
- `graphrag/query/factory.py::get_basic_search_engine`

