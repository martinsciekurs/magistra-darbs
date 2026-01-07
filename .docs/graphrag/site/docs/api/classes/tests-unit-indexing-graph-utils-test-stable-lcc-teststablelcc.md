---
sidebar_position: 6
---

# TestStableLCC

**File:** `tests/unit/indexing/graph/utils/test_stable_lcc.py`

## Overview

TestStableLCC is a unit test suite for validating the stability and correctness of the stable_largest_connected_component function across both undirected and directed graphs.

Purpose:
- Verify determinism: ensure stable_largest_connected_component returns identical graphs on repeated runs, even when input edges are flipped.
- Preserve directed relationships: ensure that, for DiGraph inputs, the source and target directions are preserved in the resulting components.
- Validate consistency across graph types: cover both undirected and directed graphs.

Key helpers:
- _create_strongly_connected_graph(digraph=False): helper to construct a representative linear chain graph with node attributes; by default undirected Graph, DiGraph when digraph=True.
- _create_strongly_connected_graph_with_edges_flipped(digraph=False): helper to construct a five-node graph used for stability tests; flips edges scenario; supports Graph or DiGraph.

Tests provided:
- test_undirected_graph_run_twice_produces_same_graph
- test_directed_graph_keeps_source_target_intact
- test_directed_graph_run_twice_produces_same_graph

Note: This docstring focuses on high-level intent and test coverage; it omits implementation details.

## Methods

### `_create_strongly_connected_graph`

```python
def _create_strongly_connected_graph(self, digraph=False)
```

### `_create_strongly_connected_graph_with_edges_flipped`

```python
def _create_strongly_connected_graph_with_edges_flipped(self, digraph=False)
```

### `test_undirected_graph_run_twice_produces_same_graph`

```python
def test_undirected_graph_run_twice_produces_same_graph(self)
```

### `test_directed_graph_keeps_source_target_intact`

```python
def test_directed_graph_keeps_source_target_intact(self)
```

### `test_directed_graph_run_twice_produces_same_graph`

```python
def test_directed_graph_run_twice_produces_same_graph(self)
```

