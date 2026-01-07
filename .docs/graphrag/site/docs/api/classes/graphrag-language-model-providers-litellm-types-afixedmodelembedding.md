---
sidebar_position: 101
---

# AFixedModelEmbedding

**File:** `graphrag/language_model/providers/litellm/types.py`

## Overview

Callable interface to obtain embeddings via a fixed Litellm model.

This class stores the configuration for a pre-selected model and exposes a callable interface (__call__) that returns an EmbeddingResponse from the underlying Litellm/OpenAI service. Key configuration attributes include the selected model parameters and per-request settings (timeouts, API credentials, and caching) used when requesting embeddings.

Args:
  request_id: str | None (default: None)
      Optional request identifier.
  input: list (default: [])
      List input to embed.
  dimensions: int | None (default: None)
      Optional embedding dimensions.
  encoding_format: str | None (default: None)
      Optional encoding format.
  timeout: int (default: 600)
      Timeout in seconds for the request.
  api_base: str | None (default: None)
      Optional API base.
  api_version: str | None (default: None)
      Optional API version.
  api_key: str | None (default: None)
      Optional API key.
  api_type: str | None (default: None)
      Optional API type.
  caching: bool (default: False)
      Whether to enable caching.
  user: str | None (default: None)
      Optional user.
  **kwargs: Any
      Additional keyword arguments forwarded to the embedding service.

Returns:
  EmbeddingResponse
      The embedding response as produced by the underlying service (type alias to CreateEmbeddingResponse in litellm).

Raises:
  Exception
      Exceptions raised by the embedding service or underlying libraries.

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

