---
sidebar_position: 158
---

# graphrag/language_model/providers/litellm/services/retry/exponential_retry.py

## Overview

Exponential backoff retry utility for the Litellm integration (LiteLLM provider).

This module exposes ExponentialRetry, a lightweight helper that offers both synchronous and asynchronous retry semantics with exponential backoff and optional jitter to gracefully handle transient failures when calling external services.

Public exports:
- ExponentialRetry: Class implementing exponential backoff retry logic for sync and async callables.

Brief summary:
ExponentialRetry supports configurable max_retries, base_delay, and jitter to control retry behavior for both sync and async operations.

Args:
- max_retries: int. Maximum number of retry attempts. Must be greater than 0. Default: 5.
- base_delay: float. Base delay between retries in seconds. Must be greater than 0.0. Default: 2.0.
- jitter: bool. If True, apply a small random jitter to each delay. Default: True.
- kwargs: Any. Additional keyword arguments for compatibility.

Returns:
- None

Raises:
- ValueError: If max_retries &lt;= 0 or base_delay &lt;= 0.0.

Retry behavior:
- retry: Synchronous retry of a callable. The first retry occurs after an initial delay of 1.0 second and each subsequent delay is multiplied by the base_delay factor. If jitter is enabled, a random amount up to the computed delay is added.
- aretry: Asynchronous retry of an awaitable callable. Follows the same delay progression and jitter rules as retry.

Examples:
- Synchronous usage:
  retryer = ExponentialRetry(max_retries=3, base_delay=1.5, jitter=True)
  result = retryer.retry(some_sync_func, arg1=value1)

- Asynchronous usage:
  retryer = ExponentialRetry(max_retries=3, base_delay=1.5, jitter=True)
  result = await retryer.aretry(some_async_func, arg1=value1)

## Classes

- [`ExponentialRetry`](../api/classes/graphrag-language-model-providers-litellm-services-retry-exponential-retry-exponentialretry)

## Functions

- [`__init__`](../api/functions/graphrag-language-model-providers-litellm-services-retry-exponential-retry-init)
- [`retry`](../api/functions/graphrag-language-model-providers-litellm-services-retry-exponential-retry-retry)
- [`aretry`](../api/functions/graphrag-language-model-providers-litellm-services-retry-exponential-retry-aretry)

