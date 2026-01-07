---
sidebar_position: 278
---

# get_openai_model_parameters_from_dict

**File:** `graphrag/language_model/providers/fnllm/utils.py` (lines 147-165)

## Signature

```python
def get_openai_model_parameters_from_dict(config: dict[str, Any]) -> dict[str, Any]
```

## Description

Get the OpenAI API parameters from a configuration dictionary, adjusting for reasoning model differences.

Args:
    config: dict[str, Any] - Configuration dictionary containing model and related parameter fields used to derive OpenAI API parameters.

Returns:
    dict[str, Any] - Dictionary of OpenAI API parameters derived from the input config. Includes 'n' and either:
        - For reasoning models: 'max_completion_tokens' and 'reasoning_effort'
        - For non-reasoning models: 'max_tokens', 'temperature', 'frequency_penalty', 'presence_penalty', 'top_p'
      If 'response_format' is provided in config, it is included as 'response_format' in the result.

Raises:
    KeyError - If required keys (such as 'model') are missing from config.

## Dependencies

This function calls:

- `graphrag/language_model/providers/fnllm/utils.py::is_reasoning_model`

## Called By

This function is called by:

- `graphrag/language_model/providers/fnllm/utils.py::get_openai_model_parameters_from_config`
- `graphrag/query/structured_search/drift_search/search.py::DRIFTSearch.init_local_search`
- `graphrag/query/structured_search/drift_search/search.py::DRIFTSearch.search`
- `graphrag/query/structured_search/drift_search/search.py::DRIFTSearch.stream_search`

