---
sidebar_position: 279
---

# tests/verbs/util.py

## Overview

Test utilities for verb workflow testing in Graphrag tests.

This module provides helpers to load test data tables, compare outputs, asynchronously update document metadata, and create a test context with test data loaded into storage. It also defines small test configuration constants used by tests, including a fake API key.

Exports:
- FAKE_API_KEY
- DEFAULT_CHAT_MODEL_CONFIG
- DEFAULT_EMBEDDING_MODEL_CONFIG
- DEFAULT_MODEL_CONFIG
- load_test_table(output)
- compare_outputs(actual, expected, columns=None)
- update_document_metadata(metadata, context)
- create_test_context(storage=None)

Functions:

load_test_table(output: str) -&gt; pd.DataFrame
  Load a test table from parquet data using the provided workflow output name.
  Args:
  output: The workflow output name, typically the workflow name, used to locate the parquet file at tests/verbs/data/&#123;output&#125;.parquet.
  Returns:
  pd.DataFrame: The DataFrame read from the specified parquet file.

compare_outputs(actual: pd.DataFrame, expected: pd.DataFrame, columns: list[str] | None = None) -&gt; None
  Compare the actual and expected dataframes, optionally specifying columns to compare. This function uses pandas.testing.assert_series_equal to compare columns and intentionally omits the id column from value checks. If a mismatch is found, the function prints the Expected and Actual values for debugging before raising an AssertionError.
  Args:
  actual: The actual DataFrame produced by the workflow.
  expected: The expected DataFrame to compare against.
  columns: Optional subset of columns to compare.
  Returns:
  None

update_document_metadata(metadata: list[str], context: PipelineRunContext) -&gt; None
  Asynchronously load the documents table from storage, create a new metadata column containing per-row dictionaries built from the selected metadata columns, and write the updated table back to storage.
  Args:
  metadata: List of metadata column names to include in per-row dictionaries.
  context: PipelineRunContext providing storage and context for the operation.
  Returns:
  None

create_test_context(storage: list[str] | None = None) -&gt; PipelineRunContext
  Create a test context with test tables loaded into storage.
  Args:
  storage: list[str] | None — A list of test table names to load from test data and write into the context's output storage. If None, only the documents table is loaded and stored.
  Returns:
  PipelineRunContext: The initialized pipeline run context with the test data loaded into its output storage.

## Functions

- [`load_test_table`](../api/functions/tests-verbs-util-load-test-table)
- [`compare_outputs`](../api/functions/tests-verbs-util-compare-outputs)
- [`update_document_metadata`](../api/functions/tests-verbs-util-update-document-metadata)
- [`create_test_context`](../api/functions/tests-verbs-util-create-test-context)

