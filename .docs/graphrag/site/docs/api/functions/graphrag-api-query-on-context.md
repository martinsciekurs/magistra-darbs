---
sidebar_position: 4
---

# on_context

**File:** `graphrag/api/query.py` (lines 1085-1087)

## Signature

```python
def on_context(context: Any) -> None
```

## Description

Store the given context in the enclosing scope's context_data.

Args:
    context (Any): The context data to store in the enclosing scope.

Returns:
    None: The function updates context_data in the outer scope and returns no value.

Raises:
    None: This function does not raise exceptions by itself.

