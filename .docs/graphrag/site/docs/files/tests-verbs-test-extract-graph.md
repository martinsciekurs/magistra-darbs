---
sidebar_position: 273
---

# tests/verbs/test_extract_graph.py

## Overview

Tests for the extract_graph workflow in graphrag.

Purpose
This module defines tests for the extract_graph workflow, ensuring that the workflow
executes with a test context and mocked LLM responses, persists the resulting
entities and relationships to storage, and validates the stored graph against
the expected schema and content.

Key exports
- test_extract_graph: test function that exercises the end-to-end extract_graph workflow.

Top-level data
- MOCK_LLM_ENTITY_RESPONSES: mocked entity responses used by tests.
- MOCK_LLM_SUMMARIZATION_RESPONSES: mocked summarization responses used by tests.

Dependencies
The tests rely on create_graphrag_config, ModelType, run_workflow, and
load_table_from_storage, as well as utilities from the test suite.

## Functions

- [`test_extract_graph`](../api/functions/tests-verbs-test-extract-graph-test-extract-graph)

