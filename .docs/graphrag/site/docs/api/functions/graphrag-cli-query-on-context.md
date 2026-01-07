---
sidebar_position: 32
---

# on_context

**File:** `graphrag/cli/query.py` (lines 442-444)

## Signature

```python
def on_context(context: Any) -> None
```

## Description

Stores the given context in the enclosing scope's nonlocal variable context_data.

This function uses a nonlocal binding to the variable context_data defined in the outer scope and assigns the provided context to it. As a result, the outer scope's context_data is updated. This function returns None.

Args:
    context (Any): The context data to store in the enclosing scope.

Returns:
    None: The function updates the outer scope's context_data and returns no value.

Raises:
    NameError: If the enclosing scope does not define context_data (nonlocal binding cannot be resolved).

