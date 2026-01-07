---
sidebar_position: 131
---

# ConversationRole

**File:** `graphrag/query/context_builder/conversation_history.py`

## Overview

ConversationRole is an enumeration that represents the role of a participant in a conversation (system, user, or assistant). It defines three members: SYSTEM, USER, and ASSISTANT, each with an underlying string value: "system", "user", and "assistant". The underlying string value is accessible via the .value attribute. Note that __str__(self) may not return the underlying value by default; depending on the implementation, str(role) can yield the enum member name (for example, ConversationRole.SYSTEM). If you need the string form, use role.value.

From_string(value: str) converts a string to the corresponding ConversationRole. Args: value: The role as a string. Expected values are "system", "user", or "assistant". Returns: The corresponding ConversationRole enum member. Raises: ValueError if value is not one of the supported roles.

Attributes:
  SYSTEM: The member representing the system role with value "system".
  USER: The member representing the user role with value "user".
  ASSISTANT: The member representing the assistant role with value "assistant".

Examples:
  role = ConversationRole.from_string("system")
  assert role is ConversationRole.SYSTEM
  print(role.value)  # "system"

## Methods

### `__str__`

```python
def __str__(self) -> str
```

### `from_string`

```python
def from_string(value: str) -> "ConversationRole"
```

