---
sidebar_position: 260
---

# tests/unit/litellm_services/test_rate_limiter.py

## Overview

Unit tests for the rate limiter components (RateLimiter and RateLimiterFactory) used by Litellm services in Graphrag.

This test module exercises RateLimiter and RateLimiterFactory, validating their behavior under various configurations such as valid and invalid parameters, and scenarios enforcing RPM (requests per minute) and TPM (tokens per minute) limits, time-based binning of acquisitions, and threaded execution. It relies on test utilities assert_max_num_values_per_period, assert_stagger, and bin_time_intervals.

Key components exercised and tested include:
- RateLimiter
- RateLimiterFactory
- Test functions such as test_rate_limiter_validation, _run_rate_limiter, test_binning, test_rpm, test_tpm, test_token_in_request_exceeds_tpm, test_rpm_and_tpm_with_rpm_as_limiting_factor, test_rpm_and_tpm_with_tpm_as_limiting_factor, test_rpm_threaded, test_tpm_threaded

## Functions

- [`test_rate_limiter_validation`](../api/functions/tests-unit-litellm-services-test-rate-limiter-test-rate-limiter-validation)
- [`_run_rate_limiter`](../api/functions/tests-unit-litellm-services-test-rate-limiter-run-rate-limiter)
- [`test_binning`](../api/functions/tests-unit-litellm-services-test-rate-limiter-test-binning)
- [`test_rpm`](../api/functions/tests-unit-litellm-services-test-rate-limiter-test-rpm)
- [`test_tpm`](../api/functions/tests-unit-litellm-services-test-rate-limiter-test-tpm)
- [`test_token_in_request_exceeds_tpm`](../api/functions/tests-unit-litellm-services-test-rate-limiter-test-token-in-request-exceeds-tpm)
- [`test_rpm_and_tpm_with_rpm_as_limiting_factor`](../api/functions/tests-unit-litellm-services-test-rate-limiter-test-rpm-and-tpm-with-rpm-as-limiting-factor)
- [`test_rpm_and_tpm_with_tpm_as_limiting_factor`](../api/functions/tests-unit-litellm-services-test-rate-limiter-test-rpm-and-tpm-with-tpm-as-limiting-factor)
- [`test_rpm_threaded`](../api/functions/tests-unit-litellm-services-test-rate-limiter-test-rpm-threaded)
- [`test_tpm_threaded`](../api/functions/tests-unit-litellm-services-test-rate-limiter-test-tpm-threaded)

