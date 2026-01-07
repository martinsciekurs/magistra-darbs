---
sidebar_position: 239
---

# tests/integration/storage/test_file_pipeline_storage.py

## Overview

Integration tests for FilePipelineStorage demonstrating asynchronous file operations.

Purpose
This test module exercises the FilePipelineStorage implementation from graphrag.storage.file_pipeline_storage. It verifies core behaviors such as find (listing .txt files under a base directory), get (reading file contents and verifying existence), set (creating new files), delete (removing files), and get_creation_date (returning a correctly formatted timestamp for a blob).

Key exports
- FilePipelineStorage

Summary
The tests cover basic storage operations, child storage interactions, and creation-date formatting to ensure correct integration behavior in asynchronous contexts.

## Functions

- [`test_find`](../api/functions/tests-integration-storage-test-file-pipeline-storage-test-find)
- [`test_child`](../api/functions/tests-integration-storage-test-file-pipeline-storage-test-child)
- [`test_get_creation_date`](../api/functions/tests-integration-storage-test-file-pipeline-storage-test-get-creation-date)

