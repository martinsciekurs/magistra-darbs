---
sidebar_position: 153
---

# graphrag/language_model/providers/litellm/request_wrappers/with_logging.py

## Overview

Utilities to wrap Litellm request functions with logging for exceptions.

Overview
This module provides wrapper utilities to log exceptions raised by Litellm request
functions (synchronous and asynchronous) and re-raise them, preserving normal
error propagation. It exports three main items: _wrapped_with_logging, _wrapped_with_logging_async,
and with_logging.

Functions
- _wrapped_with_logging(**kwargs: Any) -&gt; Any: Wraps the synchronous request function with logging.
  Args: kwargs: Keyword arguments passed to the underlying synchronous request function.
  Returns: Any: The value returned by the underlying sync_fn when called with the provided kwargs.
  Raises: Exception: Re-raised after logging the exception encountered during the call.

- _wrapped_with_logging_async(**kwargs: Any) -&gt; Any: Wraps the asynchronous request function with logging.
  Args: kwargs: Keyword arguments passed to the underlying asynchronous request function.
  Returns: Any: The value returned by the underlying async_fn when called with the provided kwargs.
  Raises: Exception: Re-raised after logging the exception encountered during the call.

- with_logging(*, sync_fn: LitellmRequestFunc, async_fn: AsyncLitellmRequestFunc) -&gt; tuple[LitellmRequestFunc, AsyncLitellmRequestFunc]:
  Wrap the provided synchronous and asynchronous Litellm request functions with logging for exceptions.
  Args:
    sync_fn: LitellmRequestFunc The synchronous chat/embedding request function to wrap.
    async_fn: AsyncLitellmRequestFunc The asynchronous chat/embedding request function to wrap.
  Returns:
    tuple[LitellmRequestFunc, AsyncLitellmRequestFunc]: A tuple of the wrapped synchronous and asynchronous functions.
  Raises:
    Exception: Re-raised after logging if an error occurs in the wrapped functions during execution.

Notes
- Exports: _wrapped_with_logging, _wrapped_with_logging_async, with_logging
- The wrappers log exceptions and then propagate them to maintain standard error handling.

## Functions

- [`_wrapped_with_logging`](../api/functions/graphrag-language-model-providers-litellm-request-wrappers-with-logging-wrapped-with-logging)
- [`_wrapped_with_logging_async`](../api/functions/graphrag-language-model-providers-litellm-request-wrappers-with-logging-wrapped-with-logging-async)
- [`with_logging`](../api/functions/graphrag-language-model-providers-litellm-request-wrappers-with-logging-with-logging)

