---
sidebar_position: 578
---

# test_generate_text_embeddings

**File:** `tests/verbs/test_generate_text_embeddings.py` (lines 21-68)

## Signature

```python
def test_generate_text_embeddings()
```

## Description

Test the generate_text_embeddings workflow using a mock embedding model and validate produced embeddings.

This test creates a test context with several storage tables, configures the graphrag embedding to use a mock embedding model,
runs the generate_text_embeddings workflow, and asserts that:
- For every embedding field, a parquet named embeddings.&#123;field&#125;.parquet exists in the output storage
- embeddings.entity.description has exactly two columns: id and embedding
- embeddings.document.text has exactly two columns: id and embedding

The test relies on utilities: create_test_context, create_graphrag_config, run_workflow, and load_table_from_storage.

Args:
    None

Returns:
    None

Raises:
    Exception: Exceptions raised by underlying test utilities or storage operations may propagate.

## Dependencies

This function calls:

- `graphrag/config/create_graphrag_config.py::create_graphrag_config`
- `graphrag/index/workflows/generate_text_embeddings.py::run_workflow`
- `graphrag/utils/storage.py::load_table_from_storage`
- `tests/verbs/util.py::create_test_context`

