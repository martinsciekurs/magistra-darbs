---
sidebar_position: 149
---

# load_strategy

**File:** `graphrag/index/operations/summarize_communities/summarize_communities.py` (lines 117-130)

## Signature

```python
def load_strategy(
    strategy: CreateCommunityReportsStrategyType,
) -> CommunityReportsStrategy
```

## Description

Load the strategy method for community reports based on the provided type.

Args:
    strategy (CreateCommunityReportsStrategyType): The strategy type used to determine which community reports strategy to load.

Returns:
    CommunityReportsStrategy: The callable strategy function corresponding to the supplied strategy type.

Raises:
    ValueError: If an unknown strategy type is provided.

## Called By

This function is called by:

- `graphrag/index/operations/summarize_communities/summarize_communities.py::summarize_communities`

