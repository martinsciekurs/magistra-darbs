---
sidebar_position: 127
---

# ModelOutput

**File:** `graphrag/language_model/response/base.py`

## Overview

ModelOutput encapsulates the textual content of a language model's output along with the complete raw JSON response returned by the LLM provider.

Purpose:
    Provide convenient access to both the human-readable content and the full provider response for debugging and downstream processing.

Returns:
    content() -&gt; str: The textual content of the output.
    full_response() -&gt; dict[str, Any] | None: The complete JSON response returned by the model.

## Methods

### `content`

```python
def content(self) -> str
```

### `full_response`

```python
def full_response(self) -> dict[str, Any] | None
```

