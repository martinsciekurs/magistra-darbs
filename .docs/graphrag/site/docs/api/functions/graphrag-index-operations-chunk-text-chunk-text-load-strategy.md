---
sidebar_position: 73
---

# load_strategy

**File:** `graphrag/index/operations/chunk_text/chunk_text.py` (lines 114-130)

## Signature

```python
def load_strategy(strategy: ChunkStrategyType) -> ChunkStrategy
```

## Description

Load the strategy method for the given chunking strategy.

Args:
    strategy (ChunkStrategyType): The type of chunk strategy to load. If ChunkStrategyType.tokens, the tokens strategy is returned. If ChunkStrategyType.sentence, NLP resources are bootstrapped and the sentences strategy is returned.

Returns:
    ChunkStrategy: The loaded strategy callable corresponding to the provided strategy type.

Raises:
    ValueError: If an unknown strategy is provided.

## Dependencies

This function calls:

- `graphrag/index/operations/chunk_text/bootstrap.py::bootstrap`

## Called By

This function is called by:

- `graphrag/index/operations/chunk_text/chunk_text.py::chunk_text`
- `tests/unit/indexing/operations/chunk_text/test_chunk_text.py::test_load_strategy_tokens`
- `tests/unit/indexing/operations/chunk_text/test_chunk_text.py::test_load_strategy_sentence`
- `tests/unit/indexing/operations/chunk_text/test_chunk_text.py::test_load_strategy_none`

