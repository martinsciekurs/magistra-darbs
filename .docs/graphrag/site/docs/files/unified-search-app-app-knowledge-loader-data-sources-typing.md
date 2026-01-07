---
sidebar_position: 286
---

# unified-search-app/app/knowledge_loader/data_sources/typing.py

## Overview

Typing and interface definitions for knowledge loader data sources.

This module defines the write mode constants and the Datasource abstract base
class used by the knowledge loader to interact with various data sources. It
includes method signatures for reading settings, reading data, writing data, and
checking for table existence. Concrete data sources implement these methods to
read from and write to their underlying storage and to load their configuration.

Exports:
  Overwrite (int): Write mode that overwrites existing data.
  Append (int): Write mode that appends to existing data.
  Datasource (ABC): Abstract base class defining the required interface for data sources.

Notes:
  read_settings(file: str) -&gt; GraphRagConfig | None
  read(table: str, throw_on_missing: bool = False, columns: list[str] | None = None) -&gt; pd.DataFrame
  __call__(table: str, columns: list[str] | None) -&gt; pd.DataFrame
  write(table: str, df: pd.DataFrame, mode: WriteMode | None = None) -&gt; None
  has_table(table: str) -&gt; bool

## Classes

- [`Datasource`](../api/classes/unified-search-app-app-knowledge-loader-data-sources-typing-datasource)

## Functions

- [`read_settings`](../api/functions/unified-search-app-app-knowledge-loader-data-sources-typing-read-settings)
- [`read`](../api/functions/unified-search-app-app-knowledge-loader-data-sources-typing-read)
- [`__call__`](../api/functions/unified-search-app-app-knowledge-loader-data-sources-typing-call)
- [`write`](../api/functions/unified-search-app-app-knowledge-loader-data-sources-typing-write)
- [`has_table`](../api/functions/unified-search-app-app-knowledge-loader-data-sources-typing-has-table)

