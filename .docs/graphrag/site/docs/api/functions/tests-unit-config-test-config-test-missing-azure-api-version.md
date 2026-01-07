---
sidebar_position: 468
---

# test_missing_azure_api_version

**File:** `tests/unit/config/test_config.py` (lines 123-133)

## Signature

```python
def test_missing_azure_api_version() -> None
```

## Description

Test that a ValidationError is raised when an Azure OpenAI Chat model configuration is missing the required api_version field.

Args:
    None: This test does not take any parameters.

Returns:
    None: This test does not return a value.

Raises:
    pydantic.ValidationError: If the model configuration is invalid due to a missing api_version in an Azure OpenAI Chat model.

## Dependencies

This function calls:

- `graphrag/config/create_graphrag_config.py::create_graphrag_config`

