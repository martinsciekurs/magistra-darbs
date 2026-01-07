---
sidebar_position: 150
---

# FixedModelEmbedding

**File:** `graphrag/language_model/providers/litellm/types.py`

## Overview

FixedModelEmbedding: Synchronous embedding function for a pre-configured model.

This class provides an embedding interface that uses a pre-configured model. It computes embeddings for a batch of inputs using the configured model and does not require a model parameter. It mirrors litellm.embedding but omits the model argument, relying on the model configuration.

Args:
  request_id: Optional request identifier.
  input: List of inputs to embed.
  dimensions: Embedding dimensionality to request (optional).
  encoding_format: Encoding format to return (optional).
  timeout: Timeout for the embedding request in seconds (default to 600, i.e., 10 minutes).
  api_base: API base URL override (optional).
  api_version: API version override (optional).
  api_key: API key override (optional).
  api_type: API type override (optional).
  caching: Enable/disable caching.
  user: User identifier (optional).
  **kwargs: Additional keyword arguments.

Returns:
  EmbeddingResponse: The embedding response containing the computed embeddings.

Raises:
  Exception: If an error occurs during embedding computation or API calls (propagates from underlying libraries).

## Methods

### `__call__`

```python
def __call__(
        self,
        *,
        request_id: str | None = None,
        input: list = [],  # type: ignore  # noqa: B006
        # Optional params
        dimensions: int | None = None,
        encoding_format: str | None = None,
        timeout: int = 600,  # default to 10 minutes
        # set api_base, api_version, api_key
        api_base: str | None = None,
        api_version: str | None = None,
        api_key: str | None = None,
        api_type: str | None = None,
        caching: bool = False,
        user: str | None = None,
        **kwargs: Any,
    ) -> EmbeddingResponse
```

