---
sidebar_position: 272
---

# tests/verbs/test_extract_covariates.py

## Overview

Tests for covariates extraction workflow using mocked LLM responses.

Purpose
This module provides unit tests for the covariates extraction workflow in Graphrag. It defines test_extract_covariates to verify that the workflow correctly extracts covariates given mocked LLM responses.

Key exports
- test_extract_covariates: unit test that exercises the covariates extraction workflow.
- MOCK_LLM_RESPONSES: a list of mocked language model responses used to drive the test.

Brief summary
The test imports utilities and components such as create_graphrag_config, ModelType, COVARIATES_FINAL_COLUMNS, and load_table_from_storage, then runs the extraction workflow with run_workflow and validates results against stored test data.

## Functions

- [`test_extract_covariates`](../api/functions/tests-verbs-test-extract-covariates-test-extract-covariates)

