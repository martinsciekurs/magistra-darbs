---
sidebar_position: 246
---

# tests/smoke/test_fixtures.py

## Overview

Smoke-test utilities for fixtures that validate the indexer and its queries against predefined configurations using Azurite blob storage.

This module provides helpers to load fixture configurations, prepare Azurite data, run the indexer, generate parameterized tests, run queries, and verify indexer outputs against workflow configurations. It exposes the TestIndexer class, which coordinates setup, execution, and validation of smoke-test fixtures, and its public test_fixture method. Internal utilities handle test data loading, Azurite preparation, test cleanup, and test-automation orchestration. The module relies on KNOWN_WARNINGS (including NO_COMMUNITY_RECORDS_WARNING) to filter noise during test runs.

## Classes

- [`TestIndexer`](../api/classes/tests-smoke-test-fixtures-testindexer)

## Functions

- [`__assert_indexer_outputs`](../api/functions/tests-smoke-test-fixtures-assert-indexer-outputs)
- [`__run_indexer`](../api/functions/tests-smoke-test-fixtures-run-indexer)
- [`cleanup`](../api/functions/tests-smoke-test-fixtures-cleanup)
- [`prepare_azurite_data`](../api/functions/tests-smoke-test-fixtures-prepare-azurite-data)
- [`_load_fixtures`](../api/functions/tests-smoke-test-fixtures-load-fixtures)
- [`pytest_generate_tests`](../api/functions/tests-smoke-test-fixtures-pytest-generate-tests)
- [`__run_query`](../api/functions/tests-smoke-test-fixtures-run-query)
- [`wrapper`](../api/functions/tests-smoke-test-fixtures-wrapper)
- [`decorator`](../api/functions/tests-smoke-test-fixtures-decorator)
- [`test_fixture`](../api/functions/tests-smoke-test-fixtures-test-fixture)

