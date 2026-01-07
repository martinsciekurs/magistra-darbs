---
sidebar_position: 109
---

# _load_strategy

**File:** `graphrag/index/operations/extract_graph/extract_graph.py` (lines 85-97)

## Signature

```python
def _load_strategy(strategy_type: ExtractEntityStrategyType) -> EntityExtractStrategy
```

## Description

Load the strategy method implementation for the given strategy type.

Args:
    strategy_type (ExtractEntityStrategyType): The type of extraction strategy to load.

Returns:
    EntityExtractStrategy: The loaded strategy callable.

Raises:
    ValueError: If an unknown strategy_type is provided.

## Called By

This function is called by:

- `graphrag/index/operations/extract_graph/extract_graph.py::extract_graph`

