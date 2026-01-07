---
sidebar_position: 156
---

# graphrag/language_model/providers/litellm/services/rate_limiter/rate_limiter.py

## Overview

Rate limiter interface for implementing rate limiting strategies.

This module defines an abstract base class RateLimiter that specifies the interface for rate limiting strategies. Concrete subclasses must implement their own initialization logic and provide a concrete acquire method that returns a context manager guarding a request.

Public exports:
- RateLimiter: Abstract base class for rate limiting strategies.

Args:
  __init__(self, /, **kwargs: Any): Abstract initializer for rate limiters. Subclasses must implement their own initialization logic; this method should not perform concrete initialization.
  acquire(self, *, token_count: int) -&gt; Iterator[None]: Acquire Rate Limiter. The estimated number of tokens for the current request.

Returns:
  None: For __init__
  Iterator[None]: A context manager that yields None.

Raises:
  NotImplementedError: RateLimiter subclasses must implement the acquire method.

## Classes

- [`RateLimiter`](../api/classes/graphrag-language-model-providers-litellm-services-rate-limiter-rate-limiter-ratelimiter)

## Functions

- [`__init__`](../api/functions/graphrag-language-model-providers-litellm-services-rate-limiter-rate-limiter-init)
- [`acquire`](../api/functions/graphrag-language-model-providers-litellm-services-rate-limiter-rate-limiter-acquire)

