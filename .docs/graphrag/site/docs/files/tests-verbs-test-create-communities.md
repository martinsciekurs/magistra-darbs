---
sidebar_position: 268
---

# tests/verbs/test_create_communities.py

## Overview

Tests for the create_communities workflow.

This module defines test_create_communities, which exercises the create_communities workflow by generating final communities and validating the produced output against the test dataset and the expected schema.

Key exports:
  - test_create_communities: test function that runs the workflow and asserts correctness.

Summary:
  The test uses create_graphrag_config to configure the workflow, validates the results against COMMUNITIES_FINAL_COLUMNS, and loads produced data with load_table_from_storage to verify that the final communities table matches expectations.

Args:
  None: This module does not accept any parameters.

Returns:
  None: The tests do not return a value; they perform assertions to verify correctness.

Raises:
  Exception: Exceptions raised by the workflow execution or storage utilities (e.g., failures in loading test data).

## Functions

- [`test_create_communities`](../api/functions/tests-verbs-test-create-communities-test-create-communities)

