---
sidebar_position: 119
---

# LanguageModelConfigMissingError

**File:** `graphrag/config/errors.py`

## Overview

LanguageModelConfigMissingError is raised when a required language model configuration key is missing from the configuration.

Args:
    key: The key of the missing model configuration. Used to customize the error message in settings.yaml.

Returns:
    None

Raises:
    None

Attributes:
    key: The key of the missing model configuration. Stored on the instance to provide context for the error message.

## Methods

### `__init__`

```python
def __init__(self, key: str = "") -> None
```

