---
sidebar_position: 89
---

# load_strategy

**File:** `graphrag/index/operations/embed_text/embed_text.py` (lines 229-246)

## Signature

```python
def load_strategy(strategy: TextEmbedStrategyType) -> TextEmbeddingStrategy
```

## Description

Load the embedding strategy callable for the given strategy type.

Args:
    strategy: TextEmbedStrategyType - The strategy type used to determine which embedding strategy to load.

Returns:
    TextEmbeddingStrategy: The loaded strategy callable corresponding to the provided strategy.

Raises:
    ValueError: If an unknown strategy is provided.

## Called By

This function is called by:

- `graphrag/index/operations/embed_text/embed_text.py::_text_embed_in_memory`
- `graphrag/index/operations/embed_text/embed_text.py::_text_embed_with_vector_store`

