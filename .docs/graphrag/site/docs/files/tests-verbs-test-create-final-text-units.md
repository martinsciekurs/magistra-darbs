---
sidebar_position: 271
---

# tests/verbs/test_create_final_text_units.py

## Overview

Tests for the asynchronous creation of final text units in Graphrag.

This module contains tests that exercise the create_final_text_units workflow. It imports configuration, the expected final text units schema, the workflow runner, and storage utilities to validate that the produced output matches the test table used for verification.

Key exports:
- test_create_final_text_units: Test the asynchronous creation of final text units and validate the produced output against the expected test table. Returns: None. This test does not return a value; it asserts correctness by comparing actual output to expected data.

Brief summary:
This test ensures end-to-end correctness of final text unit creation by invoking the workflow with the configured environment and comparing the produced data to the test table schema TEXT_UNITS_FINAL_COLUMNS loaded from storage.

## Functions

- [`test_create_final_text_units`](../api/functions/tests-verbs-test-create-final-text-units-test-create-final-text-units)

