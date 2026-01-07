---
sidebar_position: 44
---

# graphrag/index/input/json.py

## Overview

Utilities for loading and processing JSON inputs for the GraphRag indexing pipeline.

This module provides helpers to load JSON inputs from a storage backend and to load a single JSON input file into pandas DataFrames. It uses InputConfig for configuration and PipelineStorage as the storage backend, and relies on load_files and process_data_columns to assemble and process data.

Key exports:
- load_json(config: InputConfig, storage: PipelineStorage) -&gt; pd.DataFrame: Load json inputs from a directory and return a concatenated DataFrame containing the data from loaded JSON files.
- load_file(path: str, group: dict | None) -&gt; pd.DataFrame: Load a JSON input file from storage and return it as a DataFrame, augmented with grouping keys (if any) and processed by process_data_columns.

## Functions

- [`load_json`](../api/functions/graphrag-index-input-json-load-json)
- [`load_file`](../api/functions/graphrag-index-input-json-load-file)

