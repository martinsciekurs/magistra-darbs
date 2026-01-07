---
sidebar_position: 75
---

# graphrag/index/operations/finalize_relationships.py

## Overview

Module for finalizing relationship records by constructing a graph from raw relationships and computing derived metrics to produce finalized records.

Purpose
Expose finalize_relationships, which orchestrates graph construction, degree computations, edge deduplication, and identifier assignment to output a DataFrame conforming to the final relationships schema.

Key exports
- finalize_relationships(relationships): Transforms input relationships DataFrame into finalized relationship records. It builds a graph from the input relationships, computes node degrees, deduplicates edges, computes a combined degree for each edge, assigns stable human-readable and UUID-based identifiers, and returns a DataFrame containing the expected final columns (RELATIONSHIPS_FINAL_COLUMNS).

Overview
The function relies on compute_degree, compute_edge_combined_degree, create_graph, and the RELATIONSHIPS_FINAL_COLUMNS schema to produce a DataFrame with the final set of columns. The output is suitable for downstream processing and storage.

Args
relationships: DataFrame containing edge information for the graph.

Returns
DataFrame containing finalized relationship records with the final columns defined by RELATIONSHIPS_FINAL_COLUMNS.

Raises
Exceptions may be raised by the underlying operations (graph construction, degree computations, edge deduplication, and identifier assignment) or by pandas DataFrame operations; specific exception types are not asserted here.

## Functions

- [`finalize_relationships`](../api/functions/graphrag-index-operations-finalize-relationships-finalize-relationships)

