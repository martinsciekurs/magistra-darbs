---
sidebar_position: 287
---

# _create_base_embeddings

**File:** `graphrag/language_model/providers/litellm/embedding_model.py` (lines 42-97)

## Signature

```python
def _create_base_embeddings(
    model_config: "LanguageModelConfig",
) -> tuple[FixedModelEmbedding, AFixedModelEmbedding]
```

## Description

Wrap the base litellm embedding function with the model configuration.

Args
----
    model_config: LanguageModelConfig
        The configuration for the language model.

Returns
-------
    tuple[FixedModelEmbedding, AFixedModelEmbedding]
        A tuple containing the synchronous and asynchronous embedding callables
        produced by wrapping the base embedding with the provided model
        configuration.

Raises
------
    ValueError
        Azure Managed Identity authentication is only supported for Azure models when
        model_provider is not "azure"; in that case authentication setup is rejected with
        the corresponding error message.

Notes
-----
    Azure authentication branch:
    - Triggered when model_config.auth_type == AuthType.AzureManagedIdentity.
    - If model_config.model_provider == "azure":
      - azure_scope is set from the audience value (audience is moved to azure_scope).
      - azure_ad_token_provider is added, constructed via get_bearer_token_provider(
        DefaultAzureCredential(), model_config.audience or COGNITIVE_SERVICES_AUDIENCE).
    - If model_config.model_provider != "azure": a ValueError is raised as described above.

## Called By

This function is called by:

- `graphrag/language_model/providers/litellm/embedding_model.py::_create_embeddings`

