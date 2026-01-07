---
sidebar_position: 285
---

# unified-search-app/app/knowledge_loader/data_sources/local_source.py

## Overview

Local data source loader for knowledge_loader that reads local Parquet data and loads Graph Rag configurations.

Purpose
- This module provides utilities for accessing Parquet data stored on the local filesystem and for loading Graph Rag configuration from a base path that serves as the root for the local data source.

Key exports
- load_local_prompt_config(base_path: str) -&gt; dict[str, str]
  Load local prompt configuration by reading prompt files from base_path and returning a mapping from prompt name (filename without extension) to the file contents as strings.

- LocalDatasource class
  A helper that provides access to local Parquet data and loads Graph Rag configuration using the provided base_path as the root.

  Methods:
  - __init__(base_path: str)
    Initialize the LocalDatasource with the provided base path.

  - read(table: str, throw_on_missing: bool = False, columns: list[str] | None = None) -&gt; pd.DataFrame
    Read a parquet file corresponding to the given table from the local source.

  - read_settings(file: str, throw_on_missing: bool = False) -&gt; GraphRagConfig | None
    Read settings from the local source. The file parameter is unused; settings are loaded by invoking load_config with root_dir derived from the base_path.

Brief summary
- The module centralizes local data access and configuration loading for knowledge loading workflows, enabling reading of data from the local filesystem and loading of configuration necessary for Graph Rag pipelines.

## Classes

- [`LocalDatasource`](../api/classes/unified-search-app-app-knowledge-loader-data-sources-local-source-localdatasource)

## Functions

- [`load_local_prompt_config`](../api/functions/unified-search-app-app-knowledge-loader-data-sources-local-source-load-local-prompt-config)
- [`read`](../api/functions/unified-search-app-app-knowledge-loader-data-sources-local-source-read)
- [`__init__`](../api/functions/unified-search-app-app-knowledge-loader-data-sources-local-source-init)
- [`read_settings`](../api/functions/unified-search-app-app-knowledge-loader-data-sources-local-source-read-settings)

