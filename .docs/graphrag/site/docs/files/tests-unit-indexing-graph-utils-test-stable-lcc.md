---
sidebar_position: 250
---

# tests/unit/indexing/graph/utils/test_stable_lcc.py

## Overview

Unit tests for the stable_largest_connected_component function used in indexing graphs.

This module defines a TestStableLCC test suite that validates the stability and correctness of stable_largest_connected_component across both undirected graphs and directed graphs. It aims to:
- Verify determinism: stable_largest_connected_component returns identical graphs on repeated runs, even if input edges are flipped.
- Preserve directed relationships: for DiGraph inputs, the source and target of edges are preserved.

Key exports:
- stable_largest_connected_component (imported from graphrag.index.utils.stable_lcc)
- TestStableLCC class with tests:
  - test_undirected_graph_run_twice_produces_same_graph
  - test_directed_graph_keeps_source_target_intact
  - test_directed_graph_run_twice_produces_same_graph
- Helper methods:
  - _create_strongly_connected_graph(self, digraph=False)
  - _create_strongly_connected_graph_with_edges_flipped(self, digraph=False)

Brief summary: The module ensures that the stable largest connected component computation is deterministic and preserves edge directions for directed graphs, using specific test graphs.

Raises: AssertionError if the graphs produced by stable_largest_connected_component differ between runs or if input/output edges in directed graphs are not preserved.

## Classes

- [`TestStableLCC`](../api/classes/tests-unit-indexing-graph-utils-test-stable-lcc-teststablelcc)

## Functions

- [`_create_strongly_connected_graph`](../api/functions/tests-unit-indexing-graph-utils-test-stable-lcc-create-strongly-connected-graph)
- [`_create_strongly_connected_graph_with_edges_flipped`](../api/functions/tests-unit-indexing-graph-utils-test-stable-lcc-create-strongly-connected-graph-with-edges-flipped)
- [`test_undirected_graph_run_twice_produces_same_graph`](../api/functions/tests-unit-indexing-graph-utils-test-stable-lcc-test-undirected-graph-run-twice-produces-same-graph)
- [`test_directed_graph_keeps_source_target_intact`](../api/functions/tests-unit-indexing-graph-utils-test-stable-lcc-test-directed-graph-keeps-source-target-intact)
- [`test_directed_graph_run_twice_produces_same_graph`](../api/functions/tests-unit-indexing-graph-utils-test-stable-lcc-test-directed-graph-run-twice-produces-same-graph)

