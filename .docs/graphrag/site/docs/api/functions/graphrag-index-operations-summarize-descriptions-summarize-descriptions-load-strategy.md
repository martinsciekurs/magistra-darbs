---
sidebar_position: 161
---

# load_strategy

**File:** `graphrag/index/operations/summarize_descriptions/summarize_descriptions.py` (lines 111-122)

## Signature

```python
def load_strategy(strategy_type: SummarizeStrategyType) -> SummarizationStrategy
```

## Description

Load the summarization strategy callable for the given strategy_type.

Args:
    strategy_type (SummarizeStrategyType): The strategy type used to determine which summarization strategy to load.

Returns:
    SummarizationStrategy: The loaded strategy callable corresponding to the provided strategy_type.

Raises:
    ValueError: If an unknown strategy_type is provided.

## Called By

This function is called by:

- `graphrag/index/operations/summarize_descriptions/summarize_descriptions.py::summarize_descriptions`

