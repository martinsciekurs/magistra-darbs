---
sidebar_position: 18
---

# graphrag/config/enums.py

## Overview

Graphrag configuration enums and string-backed identifiers.

Purpose: This module defines top-level string constants used as identifiers for configuration of backends, embeddings, chats, storage, and related features, along with Enum classes that map to these strings for type-safe usage across Graphrag's configuration and runtime logic.

Key exports:
- Constants affecting configuration: LanceDB, AzureAISearch, CosmosDB, OpenAIEmbedding, AzureOpenAIEmbedding, Embedding, OpenAIChat, AzureOpenAIChat, Chat, MockChat, MockEmbedding, APIKey, AzureManagedIdentity, AsyncIO, Threaded, LOCAL, GLOBAL, DRIFT, BASIC, Standard, Fast, StandardUpdate, FastUpdate, RegexEnglish, Syntactic, CFG, Graph, LCC, WeightedComponents
- Enums: ModelType, SearchMethod, ChunkStrategyType, InputFileType, CacheType, ReportingType, StorageType

What they represent: The constants are string identifiers used to configure storage backends, model and embedding types, chat interfaces, and miscellaneous options. The Enum classes provide string-based members that map to these identifiers to enable type checking and clearer usage in code.

## Classes

- [`ModelType`](../api/classes/graphrag-config-enums-modeltype)
- [`SearchMethod`](../api/classes/graphrag-config-enums-searchmethod)
- [`ChunkStrategyType`](../api/classes/graphrag-config-enums-chunkstrategytype)
- [`InputFileType`](../api/classes/graphrag-config-enums-inputfiletype)
- [`CacheType`](../api/classes/graphrag-config-enums-cachetype)
- [`ReportingType`](../api/classes/graphrag-config-enums-reportingtype)
- [`StorageType`](../api/classes/graphrag-config-enums-storagetype)

## Functions

- [`__repr__`](../api/functions/graphrag-config-enums-repr)
- [`__str__`](../api/functions/graphrag-config-enums-str)
- [`__repr__`](../api/functions/graphrag-config-enums-repr)
- [`__repr__`](../api/functions/graphrag-config-enums-repr)
- [`__repr__`](../api/functions/graphrag-config-enums-repr)
- [`__repr__`](../api/functions/graphrag-config-enums-repr)
- [`__repr__`](../api/functions/graphrag-config-enums-repr)

