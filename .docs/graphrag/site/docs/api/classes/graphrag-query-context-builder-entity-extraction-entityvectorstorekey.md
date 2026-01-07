---
sidebar_position: 73
---

# EntityVectorStoreKey

**File:** `graphrag/query/context_builder/entity_extraction.py`

## Overview

Enum that defines the keys used to locate and identify Entity vectors in a vector store.

Purpose:
    Provides the valid keys for identifying an Entity vector, typically by id or by title.

Attributes:
    ID: The enum member representing the string key "id".
    TITLE: The enum member representing the string key "title".

Methods:
    from_string(value: str) -&gt; EntityVectorStoreKey:
        Convert a string key to the corresponding EntityVectorStoreKey enum member.
        Returns: The corresponding enum member (EntityVectorStoreKey.ID for "id",
                 EntityVectorStoreKey.TITLE for "title").
        Raises: ValueError if value is not a valid key ("id" or "title").

## Methods

### `from_string`

```python
def from_string(value: str) -> "EntityVectorStoreKey"
```

