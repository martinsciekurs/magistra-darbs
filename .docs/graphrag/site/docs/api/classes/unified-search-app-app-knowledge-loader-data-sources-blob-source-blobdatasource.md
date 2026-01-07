---
sidebar_position: 15
---

# BlobDatasource

**File:** `unified-search-app/app/knowledge_loader/data_sources/blob_source.py`

## Overview

BlobDatasource provides access to knowledge data stored in Azure Blob Storage, enabling reading Parquet tables and graphrag configurations used by the knowledge loader. It connects to a configured Azure Blob container using the provided database identifier to locate data and settings.

Args:
    database (str): The database identifier used to access the blob storage. This maps to a logical namespace within the configured container and determines where data and settings for this knowledge domain are stored.

Attributes:
    database (str): The database identifier used to access the blob storage.

Methods:
    read(table, throw_on_missing=False, columns=None) -&gt; pd.DataFrame
        Read a Parquet table from blob storage.

        Args:
            table (str): The table name to read (without the .parquet extension).
            throw_on_missing (bool): If True, raise FileNotFoundError when the blob does not exist.
            columns (list[str] | None): Optional subset of columns to load; if None, load all columns.

        Returns:
            pd.DataFrame: A DataFrame containing the data from the Parquet file.

        Raises:
            FileNotFoundError: If the table file does not exist and throw_on_missing is True.
            Azure-related errors: Authentication/permission/network-related errors may be raised.

    read_settings(file, throw_on_missing=False) -&gt; GraphRagConfig | None
        Read graphrag configuration settings from a blob container.

        Args:
            file (str): The blob file name containing the graphrag settings.
            throw_on_missing (bool): If True, raise FileNotFoundError when the settings file does not exist.

        Returns:
            GraphRagConfig | None: The graphrag configuration loaded from the file, or None if not found.

        Raises:
            FileNotFoundError: If the file is missing and throw_on_missing is True.
            YAML parsing errors or Azure-related errors may occur.

Notes:
    - Requires Azure credentials with access to the storage account and container. Uses DefaultAzureCredential to obtain credentials and connects via BlobServiceClient/ContainerClient.

## Methods

### `__init__`

```python
def __init__(self, database: str)
```

### `read`

```python
def read(
        self,
        table: str,
        throw_on_missing: bool = False,
        columns: list[str] | None = None,
    ) -> pd.DataFrame
```

### `read_settings`

```python
def read_settings(
        self,
        file: str,
        throw_on_missing: bool = False,
    ) -> GraphRagConfig | None
```

