---
sidebar_position: 148
---

# BaseModelResponse

**File:** `graphrag/language_model/response/base.pyi`

## Overview

BaseModelResponse is a generic container for the response produced by a base language model. It pairs the raw model output with optional parsed content and related metadata, and is parameterized by the type _T of the parsed response. The actual raw content is held in output (BaseModelOutput), while parsed_response holds a typed interpretation if available.

Args:
    output: BaseModelOutput
        BaseModelOutput instance containing the content and full_response produced by the base model.
    parsed_response: _T | None
        The parsed response of type _T, or None if no parsing was performed.
    history: list[Any]
        History list related to the interaction; defaults are provided by the Pydantic framework.
    tool_calls: list[Any]
        Tool calls associated with the response; defaults are provided by the Pydantic framework.
    metrics: Any | None
        Optional metrics about the response (e.g., latency, resource usage).
    cache_hit: bool | None
        Indicates whether a cached response was used, if applicable.

Attributes:
    output: BaseModelOutput
        Raw model output content and full_response.
    parsed_response: _T | None
        Parsed content of type _T, if available.
    history: list[Any]
        Interaction history;
    tool_calls: list[Any]
        Tool calls associated with the response.
    metrics: Any | None
        Optional metrics about the response.
    cache_hit: bool | None
        Whether a cached response was used.

Returns:
    None. The constructor is provided by the Pydantic BaseModel superclass; this class does not implement a custom __init__.

Raises:
    None

## Methods

### `__init__`

```python
def __init__(
        self,
        output: BaseModelOutput,
        parsed_response: _T | None = None,
        history: list[Any] = ...,  # default provided by Pydantic
        tool_calls: list[Any] = ...,  # default provided by Pydantic
        metrics: Any | None = None,
        cache_hit: bool | None = None,
    ) -> None
```

