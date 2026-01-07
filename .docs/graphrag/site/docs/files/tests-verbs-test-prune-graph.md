---
sidebar_position: 278
---

# tests/verbs/test_prune_graph.py

## Overview

Tests for the prune_graph workflow in graphrag.

Purpose:
This module contains unit tests validating the prune_graph workflow, ensuring the graph pruning operation behaves as expected in the graphrag project.

Key exports:
- test_prune_graph: Unit test that asserts pruning the graph results in 20 entities.

Brief summary:
The tests exercise the prune_graph workflow by invoking run_workflow with a Graphrag config and storage interactions, verifying the final entity count.

Args:
  None: This module's tests do not accept any parameters.

Returns:
  None: Tests do not return a value.

Raises:
  Exception: Exceptions may propagate from the underlying operations used in the test (e.g., test utilities, storage I/O, or workflow execution).

## Functions

- [`test_prune_graph`](../api/functions/tests-verbs-test-prune-graph-test-prune-graph)

