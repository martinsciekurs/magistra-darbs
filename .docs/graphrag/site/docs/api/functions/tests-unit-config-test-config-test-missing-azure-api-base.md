---
sidebar_position: 467
---

# test_missing_azure_api_base

**File:** `tests/unit/config/test_config.py` (lines 110-120)

## Signature

```python
def test_missing_azure_api_base() -> None
```

## Description

Test that a ValidationError is raised when an Azure OpenAI Chat model configuration is missing the required api_base field.

Parameters:
    None

Returns:
    None

Raises:
    pydantic.ValidationError: If the model configuration is invalid due to a missing api_base in an Azure OpenAI Chat model.

## Dependencies

This function calls:

- `graphrag/config/create_graphrag_config.py::create_graphrag_config`

