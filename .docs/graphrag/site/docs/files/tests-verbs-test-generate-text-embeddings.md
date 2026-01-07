---
sidebar_position: 276
---

# tests/verbs/test_generate_text_embeddings.py

## Overview

Test suite for the generate_text_embeddings workflow.

Purpose
Tests the generate_text_embeddings workflow using a mock embedding model and validates produced embeddings and the corresponding storage artifacts.

Key exports
- test_generate_text_embeddings: test function that sets up a test context with multiple storage tables, configures Graphrag embedding to use a mock embedding model, runs the workflow, and asserts that a parquet named embeddings.&#123;field&#125;.parquet exists in the output storage for every embedding field.

Brief summary
This module defines a single test that exercises the end-to-end generation of text embeddings and their storage artifacts.

## Functions

- [`test_generate_text_embeddings`](../api/functions/tests-verbs-test-generate-text-embeddings-test-generate-text-embeddings)

