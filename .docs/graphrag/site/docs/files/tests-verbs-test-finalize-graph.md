---
sidebar_position: 275
---

# tests/verbs/test_finalize_graph.py

## Overview

Tests for the finalize_graph workflow in GraphRag.

Purpose:
- Validate that the finalize_graph workflow produces final entities and relationships tables, with default coordinates, and that the UMAP-enabled variant produces x/y coordinates and the expected columns.

Key exports:
- _prep_tables: Prepare test tables for the finalize_graph workflow by loading test data into a test context, dropping final columns that wouldn't be present in inputs (x, y, degree from entities and combined_degree from relationships), and returning the initialized context.
- test_finalize_graph: Test that finalize_graph produces final entities and relationships tables with default coordinates.
- test_finalize_graph_umap: Test the finalize_graph workflow with UMAP enabled to verify x/y coordinates and expected final tables.

Overview:
This module uses create_graphrag_config to create a configuration, loads/saves tables via load_table_from_storage / write_table_to_storage, and runs the finalize_graph workflow via run_workflow. It asserts that the resulting tables have the expected structure and values. It relies on ENTITIES_FINAL_COLUMNS and RELATIONSHIPS_FINAL_COLUMNS to determine final column sets.

Args:
- _prep_tables: None
- test_finalize_graph: None
- test_finalize_graph_umap: None

Returns:
- _prep_tables: PipelineRunContext: The initialized pipeline run context with the test data loaded into its output storage.
- test_finalize_graph: None
- test_finalize_graph_umap: None

Raises:
- Exceptions raised by storage operations or workflow execution (load_table_from_storage, write_table_to_storage, run_workflow) during test setup and execution.

## Functions

- [`_prep_tables`](../api/functions/tests-verbs-test-finalize-graph-prep-tables)
- [`test_finalize_graph`](../api/functions/tests-verbs-test-finalize-graph-test-finalize-graph)
- [`test_finalize_graph_umap`](../api/functions/tests-verbs-test-finalize-graph-test-finalize-graph-umap)

