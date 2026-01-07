---
sidebar_position: 77
---

# ModelResponse

**File:** `graphrag/language_model/response/base.py`

## Overview

ModelResponse is a generic container for responses from an LLM provider. It encapsulates the textual output, the provider's full JSON response, and an optional parsed model instance along with a history of responses. The class is parameterized by T, a subclass of BaseModel, representing a typed interpretation of the response.

Attributes:
  output (ModelOutput): The output associated with this response. Access the textual content via output.content and the complete provider JSON via output.full_response (dict[str, Any] or None).
  history (list[Any]): The history of this response as a list of entries.
  parsed_response (T | None): The parsed model instance of type T, or None if not available.

Notes:
- ModelOutput is a separate type that wraps the textual content and the full provider JSON.
- This docstring describes class-level behavior and fields; initialization parameters, if any, are defined in the implementation.

## Methods

### `output`

```python
def output(self) -> ModelOutput
```

### `history`

```python
def history(self) -> list
```

### `parsed_response`

```python
def parsed_response(self) -> T | None
```

