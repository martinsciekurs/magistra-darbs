---
sidebar_position: 133
---

# ReportingType

**File:** `graphrag/config/enums.py`

## Overview

ReportingType is an enumeration of the available reporting configurations used by the graphrag configuration system.

Summary:
Provides a type-safe collection of reporter configuration options, each with a string value that can be consumed by the codebase or serialized.

Attributes:
    value: The string value associated with the enumeration member.

Methods:
    __repr__(self):
        Return a string representation of the enumeration member. The current implementation returns the member's value wrapped in double quotes (e.g., '"standard"'), which is convenient for certain serialization scenarios but differs from Python's standard Enum representation. For conventional display, consider implementing __str__ or using the .value attribute.

Examples:
    from graphrag.config.enums import ReportingType
    t = ReportingType.Standard
    s = t.value           # "standard"
    r = repr(t)           # '"standard"' (based on current __repr__)

## Methods

### `__repr__`

```python
def __repr__(self)
```

