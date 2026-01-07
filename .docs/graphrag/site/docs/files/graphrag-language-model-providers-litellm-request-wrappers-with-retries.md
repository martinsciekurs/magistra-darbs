---
sidebar_position: 155
---

# graphrag/language_model/providers/litellm/request_wrappers/with_retries.py

## Overview

Utilities to wrap Litellm request functions with retry logic.

This module constructs retry-enabled wrappers for both synchronous and asynchronous
Litellm request functions. It builds a retry service from a LanguageModelConfig and
returns two wrappers: one for synchronous calls and one for asynchronous calls. The
wrappers delegate to the provided functions, applying the configured retry policy.

Key exports:
- _wrapped_with_retries_async
- _wrapped_with_retries
- with_retries

Summary:
Retry configuration is driven by model_config fields: retry_strategy, max_retries, and
max_retry_... (as defined in the project). The wrappers propagate exceptions from the
underlying functions or from the retry service.

Exports details:

- _wrapped_with_retries_async:
  Args: kwargs: Keyword arguments passed to the underlying asynchronous request function.
  Returns: Any: The value returned by the underlying asynchronous request function when called with the provided kwargs.
  Raises: Exception: Propagated from the underlying asynchronous function or the retry service.

- _wrapped_with_retries:
  Args: kwargs: Keyword arguments passed to the underlying synchronous request function.
  Returns: Any: The value returned by the underlying synchronous request function when called with the provided kwargs.
  Raises: Exception: Propagated from the underlying synchronous function or the retry service.

- with_retries:
  Args:
    sync_fn: LitellmRequestFunc
    async_fn: AsyncLitellmRequestFunc
    model_config: LanguageModelConfig
  Returns:
    tuple[LitellmRequestFunc, AsyncLitellmRequestFunc]: The wrapped synchronous and asynchronous
      request functions.
  Raises:
    Exception: Propagated from the underlying functions or the retry service.

## Functions

- [`_wrapped_with_retries_async`](../api/functions/graphrag-language-model-providers-litellm-request-wrappers-with-retries-wrapped-with-retries-async)
- [`_wrapped_with_retries`](../api/functions/graphrag-language-model-providers-litellm-request-wrappers-with-retries-wrapped-with-retries)
- [`with_retries`](../api/functions/graphrag-language-model-providers-litellm-request-wrappers-with-retries-with-retries)

