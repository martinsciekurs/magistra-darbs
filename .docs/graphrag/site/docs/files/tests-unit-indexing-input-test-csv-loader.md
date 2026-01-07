---
sidebar_position: 251
---

# tests/unit/indexing/input/test_csv_loader.py

## Overview

Unit tests for the CSV loading functionality of the indexing input loader.

This module contains unit tests that exercise loading CSV data via the input
loader, using the Graphrag config models and storage helpers. It covers both
single and multiple CSV files, with and without a title column and with metadata
verification. The tests validate the resulting DataFrame shapes and key content,
such as the value in the title column.

Key exports:
- test_csv_loader_one_file: Tests loading a single CSV file and asserts the DataFrame
  shape and the first title entry.
- test_csv_loader_one_file_with_title: Tests loading a single CSV with a title column
  and asserts the DataFrame shape and the first title entry.
- test_csv_loader_one_file_with_metadata: Tests loading a CSV with metadata and validates
  DataFrame and metadata content.
- test_csv_loader_multiple_files: Tests loading multiple CSV files and asserts the DataFrame
  shape.

## Functions

- [`test_csv_loader_one_file`](../api/functions/tests-unit-indexing-input-test-csv-loader-test-csv-loader-one-file)
- [`test_csv_loader_one_file_with_title`](../api/functions/tests-unit-indexing-input-test-csv-loader-test-csv-loader-one-file-with-title)
- [`test_csv_loader_one_file_with_metadata`](../api/functions/tests-unit-indexing-input-test-csv-loader-test-csv-loader-one-file-with-metadata)
- [`test_csv_loader_multiple_files`](../api/functions/tests-unit-indexing-input-test-csv-loader-test-csv-loader-multiple-files)

