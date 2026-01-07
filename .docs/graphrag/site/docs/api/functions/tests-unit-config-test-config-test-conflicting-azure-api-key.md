---
sidebar_position: 466
---

# test_conflicting_azure_api_key

**File:** `tests/unit/config/test_config.py` (lines 82-97)

## Signature

```python
def test_conflicting_azure_api_key() -> None
```

## Description

Test that configuring an Azure OpenAI Chat model with Azure Managed Identity and an API key raises a ValidationError.

Returns:
    None

Raises:
    ValidationError: If the models configuration includes an api_key while auth_type is AzureManagedIdentity for an Azure OpenAI Chat model, making the config invalid.

## Dependencies

This function calls:

- `graphrag/config/create_graphrag_config.py::create_graphrag_config`

