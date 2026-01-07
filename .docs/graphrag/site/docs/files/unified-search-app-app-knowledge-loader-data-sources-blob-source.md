---
sidebar_position: 283
---

# unified-search-app/app/knowledge_loader/data_sources/blob_source.py

## Overview

BlobDatasource for Azure Blob Storage-backed knowledge data used by the knowledge loader.

This module defines the BlobDatasource class which provides access to knowledge data stored in Azure Blob Storage, enabling reading Parquet tables and graphrag configurations used by the knowledge loader. It connects to a configured Azure Blob container using the provided database identifier to locate data and settings.

Key exports:
- BlobDatasource: Primary export providing access to blob storage for knowledge data and settings.

Brief summary:
- Supports reading parquet tables via read, loading graphrag settings via read_settings, and loading arbitrary blob content via load_blob_file and prompt configurations via load_blob_prompt_config.

Args:
- database: The database identifier used to access the blob storage.

Returns:
- BlobDatasource: An instance configured to access the specified blob container and its data/settings.

Raises:
- Exception: If authentication, network, or other Azure Blob Storage errors occur.

## Classes

- [`BlobDatasource`](../api/classes/unified-search-app-app-knowledge-loader-data-sources-blob-source-blobdatasource)

## Functions

- [`__init__`](../api/functions/unified-search-app-app-knowledge-loader-data-sources-blob-source-init)
- [`_get_container`](../api/functions/unified-search-app-app-knowledge-loader-data-sources-blob-source-get-container)
- [`load_blob_prompt_config`](../api/functions/unified-search-app-app-knowledge-loader-data-sources-blob-source-load-blob-prompt-config)
- [`load_blob_file`](../api/functions/unified-search-app-app-knowledge-loader-data-sources-blob-source-load-blob-file)
- [`read`](../api/functions/unified-search-app-app-knowledge-loader-data-sources-blob-source-read)
- [`read_settings`](../api/functions/unified-search-app-app-knowledge-loader-data-sources-blob-source-read-settings)

