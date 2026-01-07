---
sidebar_position: 111
---

# DocSelectionType

**File:** `graphrag/prompt_tune/types.py`

## Overview

DocSelectionType is an enumeration of strategies for selecting documents in the prompt tuning workflow.

It defines four strategies, each associated with a string value:
- ALL -&gt; "all"
- RANDOM -&gt; "random"
- TOP -&gt; "top"
- AUTO -&gt; "auto"

Attributes:
    ALL (str): The "all" selection strategy.
    RANDOM (str): The "random" selection strategy.
    TOP (str): The "top" selection strategy.
    AUTO (str): The "auto" selection strategy.

Methods:
    __str__(self) -&gt; str:
        Returns: str
            The string representation of the enum value.

## Methods

### `__str__`

```python
def __str__(self)
```

