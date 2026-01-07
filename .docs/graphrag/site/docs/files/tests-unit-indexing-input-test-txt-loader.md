---
sidebar_position: 253
---

# tests/unit/indexing/input/test_txt_loader.py

## Overview

Tests for the TXT input loader used in the indexing input path.

Purpose
Unit tests for loading TXT files via the input loader. The tests cover loading a single TXT file, loading with metadata, and loading multiple TXT files.

Key exports
test_txt_loader_one_file
test_txt_loader_one_file_with_metadata
test_txt_loader_multiple_files

Summary
These tests exercise the integration of the input factory (create_input) and storage creation (create_storage_from_config) with TXT data loading to verify DataFrame shapes and metadata handling.

## Functions

- [`test_txt_loader_one_file`](../api/functions/tests-unit-indexing-input-test-txt-loader-test-txt-loader-one-file)
- [`test_txt_loader_one_file_with_metadata`](../api/functions/tests-unit-indexing-input-test-txt-loader-test-txt-loader-one-file-with-metadata)
- [`test_txt_loader_multiple_files`](../api/functions/tests-unit-indexing-input-test-txt-loader-test-txt-loader-multiple-files)

