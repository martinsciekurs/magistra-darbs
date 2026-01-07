---
sidebar_position: 42
---

# get_embedding_settings

**File:** `graphrag/config/get_embedding_settings.py` (lines 9-38)

## Signature

```python
def get_embedding_settings(
    settings: GraphRagConfig,
    vector_store_params: dict | None = None,
) -> dict
```

## Description

Transform GraphRAG config into settings for workflows.

Args:
    settings: GraphRagConfig
        GraphRagConfig containing embed_text and vector_store configuration.
    vector_store_params: dict | None
        Optional dictionary of vector store parameters to override defaults.

Returns:
    dict
        A dictionary with a single key "strategy" containing the embedding strategy
        configured using language model settings and merged vector store settings
        from both the config and any provided vector_store_params.

Raises:
    Exceptions propagated from GraphRagConfig methods or underlying calls may occur.

## Called By

This function is called by:

- `graphrag/index/workflows/generate_text_embeddings.py::run_workflow`
- `graphrag/index/workflows/update_text_embeddings.py::run_workflow`

