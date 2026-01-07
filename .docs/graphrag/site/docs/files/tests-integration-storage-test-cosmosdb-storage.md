---
sidebar_position: 237
---

# tests/integration/storage/test_cosmosdb_storage.py

## Overview

CosmosDBPipelineStorage integration tests for the Graphrag project.

Purpose:
    Provide integration tests for CosmosDBPipelineStorage as implemented in graphrag.storage.cosmosdb_pipeline_storage. The tests exercise creation date formatting, clearing storage, child storage creation, and find/list behavior against a test Cosmos DB container.

Key exports:
    test_get_creation_date
    test_clear
    test_child
    test_find

Summary:
    The tests verify correct timestamp formatting for creation dates, ensure storage is fully cleared and internal clients are reset, validate the ability to create child storages from a parent, and exercise the end-to-end find/list operations in a test container.

Args:
    None

Returns:
    None

Raises:
    None

## Functions

- [`test_get_creation_date`](../api/functions/tests-integration-storage-test-cosmosdb-storage-test-get-creation-date)
- [`test_clear`](../api/functions/tests-integration-storage-test-cosmosdb-storage-test-clear)
- [`test_child`](../api/functions/tests-integration-storage-test-cosmosdb-storage-test-child)
- [`test_find`](../api/functions/tests-integration-storage-test-cosmosdb-storage-test-find)

