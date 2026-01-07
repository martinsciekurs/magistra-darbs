---
sidebar_position: 274
---

# tests/verbs/test_extract_graph_nlp.py

## Overview

Module tests for the extract_graph_nlp workflow in Graphrag.

Purpose:
- Validate that the extract_graph_nlp workflow correctly extracts entities and relationships and persists them to storage as structured tables.

Key exports:
- test_extract_graph_nlp: an asynchronous pytest test that constructs a test context with text units, builds a Graphrag config using create_graphrag_config, runs the workflow, and verifies the produced storage tables.

Overview:
- This module wires together create_graphrag_config, run_workflow, and load_table_from_storage to exercise the end-to-end behavior of the extract_graph_nlp workflow in a test context.

What is validated:
- The resulting storage tables have the expected schema and exact row counts, as asserted by loading the tables from storage and inspecting their structure and size.

Notes:
- The test is asynchronous and does not return a value; it may raise assertion errors if expectations are not met. Exceptions raised by the workflow or storage access will surface as test failures.

## Functions

- [`test_extract_graph_nlp`](../api/functions/tests-verbs-test-extract-graph-nlp-test-extract-graph-nlp)

