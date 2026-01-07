---
sidebar_position: 236
---

# tests/integration/storage/test_blob_pipeline_storage.py

## Overview

Integration tests for BlobPipelineStorage.

These tests exercise the BlobPipelineStorage class from graphrag.storage.blob_pipeline_storage to verify correct behavior in integration scenarios against a storage backend.

Setup and prerequisites:
Requires a test environment with an accessible storage backend. Tests typically rely on temporary working directories or containers and cleanup after execution.

Test cases:
- test_get_creation_date: verifies that get_creation_date returns a correctly formatted timestamp string for a blob.
- test_dotprefix: verifies correct handling of dot-prefix paths when writing and listing files.
- test_child: verifies that a child BlobPipelineStorage can be created from a parent storage and used for basic file operations.
- test_find: verifies file discovery operations for relevant blob paths.

Notes:
These tests are synchronous; there are no asynchronous operations.

## Functions

- [`test_get_creation_date`](../api/functions/tests-integration-storage-test-blob-pipeline-storage-test-get-creation-date)
- [`test_dotprefix`](../api/functions/tests-integration-storage-test-blob-pipeline-storage-test-dotprefix)
- [`test_child`](../api/functions/tests-integration-storage-test-blob-pipeline-storage-test-child)
- [`test_find`](../api/functions/tests-integration-storage-test-blob-pipeline-storage-test-find)

