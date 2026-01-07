---
sidebar_position: 130
---

# InputFileType

**File:** `graphrag/config/enums.py`

## Overview

InputFileType is an enumeration of input file types used by the configuration.

This Enum defines string-valued members that identify various input sources. Each member maps to a string key defined elsewhere in the configuration.

Enum members:
    LanceDB
    AzureAISearch
    CosmosDB
    OpenAIEmbedding
    AzureOpenAIEmbedding
    Embedding
    OpenAIChat
    AzureOpenAIChat
    Chat
    MockChat
    MockEmbedding
    APIKey
    AzureManagedIdentity
    AsyncIO
    Threaded
    LOCAL
    GLOBAL
    DRIFT
    BASIC
    Standard
    Fast
    StandardUpdate
    FastUpdate
    RegexEnglish
    Syntactic
    CFG
    Graph
    LCC
    WeightedComponents

Usage:
  - Access a member directly: InputFileType.LanceDB
  - Construct by value: InputFileType(value)

Raises:
  ValueError: If value is not a valid member value.

## Methods

### `__repr__`

```python
def __repr__(self)
```

