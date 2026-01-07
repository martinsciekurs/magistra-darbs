---
sidebar_position: 269
---

# tests/verbs/test_create_community_reports.py

## Overview

Tests for the create_community_reports workflow used in graphrag tests.

Purpose:
Validate that the create_community_reports workflow produces the expected community_reports output when using predetermined mock responses and test data.

Key exports:
- MOCK_RESPONSES: top-level data used to mock language model responses during tests
- test_create_community_reports: test function that exercises the workflow and asserts that the produced output matches the expected dataset

Brief summary:
The tests load test data into a test context, configure a mock language model with predefined responses, run the workflow to generate community reports, and assert that the resulting community_reports table matches the expected test data, including specific checks.

Args:
    None: This module does not define a function that accepts arguments.

Returns:
    None: This module does not return a value.

Raises:
    AssertionError: If a test assertion fails.
    Exception: If an unexpected error occurs during test execution.

## Functions

- [`test_create_community_reports`](../api/functions/tests-verbs-test-create-community-reports-test-create-community-reports)

