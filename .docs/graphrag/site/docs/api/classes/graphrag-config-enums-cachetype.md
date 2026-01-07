---
sidebar_position: 132
---

# CacheType

**File:** `graphrag/config/enums.py`

## Overview

"CacheType"  
Enumeration of cache backends used by graphrag configuration.

Purpose:
This Enum provides a typed collection of string-valued identifiers that correspond to the top-level configuration constants defined in graphrag.config. Each member's value is the backend identifier string used in configuration. The constants include LanceDB, AzureAISearch, CosmosDB, OpenAIEmbedding, AzureOpenAIEmbedding, Embedding, OpenAIChat, AzureOpenAIChat, Chat, MockChat, MockEmbedding, APIKey, AzureManagedIdentity, AsyncIO, Threaded, LOCAL, GLOBAL, DRIFT, BASIC, Standard, Fast, StandardUpdate, FastUpdate, RegexEnglish, Syntactic, CFG, Graph, LCC, WeightedComponents. The actual code uses AzureAISearch as the constant name (not the spaced human-friendly form).

Attributes:
- Each member has a string value that corresponds to the backend identifier used in configuration. Examples:
  "lancedb" (LanceDB), "azure_ai_search" (AzureAISearch), "cosmosdb" (CosmosDB), "openai_embedding" (OpenAIEmbedding), "azure_openai_embedding" (AzureOpenAIEmbedding), "embedding" (Embedding), "openai_chat" (OpenAIChat), "azure_openai_chat" (AzureOpenAIChat), "chat" (Chat), "mock_chat" (MockChat), "mock_embedding" (MockEmbedding), "api_key" (APIKey), "azure_managed_identity" (AzureManagedIdentity), "asyncio" (AsyncIO), "threaded" (Threaded), "local" (LOCAL), "global" (GLOBAL), "drift" (DRIFT), "basic" (BASIC), "standard" (Standard), "fast" (Fast), "standard-update" (StandardUpdate), "fast-update" (FastUpdate), "regex_english" (RegexEnglish), "syntactic_parser" (Syntactic), "cfg" (CFG), "graph" (Graph), "lcc" (LCC), "weighted_components" (WeightedComponents).

Representation:
- __repr__(self) -&gt; str: Returns a string representation of the enumeration member. Following standard Enum semantics, this typically includes the member name and its value.

## Methods

### `__repr__`

```python
def __repr__(self)
```

