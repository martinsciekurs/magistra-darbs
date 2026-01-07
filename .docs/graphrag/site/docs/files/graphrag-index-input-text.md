---
sidebar_position: 45
---

# graphrag/index/input/text.py

## Overview

Utilities to load text inputs from a storage backend into pandas DataFrames. This module provides two helpers, load_text and load_file, for ingesting text data as configured by InputConfig and PipelineStorage. load_text aggregates multiple text items from the configured source into a single DataFrame; load_file retrieves a single text item and returns it as a one-row DataFrame with its metadata, optionally merged with provided grouping data.

Exports: load_text, load_file.

Details:
- load_text(config, storage) loads text inputs from the configured storage backend and returns a concatenated DataFrame containing the text content and metadata for all items. The exact columns depend on the storage metadata and the load_files logic; typical fields include an id, title, creation_date, a text column, and any additional metadata.
- load_file(path, group=None) loads a single text input from storage and returns a one-row DataFrame containing the text and its metadata; if group is provided, it is merged with the item metadata to form the row.

Notes:
- The module uses the storage backend as defined by InputConfig and relies on load_files to read file contents; terminology favors storage backend over directory.
- Error handling: implementations may raise KeyError when required metadata keys are missing; ValueError for invalid inputs; and OSError/IOError for storage access failures.

## Functions

- [`load_text`](../api/functions/graphrag-index-input-text-load-text)
- [`load_file`](../api/functions/graphrag-index-input-text-load-file)

