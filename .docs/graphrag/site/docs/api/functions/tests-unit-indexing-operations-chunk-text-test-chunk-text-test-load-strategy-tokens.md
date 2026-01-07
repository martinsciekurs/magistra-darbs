---
sidebar_position: 519
---

# test_load_strategy_tokens

**File:** `tests/unit/indexing/operations/chunk_text/test_chunk_text.py` (lines 37-42)

## Signature

```python
def test_load_strategy_tokens()
```

## Description

Load the strategy callable for the given ChunkStrategyType.

Args:
    strategy (ChunkStrategyType): The type of chunk strategy to load. If ChunkStrategyType.tokens, the tokens strategy is returned. If ChunkStrategyType.sentence, NLP resources are bootstrapped and the sentences strategy is returned.

Returns:
    ChunkStrategy: The loaded strategy callable corresponding to the provided strategy type.

Raises:
    ValueError: If an unknown strategy is provided.

## Dependencies

This function calls:

- `graphrag/index/operations/chunk_text/chunk_text.py::load_strategy`

