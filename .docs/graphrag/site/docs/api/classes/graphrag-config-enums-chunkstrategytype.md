---
sidebar_position: 113
---

# ChunkStrategyType

**File:** `graphrag/config/enums.py`

## Overview

ChunkStrategyType is an Enum subclass that defines the available chunking strategies used by Graphrag configuration.

This enum maps each strategy to a string value that appears in configuration and is intended to be used to configure chunking behavior.

Enum members:
- BASIC: basic
- Standard: standard
- Fast: fast
- StandardUpdate: standard-update
- FastUpdate: fast-update

Accessing values:
The literal string for a member is accessible via the value attribute. For example, ChunkStrategyType.BASIC.value yields basic.

Inheritance:
This class inherits from Enum; members are enumeration members rather than plain strings.

Usage notes:
Do not rely on the string representations of the members; use .value to obtain the underlying string used in configuration.

## Methods

### `__repr__`

```python
def __repr__(self)
```

