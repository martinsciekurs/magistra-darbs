---
sidebar_position: 78
---

# graphrag/index/operations/layout_graph/typing.py

## Overview

Layout graph typing utilities.

Overview:
This module defines the core data container and type alias used to describe how
nodes are positioned and rendered in the layout graph. It provides a NodePosition
dataclass, a GraphLayout type alias, and a helper to_pandas method to serialize a
NodePosition into a pandas-friendly 5-tuple.

Exports:
- GraphLayout: type alias representing a list of NodePosition objects
- NodePosition: dataclass with fields label (str), x (float), y (float),
  cluster (int | str), size (float)
- NodePosition.to_pandas(self) -&gt; tuple[str, float, float, str, float]:
  Converts a NodePosition to a pandas-friendly 5-tuple. The cluster value is emitted
  as a string for pandas compatibility.

Public attributes and methods:
- NodePosition.label: Node's display label
- NodePosition.x: x-coordinate
- NodePosition.y: y-coordinate
- NodePosition.cluster: cluster identifier (int or str)
- NodePosition.size: node size

Notes:
- Requires Python 3.10+ for built-in union type in annotations (int | str).
- This module does not import pandas; to_pandas returns a 5-tuple suitable for DataFrame construction.

## Classes

- [`NodePosition`](../api/classes/graphrag-index-operations-layout-graph-typing-nodeposition)

## Functions

- [`to_pandas`](../api/functions/graphrag-index-operations-layout-graph-typing-to-pandas)

