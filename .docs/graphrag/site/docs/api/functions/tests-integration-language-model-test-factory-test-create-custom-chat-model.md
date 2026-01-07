---
sidebar_position: 413
---

# test_create_custom_chat_model

**File:** `tests/integration/language_model/test_factory.py` (lines 21-60)

## Signature

```python
def test_create_custom_chat_model()
```

## Description

Test creating and using a custom chat model via the ModelFactory and ModelManager.

This test defines a CustomChatModel with chat and achat methods, registers it with the factory,
creates an instance via ModelManager, and asserts behavior of the methods (achat returning
content-only response and chat returning content with a full_response payload).

Returns:
    None

## Dependencies

This function calls:

- `graphrag/language_model/manager.py::ModelManager`

