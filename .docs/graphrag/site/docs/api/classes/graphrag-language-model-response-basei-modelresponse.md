---
sidebar_position: 85
---

# ModelResponse

**File:** `graphrag/language_model/response/base.pyi`

## Overview

Protocol describing a model response produced by the GraphRAG language model integration. This Protocol exposes three properties: parsed_response, history, and output, and is generic over _T, the type of the parsed response.

Type parameters:
- _T: The type of the parsed_response value.

Attributes:
- parsed_response: _T | None — The parsed response, or None if not available.
- history: list[Any] — The history of the model responses as a list of items.
- output: ModelOutput — The structured output for this response. ModelOutput is defined elsewhere and typically exposes:
  - content: str — The textual content of the output.
  - full_response: dict[str, Any] | None — The full JSON response from the LLM provider, or None if not available.

## Methods

### `parsed_response`

```python
def parsed_response(self) -> _T | None
```

### `history`

```python
def history(self) -> list[Any]
```

### `output`

```python
def output(self) -> ModelOutput
```

