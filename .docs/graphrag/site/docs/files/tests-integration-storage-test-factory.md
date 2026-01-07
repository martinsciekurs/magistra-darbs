---
sidebar_position: 238
---

# tests/integration/storage/test_factory.py

## Overview

Integration tests for the StorageFactory integration in the graphrag package.

Purpose:
- Verify that StorageFactory can register and instantiate storage backends for built-in storage types (file, memory, blob, cosmosdb) and handle custom registrations.
- Validate behavior when requesting unknown storage types and using a test double implementing PipelineStorage.

Key exports:
- CustomStorage: A test double implementing the PipelineStorage interface used for integration tests.
- StorageFactory: The factory under test that creates storage backend instances.

Summary:
This module defines tests that exercise the StorageFactory's registration, creation, and type-resolution paths, ensuring the correct storage backend instances are produced for various storage types and that custom registrations are honored.

Args:
- None

Returns:
- None

Raises:
- ValueError: In tests that exercise unknown storage types (e.g., test_create_unknown_storage).

## Classes

- [`CustomStorage`](../api/classes/tests-integration-storage-test-factory-customstorage)

## Functions

- [`get`](../api/functions/tests-integration-storage-test-factory-get)
- [`test_register_class_directly_works`](../api/functions/tests-integration-storage-test-factory-test-register-class-directly-works)
- [`get_creation_date`](../api/functions/tests-integration-storage-test-factory-get-creation-date)
- [`test_get_storage_types`](../api/functions/tests-integration-storage-test-factory-test-get-storage-types)
- [`test_create_blob_storage`](../api/functions/tests-integration-storage-test-factory-test-create-blob-storage)
- [`delete`](../api/functions/tests-integration-storage-test-factory-delete)
- [`find`](../api/functions/tests-integration-storage-test-factory-find)
- [`test_create_file_storage`](../api/functions/tests-integration-storage-test-factory-test-create-file-storage)
- [`test_create_unknown_storage`](../api/functions/tests-integration-storage-test-factory-test-create-unknown-storage)
- [`keys`](../api/functions/tests-integration-storage-test-factory-keys)
- [`child`](../api/functions/tests-integration-storage-test-factory-child)
- [`test_register_and_create_custom_storage`](../api/functions/tests-integration-storage-test-factory-test-register-and-create-custom-storage)
- [`test_create_cosmosdb_storage`](../api/functions/tests-integration-storage-test-factory-test-create-cosmosdb-storage)
- [`has`](../api/functions/tests-integration-storage-test-factory-has)
- [`clear`](../api/functions/tests-integration-storage-test-factory-clear)
- [`test_create_memory_storage`](../api/functions/tests-integration-storage-test-factory-test-create-memory-storage)
- [`set`](../api/functions/tests-integration-storage-test-factory-set)
- [`__init__`](../api/functions/tests-integration-storage-test-factory-init)

