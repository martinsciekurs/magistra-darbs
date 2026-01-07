---
sidebar_position: 42
---

# graphrag/index/input/csv.py

## Overview

CSV input loader for Graphrag index from a storage backend.

Purpose
Utilities to load CSV inputs used by the Graphrag indexing pipeline. The module provides a convenient wrapper to fetch CSV data from a storage backend, assemble it into a single DataFrame, and apply data-column processing as defined by the input configuration and helper utilities.

Exports
- load_csv(config: InputConfig, storage: PipelineStorage) -&gt; pd.DataFrame
  Synchronously load CSV inputs from the storage location defined by the provided config. The configuration guides encoding and other reading settings. Returns a concatenated DataFrame containing the data from loaded CSV files with additional processing applied via process_data_columns.

- load_file(path: str, group: dict | None) -&gt; pd.DataFrame
  Synchronously load a single CSV file from the given path. If grouping data is provided via group, the corresponding keys are added as new columns to every row (one column per key). The resulting DataFrame is then augmented by process_data_columns to include additional configuration-derived columns.

Notes
- The functions may raise I/O related errors, encoding errors, or pandas errors for malformed CSV data.
- Empty input directories or files may yield an empty DataFrame.

Summary
The module ties together storage access, configuration-driven CSV reading, and post-load data processing to yield ready-to-use DataFrames for indexing and analysis.

## Functions

- [`load_csv`](../api/functions/graphrag-index-input-csv-load-csv)
- [`load_file`](../api/functions/graphrag-index-input-csv-load-file)

