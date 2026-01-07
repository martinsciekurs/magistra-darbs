---
sidebar_position: 161
---

# graphrag/language_model/providers/litellm/services/retry/random_wait_retry.py

## Overview

Random wait retry policy module.

Purpose:
Provide a RandomWaitRetry class implementing a retry policy that retries both asynchronous and synchronous functions using a random delay between attempts, up to a configurable maximum number of retries.

Key exports:
- RandomWaitRetry: The retry policy class.

Summary:
Implements a retry mechanism with a uniform random delay in [0, max_retry_wait] between retries, for async and sync functions, inheriting from Retry.

Parameters (configuration):
- max_retry_wait: The maximum delay, in seconds, between retries. The actual delay is drawn uniformly from [0, max_retry_wait].
- max_retries: The maximum number of retry attempts. Must be greater than 0.
- kwargs: Additional keyword arguments (Any).

Returns:
- None: Initialization returns None.

Raises:
- ValueError: max_retries must be greater than 0.
- ValueError: max_retry_wait must be greater than 0.

Notes:
- The module imports asyncio, random, time, and uses the base Retry class.
- Public API: RandomWaitRetry with methods aretry (async) and retry (sync).

## Classes

- [`RandomWaitRetry`](../api/classes/graphrag-language-model-providers-litellm-services-retry-random-wait-retry-randomwaitretry)

## Functions

- [`__init__`](../api/functions/graphrag-language-model-providers-litellm-services-retry-random-wait-retry-init)
- [`aretry`](../api/functions/graphrag-language-model-providers-litellm-services-retry-random-wait-retry-aretry)
- [`retry`](../api/functions/graphrag-language-model-providers-litellm-services-retry-random-wait-retry-retry)

