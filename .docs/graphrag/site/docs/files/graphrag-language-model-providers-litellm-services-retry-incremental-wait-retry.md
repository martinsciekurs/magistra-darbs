---
sidebar_position: 159
---

# graphrag/language_model/providers/litellm/services/retry/incremental_wait_retry.py

## Overview

Incremental wait retry strategy for Litellm retry service.

This module defines IncrementalWaitRetry, a retry policy that inserts incremental delays between attempts for both asynchronous and synchronous callables. It retries functions until they succeed or the maximum number of retries is reached, applying an incremental delay that grows with each attempt up to a configured maximum.

Exports:
- IncrementalWaitRetry: Class implementing the incremental wait retry policy with aretry to retry asynchronous callables and retry to retry synchronous callables.

Summary:
Attributes include max_retry_wait (float): The maximum delay between retries in seconds. max_retries (int): The maximum number of retry attempts. base_delay (float, optional): Optional initial delay used in the incremental computation. delay_increment (float, optional): Increment applied to the delay for each retry.

## Classes

- [`IncrementalWaitRetry`](../api/classes/graphrag-language-model-providers-litellm-services-retry-incremental-wait-retry-incrementalwaitretry)

## Functions

- [`__init__`](../api/functions/graphrag-language-model-providers-litellm-services-retry-incremental-wait-retry-init)
- [`aretry`](../api/functions/graphrag-language-model-providers-litellm-services-retry-incremental-wait-retry-aretry)
- [`retry`](../api/functions/graphrag-language-model-providers-litellm-services-retry-incremental-wait-retry-retry)

