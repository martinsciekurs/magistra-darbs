---
sidebar_position: 83
---

# CreateCommunityReportsStrategyType

**File:** `graphrag/index/operations/summarize_communities/typing.py`

## Overview

Enum describing the strategies for creating community reports in the summarize_communities operation.

Description:
CreateCommunityReportsStrategyType is an enumeration of the available strategies used to create community reports in the summarize_communities workflow. Each member represents a concrete strategy and exposes its identity via the member's name and its associated representation via the member's value. The exact type of member.value is defined by the enum's members and may be a string, a callable, or another object that encodes the strategy.

Notes:
- Access member.name for the programmer-friendly identifier and member.value for the underlying representation.
- This docstring follows Python Enum semantics: unless overridden, __repr__ and __str__ reflect Enum behavior, and the value attached to each member is whatever was assigned.
- If you need a human-facing description of a member, consider maintaining a separate mapping or documentation since Enum members themselves typically only provide name and value.

Examples:
- Access attributes of a member: strategy.name and strategy.value
- Iterate over all members: for s in CreateCommunityReportsStrategyType: ...

## Methods

### `__repr__`

```python
def __repr__(self)
```

