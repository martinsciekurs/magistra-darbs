---
sidebar_position: 46
---

# graphrag/index/input/util.py

## Overview

Utilities for loading and processing input data for GraphRag indexing.

This module exposes two helpers used by the input data pipeline:
- load_files(loader, config, storage): Load files from storage asynchronously using the provided loader and concatenate the results into a single pandas DataFrame. The loader is awaited for each file and should be compatible with pandas.concat. Failures are logged and the corresponding file is skipped rather than raised.
- process_data_columns(documents, config, path): Process configured data columns of a DataFrame by augmenting it with id, text, and title columns according to the provided configuration. Warnings are logged if a configured text or title column is not found in the data. The function mutates the input DataFrame and returns it.

Key exports: load_files, process_data_columns.

## Functions

- [`load_files`](../api/functions/graphrag-index-input-util-load-files)
- [`process_data_columns`](../api/functions/graphrag-index-input-util-process-data-columns)

