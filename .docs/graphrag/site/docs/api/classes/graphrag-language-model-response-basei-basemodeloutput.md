---
sidebar_position: 134
---

# BaseModelOutput

**File:** `graphrag/language_model/response/base.pyi`

## Overview

BaseModelOutput stores the result produced by a language model, including the main content and an optional full_response payload. Key attributes: content, full_response.

Args:
    content: The output content as a string.
    full_response: Optional dict[str, Any] representing the full response; defaults to None.

Returns:
    None

## Methods

### `__init__`

```python
def __init__(
        self,
        content: str,
        full_response: dict[str, Any] | None = None,
    ) -> None
```

