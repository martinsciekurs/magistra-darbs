---
sidebar_position: 214
---

# graphrag/storage/blob_pipeline_storage.py

## Overview

Blob-based storage backend for GraphRag pipeline data using Azure Blob Storage.

Overview:
This module provides a BlobPipelineStorage class, a Azure Blob Storage backed implementation of the PipelineStorage interface used to cache pipeline results and data. It stores dataframe exports as JSON (records format) or Parquet, supports retrieving values, finding blobs by pattern, and basic cache management. Initialization selects the authentication flow based on provided credentials: a connection_string or a storage_account_blob_url with DefaultAzureCredential.

Public API:
- BlobPipelineStorage: Azure Blob Storage backed implementation of the PipelineStorage interface.

Usage examples:
- Instantiate with a connection string:
  storage = BlobPipelineStorage(connection_string=&lt;connection_string&gt;, container_name='my-container')
- Or instantiate with a storage account URL and DefaultAzureCredential:
  storage = BlobPipelineStorage(storage_account_blob_url=&lt;storage_account_blob_url&gt;, container_name='my-container')
- Store a dataframe export (JSON or Parquet) under a key:
  storage.set('exports/key1', dataframe)
- Retrieve a cached item:
  value = storage.get('exports/key1')
- Find blobs by pattern:
  for name, meta in storage.find(re.compile(r'.*')):
      pass
- Clear cache (no-op in this implementation):
  storage.clear()

Notes:
- Requires Azure SDKs: azure-storage-blob and azure-identity.
- The constructor raises ValueError if neither a connection_string nor a storage_account_blob_url is provided. During normal operation, Azure SDK exceptions may be raised for container creation, blob operations, or metadata access.

## Classes

- [`BlobPipelineStorage`](../api/classes/graphrag-storage-blob-pipeline-storage-blobpipelinestorage)

## Functions

- [`_abfs_url`](../api/functions/graphrag-storage-blob-pipeline-storage-abfs-url)
- [`keys`](../api/functions/graphrag-storage-blob-pipeline-storage-keys)
- [`_set_df_json`](../api/functions/graphrag-storage-blob-pipeline-storage-set-df-json)
- [`_set_df_parquet`](../api/functions/graphrag-storage-blob-pipeline-storage-set-df-parquet)
- [`find`](../api/functions/graphrag-storage-blob-pipeline-storage-find)
- [`clear`](../api/functions/graphrag-storage-blob-pipeline-storage-clear)
- [`get`](../api/functions/graphrag-storage-blob-pipeline-storage-get)
- [`_create_container`](../api/functions/graphrag-storage-blob-pipeline-storage-create-container)
- [`delete`](../api/functions/graphrag-storage-blob-pipeline-storage-delete)
- [`_container_exists`](../api/functions/graphrag-storage-blob-pipeline-storage-container-exists)
- [`set`](../api/functions/graphrag-storage-blob-pipeline-storage-set)
- [`_keyname`](../api/functions/graphrag-storage-blob-pipeline-storage-keyname)
- [`__init__`](../api/functions/graphrag-storage-blob-pipeline-storage-init)
- [`has`](../api/functions/graphrag-storage-blob-pipeline-storage-has)
- [`item_filter`](../api/functions/graphrag-storage-blob-pipeline-storage-item-filter)
- [`_delete_container`](../api/functions/graphrag-storage-blob-pipeline-storage-delete-container)
- [`validate_blob_container_name`](../api/functions/graphrag-storage-blob-pipeline-storage-validate-blob-container-name)
- [`child`](../api/functions/graphrag-storage-blob-pipeline-storage-child)
- [`_blobname`](../api/functions/graphrag-storage-blob-pipeline-storage-blobname)
- [`get_creation_date`](../api/functions/graphrag-storage-blob-pipeline-storage-get-creation-date)

