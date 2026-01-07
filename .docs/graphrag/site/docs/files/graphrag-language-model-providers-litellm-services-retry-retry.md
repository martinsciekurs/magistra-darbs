---
sidebar_position: 162
---

# graphrag/language_model/providers/litellm/services/retry/retry.py

## Overview

Retry utilities for Litellm language model retry mechanism.

Purpose: This module defines an abstract base class that specifies the interface for applying configurable retry policies to operations, enabling pluggable retry strategies for both synchronous and asynchronous callables used by Litellm.

Key exports:
- class Retry: Abstract base class that defines the interface for applying a configurable retry policy to operations. Public methods: retry, aretry. Subclasses may initialize with arbitrary keyword arguments to configure their strategies.

Brief summary: The Retry class provides an abstract interface for retrying operations. Concrete implementations must override retry for synchronous callables and aretry for asynchronous callables, allowing different retry policies (e.g., max_retries, backoff, jitter) to be plugged in as needed.

## Classes

- [`Retry`](../api/classes/graphrag-language-model-providers-litellm-services-retry-retry-retry)

## Functions

- [`retry`](../api/functions/graphrag-language-model-providers-litellm-services-retry-retry-retry)
- [`__init__`](../api/functions/graphrag-language-model-providers-litellm-services-retry-retry-init)
- [`aretry`](../api/functions/graphrag-language-model-providers-litellm-services-retry-retry-aretry)

