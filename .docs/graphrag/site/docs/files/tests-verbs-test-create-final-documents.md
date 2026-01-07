---
sidebar_position: 270
---

# tests/verbs/test_create_final_documents.py

## Overview

Tests for the final documents creation workflow in Graphrag.

This module contains asynchronous tests that verify the end-to-end generation of
final documents from input units. The tests load expected documents data, initialize a test
context with text_units storage, build a Graphrag configuration, run the final documents
workflow, and compare the produced documents against the expected data. The tests also cover a
scenario where a metadata column is provided, ensuring metadata construction is integrated during
initial input loading and reflected in the final documents.

Key exports:
- test_create_final_documents
- test_create_final_documents_with_metadata_column

Args: None

Returns: None

Raises: None

## Functions

- [`test_create_final_documents`](../api/functions/tests-verbs-test-create-final-documents-test-create-final-documents)
- [`test_create_final_documents_with_metadata_column`](../api/functions/tests-verbs-test-create-final-documents-test-create-final-documents-with-metadata-column)

