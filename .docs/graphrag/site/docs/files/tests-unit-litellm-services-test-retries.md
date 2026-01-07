---
sidebar_position: 261
---

# tests/unit/litellm_services/test_retries.py

## Overview

Tests for retry behavior in litellm service retry framework.

This module provides unit tests for retry functionality implemented through RetryFactory, covering asynchronous and synchronous retry flows and a mock function used to trigger retries for timing assertions.

Key exports:
- test_retries_async
- test_retries
- mock_func

Functions:
test_retries_async(strategy: str, max_retries: int, max_retry_wait: int, expected_time: float) -&gt; None
    Test various retry strategies asynchronously.
    Args:
        strategy: The retry strategy to use.
        max_retries: The maximum number of retry attempts.
        max_retry_wait: The maximum wait time between retries.
        expected_time: The minimum elapsed time expected for the retries to complete.
    Returns:
        None
    Raises:
        ValueError: If an invalid strategy is supplied or timing constraints fail.

test_retries(strategy: str, max_retries: int, max_retry_wait: int, expected_time: float) -&gt; None
    Test various retry strategies by exercising a mock function that raises an exception to verify retry behavior and timing.
    Args:
        strategy: The retry strategy to use.
        max_retries: The maximum number of retry attempts.
        max_retry_wait: The maximum wait time between retries.
        expected_time: The minimum elapsed time expected for the retries to complete.
    Returns:
        None
    Raises:
        ValueError: If an invalid strategy is supplied or timing constraints fail.

mock_func()
    Mock function used for testing retries.
    Returns:
        None: This function does not return normally because it always raises ValueError.
    Raises:
        ValueError: Mock error for testing retries.

## Functions

- [`test_retries_async`](../api/functions/tests-unit-litellm-services-test-retries-test-retries-async)
- [`test_retries`](../api/functions/tests-unit-litellm-services-test-retries-test-retries)
- [`mock_func`](../api/functions/tests-unit-litellm-services-test-retries-mock-func)

