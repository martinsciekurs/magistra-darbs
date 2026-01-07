---
sidebar_position: 464
---

# test_missing_azure_api_key

**File:** `tests/unit/config/test_config.py` (lines 45-65)

## Signature

```python
def test_missing_azure_api_key() -> None
```

## Description

Test that a ValidationError is raised when an Azure OpenAI Chat model is configured with APIKey authentication but no API key is provided, and that switching to AzureManagedIdentity does not raise an error.

Returns:
    None

Raises:
    pydantic.ValidationError: If the model configuration is invalid (e.g., missing API key for an Azure OpenAI Chat model with APIKey authentication).

## Dependencies

This function calls:

- `graphrag/config/create_graphrag_config.py::create_graphrag_config`

