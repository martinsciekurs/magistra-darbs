---
sidebar_position: 250
---

# generate_text_embeddings

**File:** `graphrag/index/workflows/generate_text_embeddings.py` (lines 96-171)

## Signature

```python
def generate_text_embeddings(
    documents: pd.DataFrame | None,
    relationships: pd.DataFrame | None,
    text_units: pd.DataFrame | None,
    entities: pd.DataFrame | None,
    community_reports: pd.DataFrame | None,
    callbacks: WorkflowCallbacks,
    cache: PipelineCache,
    text_embed_config: dict,
    embedded_fields: list[str],
) -> dict[str, pd.DataFrame]
```

## Description

All the steps to generate all embeddings.

Args:
  documents: DataFrame or None. Data for document text embeddings; when provided, expected to include id and text columns.
  relationships: DataFrame or None. Data for relationship descriptions; when provided, expected to include id and description columns.
  text_units: DataFrame or None. Data for text units; when provided, expected to include id and text columns.
  entities: DataFrame or None. Data for entities; may include id, title, and description used for embeddings.
  community_reports: DataFrame or None. Data for community reports; used for title, summary, and full content embeddings if provided.
  callbacks: WorkflowCallbacks. Callbacks used during embedding processing.
  cache: PipelineCache. Cache used by the embedding routine.
  text_embed_config: dict. Embedding configuration (e.g., strategy) passed to the embedding function.
  embedded_fields: list[str]. The list of embedding fields to generate; each corresponds to a key in the embedding_param_map.

Returns:
  dict[str, pd.DataFrame]. Mapping from embedding name to a DataFrame containing columns ["id", "embedding"] for that embedding.

Raises:
  Exceptions raised by the underlying embedding operations (e.g., _run_embeddings or embed_text) may propagate to the caller if embedding fails.

## Dependencies

This function calls:

- `graphrag/index/workflows/generate_text_embeddings.py::_run_embeddings`

## Called By

This function is called by:

- `graphrag/index/workflows/generate_text_embeddings.py::run_workflow`
- `graphrag/index/workflows/update_text_embeddings.py::run_workflow`

