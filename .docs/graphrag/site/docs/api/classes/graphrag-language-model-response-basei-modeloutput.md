---
sidebar_position: 53
---

# ModelOutput

**File:** `graphrag/language_model/response/base.pyi`

## Overview

ModelOutput: Represents the outcome produced by a language model, providing access to the textual content and the complete raw payload when available.

Purpose:
  Encapsulates model output data and provides convenient accessors to the core content and the full payload.

Methods:
  content() -&gt; str
    Returns the textual content of the model output as a string.

  full_response() -&gt; dict[str, Any] | None
    Returns the full raw response payload as a dictionary, or None if available.

Notes:
  These are methods (not attributes). Access data by calling content() and full_response() on the instance.

## Methods

### `full_response`

```python
def full_response(self) -> dict[str, Any] | None
```

### `content`

```python
def content(self) -> str
```

