---
sidebar_position: 28
---

# graphrag/config/models/storage_config.py

## Overview

Storage configuration model for GraphRAG storage backends.

This module defines StorageConfig, a Pydantic model that encapsulates storage-related
settings for GraphRAG backends, including the storage type and the base directory for
local storage. It reads defaults from graphrag_config_defaults and uses StorageType to
determine behavior. A validator is provided to normalize the base_dir when using local
storage.

Public API
- StorageConfig: Pydantic model managing storage configuration, including the storage type and the base directory for local storage.
- validate_base_dir: field validator that normalizes base_dir to a filesystem path string for local storage; for other storage types, the input value is returned unchanged. Args: cls (type): The class that defines the validator. value (Any): The input value. info: Additional contextual information about the field. Returns: The normalized or original value depending on the storage type.

## Classes

- [`StorageConfig`](../api/classes/graphrag-config-models-storage-config-storageconfig)

## Functions

- [`validate_base_dir`](../api/functions/graphrag-config-models-storage-config-validate-base-dir)

