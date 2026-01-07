---
sidebar_position: 105
---

# ExtractEntityStrategyType

**File:** `graphrag/index/operations/extract_graph/typing.py`

## Overview

ExtractEntityStrategyType is an Enum subclass that defines the available strategies for extracting entities in the graphrag index's extraction workflow.

Purpose:
This enumeration provides a type-safe way to refer to a specific extraction strategy. Each member represents one strategy and has an associated value defined by the enum. The class itself does not implement behavior; it serves as a collection of named constants used by the extraction logic.

Members:
The enum's members are defined in the source file. Each member has a unique name and value. The exact set of members may evolve as features are added, but all members share the Enum semantics.

Usage:
- You can enumerate or inspect the defined members at runtime via ExtractEntityStrategyType.__members__.keys().
- To use a strategy, reference a concrete member in your code (for example, strategy == ExtractEntityStrategyType.SOME_MEMBER). Replace SOME_MEMBER with the actual member defined in your project.

Notes:
- __repr__ and __str__ representations follow standard Python Enum behavior unless overridden in the enum definition.
- This docstring intentionally avoids asserting specific values or representations, since those depend on the actual member definitions in the codebase.

## Methods

### `__repr__`

```python
def __repr__(self)
```

