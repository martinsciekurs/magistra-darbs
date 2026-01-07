---
sidebar_position: 252
---

# tests/unit/indexing/input/test_json_loader.py

## Overview

Tests for the JSON loader input used in indexing tests.

Purpose:
This module contains unit tests that verify the JSON loader path for input loading by constructing InputConfig and StorageConfig, loading documents with create_input, and validating the resulting DataFrame shapes and contents across various scenarios such as single/multiple files and presence of metadata or explicit title fields.

Key exports:
- test_json_loader_one_file_one_object
- test_json_loader_one_file_multiple_objects
- test_json_loader_one_file_with_title
- test_json_loader_one_file_with_metadata
- test_json_loader_multiple_files

Summary:
Tests cover loading a single JSON file with one object, a single file with multiple objects, a single file with a title column, a file including metadata, and loading from multiple JSON files to ensure correct integration and data representation.

Args:
None

Returns:
None

Raises:
None

## Functions

- [`test_json_loader_one_file_one_object`](../api/functions/tests-unit-indexing-input-test-json-loader-test-json-loader-one-file-one-object)
- [`test_json_loader_one_file_multiple_objects`](../api/functions/tests-unit-indexing-input-test-json-loader-test-json-loader-one-file-multiple-objects)
- [`test_json_loader_one_file_with_title`](../api/functions/tests-unit-indexing-input-test-json-loader-test-json-loader-one-file-with-title)
- [`test_json_loader_one_file_with_metadata`](../api/functions/tests-unit-indexing-input-test-json-loader-test-json-loader-one-file-with-metadata)
- [`test_json_loader_multiple_files`](../api/functions/tests-unit-indexing-input-test-json-loader-test-json-loader-multiple-files)

