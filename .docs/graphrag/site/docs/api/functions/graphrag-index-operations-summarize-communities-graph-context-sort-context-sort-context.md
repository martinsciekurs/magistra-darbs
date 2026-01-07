---
sidebar_position: 145
---

# sort_context

**File:** `graphrag/index/operations/summarize_communities/graph_context/sort_context.py` (lines 11-126)

## Signature

```python
def sort_context(
    local_context: list[dict],
    tokenizer: Tokenizer,
    sub_community_reports: list[dict] | None = None,
    max_context_tokens: int | None = None,
    node_name_column: str = schemas.TITLE,
    node_details_column: str = schemas.NODE_DETAILS,
    edge_id_column: str = schemas.SHORT_ID,
    edge_details_column: str = schemas.EDGE_DETAILS,
    edge_degree_column: str = schemas.EDGE_DEGREE,
    edge_source_column: str = schemas.EDGE_SOURCE,
    edge_target_column: str = schemas.EDGE_TARGET,
    claim_details_column: str = schemas.CLAIM_DETAILS,
) -> str
```

## Description

Sorts context by degree in descending order, optimizing for performance.

Args:
    local_context: list[dict]. Local context data; each entry may contain edge details under edge_details_column and associated node and claim information as defined by the surrounding schema.
    tokenizer: Tokenizer. Tokenizer used to count tokens for max_context_tokens to enforce length constraints.
    sub_community_reports: list[dict] | None. Optional list of sub-community reports to include at the top of the context.
    max_context_tokens: int | None. Optional maximum number of tokens for the produced context; if exceeded, the context is truncated accordingly.
    node_name_column: str. Column name used to identify a node's display name.
    node_details_column: str. Column name for the node's details payload.
    edge_id_column: str. Column name for the edge identifier.
    edge_details_column: str. Column name for the edge details payload.
    edge_degree_column: str. Column name for the edge degree measure.
    edge_source_column: str. Column name for the edge source node.
    edge_target_column: str. Column name for the edge target node.
    claim_details_column: str. Column name for the claim details associated with nodes.

Returns:
    str. The consolidated context string built from Entities, Claims, and Relationships, optionally prefixed with sub-community reports, truncated to max_context_tokens if specified.

Raises:
    None

## Dependencies

This function calls:

- `graphrag/index/operations/summarize_communities/graph_context/sort_context.py::_get_context_string`

## Called By

This function is called by:

- `graphrag/index/operations/summarize_communities/build_mixed_context.py::build_mixed_context`
- `graphrag/index/operations/summarize_communities/graph_context/context_builder.py::_sort_and_trim_context`
- `graphrag/index/operations/summarize_communities/graph_context/sort_context.py::parallel_sort_context_batch`
- `tests/unit/indexing/graph/extractors/community_reports/test_sort_context.py::test_sort_context`
- `tests/unit/indexing/graph/extractors/community_reports/test_sort_context.py::test_sort_context_max_tokens`

