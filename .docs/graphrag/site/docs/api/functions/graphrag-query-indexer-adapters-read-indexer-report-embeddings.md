---
sidebar_position: 345
---

# read_indexer_report_embeddings

**File:** `graphrag/query/indexer_adapters.py` (lines 130-136)

## Signature

```python
def read_indexer_report_embeddings(
    community_reports: list[CommunityReport],
    embeddings_store: BaseVectorStore,
)
```

## Description

Read in the Community Reports from the raw indexing outputs.

Args:
  community_reports: list[CommunityReport] - The community reports to enrich with embeddings.
  embeddings_store: BaseVectorStore - The vector store used to fetch embeddings by report id.

Returns:
  None - This function mutates the input CommunityReport objects by setting their full_content_embedding.

## Called By

This function is called by:

- `graphrag/api/query.py::drift_search_streaming`

