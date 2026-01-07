---
sidebar_position: 26
---

# ModelType

**File:** `graphrag/config/enums.py`

## Overview

ModelType is an enumeration of string-based model type identifiers used in graphrag's configuration.

Purpose:
Provide a centralized, type-safe collection of ModelType Members that map to backend and component identifiers such as lancedb, azure_ai_search, cosmosdb, embedding, chat, and related utilities. This helps ensure consistency across configuration and usage wherever model types are referenced.

Enum Members:
- LanceDB: "lancedb"
- AzureAISearch: "azure_ai_search"
- CosmosDB: "cosmosdb"
- OpenAIEmbedding: "openai_embedding"
- AzureOpenAIEmbedding: "azure_openai_embedding"
- Embedding: "embedding"
- OpenAIChat: "openai_chat"
- AzureOpenAIChat: "azure_openai_chat"
- Chat: "chat"
- MockChat: "mock_chat"
- MockEmbedding: "mock_embedding"
- APIKey: "api_key"
- AzureManagedIdentity: "azure_managed_identity"
- AsyncIO: "asyncio"
- Threaded: "threaded"
- LOCAL: "local"
- GLOBAL: "global"
- DRIFT: "drift"
- BASIC: "basic"
- Standard: "standard"
- Fast: "fast"
- StandardUpdate: "standard-update"
- FastUpdate: "fast-update"
- RegexEnglish: "regex_english"
- Syntactic: "syntactic_parser"
- CFG: "cfg"
- Graph: "graph"
- LCC: "lcc"
- WeightedComponents: "weighted_components"

Args:
None: This Enum does not require constructor arguments.

Returns:
There is no return value for a class. To obtain the underlying string, use member.value.

Raises:
None

Notes:
- Access the string value via member.value; the member object itself is an Enum member.
- __repr__ and __str__ representations of Enum members are not guaranteed; do not rely on a specific format.

## Methods

### `__repr__`

```python
def __repr__(self)
```

