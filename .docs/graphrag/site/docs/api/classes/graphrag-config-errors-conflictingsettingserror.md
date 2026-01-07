---
sidebar_position: 135
---

# ConflictingSettingsError

**File:** `graphrag/config/errors.py`

## Overview

Exception raised when configuration contains conflicting or incompatible settings.

Represents an error condition raised during GraphRAG configuration when two or more settings conflict with each other. The error message provided at initialization describes the specific conflict and is passed to the base ValueError constructor.

Args:
    msg: The error message to pass to the base ValueError constructor.

Returns:
    None

Raises:
    None

## Methods

### `__init__`

```python
def __init__(self, msg: str) -> None
```

