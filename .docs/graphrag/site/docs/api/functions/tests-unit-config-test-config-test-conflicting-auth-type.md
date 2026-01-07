---
sidebar_position: 465
---

# test_conflicting_auth_type

**File:** `tests/unit/config/test_config.py` (lines 68-79)

## Signature

```python
def test_conflicting_auth_type() -> None
```

## Description

Test that a conflicting authentication type raises ValidationError when a model configuration specifies AzureManagedIdentity for an OpenAIChat model.

Returns:
    None

Raises:
    ValidationError: If the models configuration contains a conflicting auth_type.

## Dependencies

This function calls:

- `graphrag/config/create_graphrag_config.py::create_graphrag_config`

