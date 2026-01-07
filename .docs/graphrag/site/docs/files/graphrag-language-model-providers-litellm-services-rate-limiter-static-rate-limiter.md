---
sidebar_position: 157
---

# graphrag/language_model/providers/litellm/services/rate_limiter/static_rate_limiter.py

## Overview

Fixed-per-period rate limiter for RPM and TPM with optional staggering.

Overview
The StaticRateLimiter enforces two independent per-period limits:
- RPM: maximum number of requests allowed per period
- TPM: maximum number of tokens allowed per period
The counters reset at the end of each period defined by period_in_seconds. Passing
None for rpm disables RPM limiting; passing None for tpm disables TPM limiting.
An optional default_stagger allows you to insert a fixed delay between successive
requests. All limits and timing are evaluated within a sliding window of the period.

Public API
- StaticRateLimiter: class implementing the rate-limiting logic
  __init__(rpm, tpm, default_stagger, period_in_seconds, **kwargs)
  acquire(token_count)

Usage
- Example:
  limiter = StaticRateLimiter(rpm=60, tpm=1000, period_in_seconds=60)
  with limiter.acquire(token_count=5):
      ...

Args
- rpm: int | None
  RPM limit; positive integer or None to disable.
- tpm: int | None
  TPM limit; positive integer or None to disable.
- default_stagger: float
  Default stagger between requests; must be &gt;= 0.
- period_in_seconds: int
  Length of the period in seconds; must be a positive integer.
- kwargs: Any
  Additional configuration options (reserved for future use).

Acquire()
- token_count: int
  Estimated number of tokens for the current request.

Returns
- Iterator[None]
  A context manager yielding None and guarding the protected block.

Raises
- ValueError
  If any configuration parameter is invalid (e.g., negative values or non-sensical inputs).

## Classes

- [`StaticRateLimiter`](../api/classes/graphrag-language-model-providers-litellm-services-rate-limiter-static-rate-limiter-staticratelimiter)

## Functions

- [`__init__`](../api/functions/graphrag-language-model-providers-litellm-services-rate-limiter-static-rate-limiter-init)
- [`acquire`](../api/functions/graphrag-language-model-providers-litellm-services-rate-limiter-static-rate-limiter-acquire)

