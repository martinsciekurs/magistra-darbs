---
sidebar_position: 71
---

# ApiKeyMissingError

**File:** `graphrag/config/errors.py`

## Overview

Exception raised when an API key is missing for a specific LLM type; this internal error is meant to be raised, not returned. The error message constructed for this exception includes the llm_type and, if provided, the azure_auth_type to aid diagnosis.

Attributes:
    llm_type: The LLM type for which the API Key is required.
    azure_auth_type: Optional Azure authentication type; included in the message if provided.

Args:
    llm_type: The LLM type for which the API Key is required.
    azure_auth_type: Optional Azure authentication type; if provided, included in the message.

## Methods

### `__init__`

```python
def __init__(self, llm_type: str, azure_auth_type: str | None = None) -> None
```

