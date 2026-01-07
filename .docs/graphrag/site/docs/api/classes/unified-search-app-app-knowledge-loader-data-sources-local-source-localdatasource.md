---
sidebar_position: 138
---

# LocalDatasource

**File:** `unified-search-app/app/knowledge_loader/data_sources/local_source.py`

## Overview

LocalDatasource provides access to Parquet data stored on the local filesystem and loads Graph Rag configuration using the provided base_path as the root of the data source.

Args:
- base_path: The base directory path for local data sources. Type: str.

Attributes:
- base_path (str): The base directory path for local data sources.

Methods:
- read(table: str, throw_on_missing: bool = False, columns: list[str] | None = None) -&gt; pd.DataFrame
  Read a parquet file named "&lt;table&gt;.parquet" located under base_path.
  - Parameters:
    - table: The table name to read (without the .parquet extension).
    - throw_on_missing: If True, raise FileNotFoundError when the file does not exist.
    - columns: Optional list of column names to read from the parquet file; if None, all columns are loaded.
  - Returns:
    - A pandas DataFrame containing the data from the parquet file.
  - Raises:
    - FileNotFoundError: if the file is missing and throw_on_missing is True.
    - OSError / IOError: underlying I/O errors may propagate.

- __init__(base_path: str) -&gt; None
  Initialize the instance with the provided base_path and store internal state for data access and settings loading.

- read_settings(file: str, throw_on_missing: bool = False) -&gt; GraphRagConfig | None
  Read settings from the local source. Note: The file parameter is unused. Settings are loaded by invoking load_config with a root_dir derived from base_path.
  - Parameters:
    - file: str. Unused; present for API compatibility.
    - throw_on_missing: bool. Ignored by this implementation.
  - Returns:
    - GraphRagConfig | None: The loaded configuration, or None if not found.
  - Raises:
    - Exceptions raised by load_config may propagate.

## Methods

### `read`

```python
def read(
        self,
        table: str,
        throw_on_missing: bool = False,
        columns: list[str] | None = None,
    ) -> pd.DataFrame
```

### `__init__`

```python
def __init__(self, base_path: str)
```

### `read_settings`

```python
def read_settings(
        self,
        file: str,
        throw_on_missing: bool = False,
    ) -> GraphRagConfig | None
```

