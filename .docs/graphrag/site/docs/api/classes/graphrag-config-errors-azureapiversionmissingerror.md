---
sidebar_position: 149
---

# AzureApiVersionMissingError

**File:** `graphrag/config/errors.py`

## Overview

AzureApiVersionMissingError is a specialized ValueError indicating that an API version is required for a given LLM type.

The constructor formats the error message using the provided llm_type as: "API Version is required for &#123;llm_type&#125;. Please rerun graphrag init and set the api_version." It initializes the base ValueError with that message.

Args:
  llm_type: The LLM type for which the API version is required.

Returns:
  None. The __init__ method returns None and initializes the base ValueError with the constructed message.

Raises:
  None

## Methods

### `__init__`

```python
def __init__(self, llm_type: str) -> None
```

