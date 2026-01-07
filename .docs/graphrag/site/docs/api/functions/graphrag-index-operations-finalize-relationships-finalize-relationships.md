---
sidebar_position: 120
---

# finalize_relationships

**File:** `graphrag/index/operations/finalize_relationships.py` (lines 18-44)

## Signature

```python
def finalize_relationships(
    relationships: pd.DataFrame,
) -> pd.DataFrame
```

## Description

Transform input relationships into finalized relationship records.

This function builds a graph from the input relationships, computes node degrees,
deduplicates edges, computes a combined degree for each edge, assigns stable
human-readable and UUID-based identifiers, and returns a DataFrame containing
the expected final columns.

Args:
    relationships: DataFrame containing edge information for relationships to finalize.

Returns:
    A DataFrame containing the finalized relationships, including the columns
    defined in RELATIONSHIPS_FINAL_COLUMNS, as well as additional columns:
    - human_readable_id: the index value assigned prior to UUID generation
    - id: a string UUID for each row
    - combined_degree: the computed combined degree per edge

Raises:
    Propagates exceptions from underlying operations such as graph creation,
    degree computation, edge degree computation, and DataFrame manipulation.

## Dependencies

This function calls:

- `graphrag/index/operations/compute_degree.py::compute_degree`
- `graphrag/index/operations/compute_edge_combined_degree.py::compute_edge_combined_degree`
- `graphrag/index/operations/create_graph.py::create_graph`

## Called By

This function is called by:

- `graphrag/index/workflows/finalize_graph.py::finalize_graph`

