---
sidebar_position: 280
---

# _create_openai_config

**File:** `graphrag/language_model/providers/fnllm/utils.py` (lines 57-107)

## Signature

```python
def _create_openai_config(config: LanguageModelConfig, azure: bool) -> OpenAIConfig
```

## Description

Create an OpenAIConfig from a LanguageModelConfig.

Args:
    config: LanguageModelConfig. The configuration used to derive the OpenAI parameters, including encoding_model, model_supports_json, and other fields; a chat_parameters object is built from get_openai_model_parameters_from_config(config).
    azure: bool. If True, construct an AzureOpenAIConfig; otherwise construct a PublicOpenAIConfig.

Returns:
    OpenAIConfig. The constructed OpenAI configuration (AzureOpenAIConfig when azure is True, PublicOpenAIConfig otherwise).

Raises:
    ValueError: Azure OpenAI Chat LLM requires an API base when azure is True.

## Dependencies

This function calls:

- `graphrag/language_model/providers/fnllm/utils.py::get_openai_model_parameters_from_config`

## Called By

This function is called by:

- `graphrag/language_model/providers/fnllm/models.py::OpenAIChatFNLLM.__init__`
- `graphrag/language_model/providers/fnllm/models.py::OpenAIEmbeddingFNLLM.__init__`
- `graphrag/language_model/providers/fnllm/models.py::AzureOpenAIChatFNLLM.__init__`
- `graphrag/language_model/providers/fnllm/models.py::AzureOpenAIEmbeddingFNLLM.__init__`

