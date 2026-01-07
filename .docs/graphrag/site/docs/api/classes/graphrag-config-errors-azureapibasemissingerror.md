---
sidebar_position: 34
---

# AzureApiBaseMissingError

**File:** `graphrag/config/errors.py`

## Overview

AzureApiBaseMissingError is an internal exception raised when the Azure API Base configuration is missing for the specified LLM type.

This exception signals that the required Azure API Base is not configured for the given LLM type.

Args:
    llm_type (str): The LLM type for which the API Base is required. The value is stored on the instance as llm_type and used to construct the error message.

Attributes:
    llm_type (str): The LLM type for which the API Base is required. Used to customize the error message.

Notes:
    The __init__ method stores llm_type and creates a descriptive message, typically "Azure API Base missing for LLM type: &#123;llm_type&#125;".

Examples:
    raise AzureApiBaseMissingError('text-davinci-003') results in an exception with a message indicating the missing API Base for that LLM type.

## Methods

### `__init__`

```python
def __init__(self, llm_type: str) -> None
```

