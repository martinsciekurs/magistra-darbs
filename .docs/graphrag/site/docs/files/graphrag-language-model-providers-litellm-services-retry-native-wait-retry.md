---
sidebar_position: 160
---

# graphrag/language_model/providers/litellm/services/retry/native_wait_retry.py

## Overview

Retry utilities for native wait-based retry logic used by the Litellm service.

Overview:
This module provides retry capabilities for both asynchronous and synchronous callables using a configurable maximum number of retries. It exposes the NativeRetry class and two helper methods aretry and retry to perform retries as needed.

Public API:
- aretry(self, func, **kwargs): Retry an asynchronous function until it succeeds or the maximum number of retries is reached. The function is awaited and its result is returned. Raises Exception if retries are exhausted.
- retry(self, func, **kwargs): Retry a synchronous function until it succeeds or max_retries is reached. The function is invoked as func(**kwargs) and its result is returned. Raises Exception if the last invocation fails after all retries.
- NativeRetry: Class that encapsulates the retry configuration (max_retries) and exposes aretry and retry for use with asynchronous and synchronous callables.
- __init__(self, *, max_retries: int = 5, **kwargs): Initializes NativeRetry with retry configuration. max_retries must be greater than 0; additional kwargs are accepted but unused.

## Classes

- [`NativeRetry`](../api/classes/graphrag-language-model-providers-litellm-services-retry-native-wait-retry-nativeretry)

## Functions

- [`aretry`](../api/functions/graphrag-language-model-providers-litellm-services-retry-native-wait-retry-aretry)
- [`retry`](../api/functions/graphrag-language-model-providers-litellm-services-retry-native-wait-retry-retry)
- [`__init__`](../api/functions/graphrag-language-model-providers-litellm-services-retry-native-wait-retry-init)

