---
sidebar_position: 284
---

# unified-search-app/app/knowledge_loader/data_sources/loader.py

## Overview

Utilities to load data sources for the knowledge loader, supporting both blob and local storage.

This module provides helpers to construct dataset base paths, create the appropriate data source
object (BlobDatasource or LocalDatasource), and load dataset listings and prompts from either blob
storage or local data.

Exports
- _get_base_path(dataset: str | None, root: str | None, extra_path: str | None = None) -&gt; str
- create_datasource(dataset_folder: str) -&gt; Datasource
- load_dataset_listing() -&gt; list[DatasetConfig]
- load_prompts(dataset: str) -&gt; dict[str, str]

Functions
- _get_base_path(dataset: str | None, root: str | None, extra_path: str | None = None) -&gt; str
  Args:
    dataset: The dataset folder name, or None to omit.
    root: The root path segment, or None to omit.
    extra_path: Additional path segments separated by '/' (if provided).
  Returns:
    str: The constructed base path as a string.
  Raises:
    Exceptions that may be raised during path construction.
- create_datasource(dataset_folder: str) -&gt; Datasource
  Args:
    dataset_folder: Path to the dataset folder to load data from.
  Returns:
    A datasource instance. If blob_account_name is set, a BlobDatasource is returned; otherwise,
    a LocalDatasource configured with the base path derived from dataset_folder and local_data_root.
  Raises:
    Exceptions that may be raised during datasource creation.
- load_dataset_listing() -&gt; list[DatasetConfig]
  Returns:
    A list of DatasetConfig instances parsed from the listing file. When blob storage is configured,
    the listing is loaded from blob storage and, on error, prints the issue and returns an empty list.
- load_prompts(dataset: str) -&gt; dict[str, str]
  Args:
    dataset: The dataset name to load prompts for.
  Returns:
    dict[str, str]: The prompts configuration for the specified dataset.
  Raises:
    Exception: Propagated exceptions from underlying load operations.

## Functions

- [`_get_base_path`](../api/functions/unified-search-app-app-knowledge-loader-data-sources-loader-get-base-path)
- [`create_datasource`](../api/functions/unified-search-app-app-knowledge-loader-data-sources-loader-create-datasource)
- [`load_dataset_listing`](../api/functions/unified-search-app-app-knowledge-loader-data-sources-loader-load-dataset-listing)
- [`load_prompts`](../api/functions/unified-search-app-app-knowledge-loader-data-sources-loader-load-prompts)

