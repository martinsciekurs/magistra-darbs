---
sidebar_position: 215
---

# graphrag/storage/cosmosdb_pipeline_storage.py

## Overview

Cosmos DB-backed storage backend for Graphrag.

This module provides the CosmosDBPipelineStorage class, a storage backend that stores and retrieves data in an Azure Cosmos DB container. It implements Graphrag's storage interface to manage databases, containers, and items, including creation/deletion of databases and containers, insertion of file contents, retrieval, and query-based operations. It maintains an internal reference to the active container.

Public exports:
- CosmosDBPipelineStorage: Cosmos DB backed storage implementation used by Graphrag.

## Classes

- [`CosmosDBPipelineStorage`](../api/classes/graphrag-storage-cosmosdb-pipeline-storage-cosmosdbpipelinestorage)

## Functions

- [`_delete_database`](../api/functions/graphrag-storage-cosmosdb-pipeline-storage-delete-database)
- [`__init__`](../api/functions/graphrag-storage-cosmosdb-pipeline-storage-init)
- [`clear`](../api/functions/graphrag-storage-cosmosdb-pipeline-storage-clear)
- [`keys`](../api/functions/graphrag-storage-cosmosdb-pipeline-storage-keys)
- [`_delete_container`](../api/functions/graphrag-storage-cosmosdb-pipeline-storage-delete-container)
- [`child`](../api/functions/graphrag-storage-cosmosdb-pipeline-storage-child)
- [`_create_container`](../api/functions/graphrag-storage-cosmosdb-pipeline-storage-create-container)
- [`set`](../api/functions/graphrag-storage-cosmosdb-pipeline-storage-set)
- [`_create_database`](../api/functions/graphrag-storage-cosmosdb-pipeline-storage-create-database)
- [`_create_progress_status`](../api/functions/graphrag-storage-cosmosdb-pipeline-storage-create-progress-status)
- [`delete`](../api/functions/graphrag-storage-cosmosdb-pipeline-storage-delete)
- [`get`](../api/functions/graphrag-storage-cosmosdb-pipeline-storage-get)
- [`item_filter`](../api/functions/graphrag-storage-cosmosdb-pipeline-storage-item-filter)
- [`_get_prefix`](../api/functions/graphrag-storage-cosmosdb-pipeline-storage-get-prefix)
- [`has`](../api/functions/graphrag-storage-cosmosdb-pipeline-storage-has)
- [`find`](../api/functions/graphrag-storage-cosmosdb-pipeline-storage-find)
- [`get_creation_date`](../api/functions/graphrag-storage-cosmosdb-pipeline-storage-get-creation-date)

