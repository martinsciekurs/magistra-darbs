---
sidebar_position: 154
---

# graphrag/language_model/providers/litellm/request_wrappers/with_rate_limiter.py

## Overview

Utilities to apply rate limiting wrappers to Litellm request functions.

This module provides asynchronous and synchronous wrappers that enforce rate limiting on Litellm request functions by using a rate limiter factory and token counting based on the request content (messages or input) and model configuration.

Key exports:
- _wrapped_with_rate_limiter_async(**kwargs) -&gt; Any: Asynchronous wrapper that applies rate limiting to a request function.
- with_rate_limiter(sync_fn: LitellmRequestFunc, async_fn: AsyncLitellmRequestFunc, model_config: "LanguageModelConfig", rpm: int | None = None, tpm: int | None = None) -&gt; tuple[LitellmRequestFunc, AsyncLitellmRequestFunc]: Wraps the synchronous and asynchronous Litellm request functions with rate limiting and returns the wrapped functions.
- _wrapped_with_rate_limiter(**kwargs) -&gt; Any: Synchronous wrapper variant.

Brief summary:
Provides wrappers to apply rate limiting to Litellm request functions for both synchronous and asynchronous use cases, leveraging litellm.token_counter and the RateLimiterFactory.

## Functions

- [`_wrapped_with_rate_limiter_async`](../api/functions/graphrag-language-model-providers-litellm-request-wrappers-with-rate-limiter-wrapped-with-rate-limiter-async)
- [`with_rate_limiter`](../api/functions/graphrag-language-model-providers-litellm-request-wrappers-with-rate-limiter-with-rate-limiter)
- [`_wrapped_with_rate_limiter`](../api/functions/graphrag-language-model-providers-litellm-request-wrappers-with-rate-limiter-wrapped-with-rate-limiter)

