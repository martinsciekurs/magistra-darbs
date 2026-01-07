---
sidebar_position: 234
---

# tests/integration/logging/test_factory.py

## Overview

Tests for the integration of the logger factory and blob workflow logger used in Graphrag's logging system.

Purpose
- Validate logger creation and management through LoggerFactory, verify that built-in logger types are registered, ensure an unknown logger type raises an error, and confirm that custom loggers can be registered and instantiated.

Key exports
- LoggerFactory: Factory for creating configured logger instances.
- BlobWorkflowLogger: Logger implementation for blob-based logging.
- ReportingType: Enum of supported reporting types.
- test_create_blob_logger: Test for creating a blob logger via LoggerFactory (skipped in this environment). If executed, it would construct kwargs including type: "blob", connection_string, base_dir, container_name and create the logger.
- test_create_unknown_logger: Test that creating an unknown logger type raises ValueError.
- test_get_logger_types: Verify that built-in logger types are registered and returned by LoggerFactory.get_logger_types.
- test_register_and_create_custom_logger: Test registering and creating a custom logger type. It registers a custom "custom" logger via LoggerFactory.register, creates it via LoggerFactory.create_logger, and asserts that the factory was invoked and the created logger has initialized attributes as expected.

Brief summary
- This module encapsulates tests for core logger factory behavior and extensibility, using mocks where appropriate, and documents expected outcomes for each scenario.

## Functions

- [`test_create_blob_logger`](../api/functions/tests-integration-logging-test-factory-test-create-blob-logger)
- [`test_create_unknown_logger`](../api/functions/tests-integration-logging-test-factory-test-create-unknown-logger)
- [`test_get_logger_types`](../api/functions/tests-integration-logging-test-factory-test-get-logger-types)
- [`test_register_and_create_custom_logger`](../api/functions/tests-integration-logging-test-factory-test-register-and-create-custom-logger)

