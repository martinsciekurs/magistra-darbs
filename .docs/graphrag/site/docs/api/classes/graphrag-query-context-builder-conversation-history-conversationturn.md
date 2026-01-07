---
sidebar_position: 60
---

# ConversationTurn

**File:** `graphrag/query/context_builder/conversation_history.py`

## Overview

Represents a single turn in a conversation history.

Args:
    role: The role associated with this turn (for example, SYSTEM, USER, or ASSISTANT).
    content: The textual content of the turn.

Returns:
    str: The string representation of the turn, provided by __str__, in the format "&lt;role&gt;: &lt;content&gt;".

Raises:
    None

## Methods

### `__str__`

```python
def __str__(self) -> str
```

