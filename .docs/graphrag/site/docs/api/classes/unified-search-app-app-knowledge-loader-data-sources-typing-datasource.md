---
sidebar_position: 55
---

# Datasource

**File:** `unified-search-app/app/knowledge_loader/data_sources/typing.py`

## Overview

Datasource interface for knowledge loader data sources.

Purpose
Abstract base class that defines the common interface for data sources used by the knowledge loader. Concrete implementations provide reading from and writing to their underlying storage, loading configuration, and checking the presence of tables.

Key attributes
- GraphRagConfig: The configuration type used by read_settings to represent datasource settings.
- Overwrite, Append: Module-level constants representing write modes defined for write operations.

Summary
Subclasses must implement the following methods to interact with their data backends:
- read_settings(file: str) -&gt; GraphRagConfig | None
- read(table: str, throw_on_missing: bool = False, columns: list[str] | None = None) -&gt; pd.DataFrame
- __call__(table: str, columns: list[str] | None) -&gt; pd.DataFrame
- write(table: str, df: pd.DataFrame, mode: WriteMode | None = None) -&gt; None
- has_table(table: str) -&gt; bool

## Methods

### `read_settings`

```python
def read_settings(self, file: str) -> GraphRagConfig | None
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

### `__call__`

```python
def __call__(self, table: str, columns: list[str] | None) -> pd.DataFrame
```

### `write`

```python
def write(
        self, table: str, df: pd.DataFrame, mode: WriteMode | None = None
    ) -> None
```

### `has_table`

```python
def has_table(self, table: str) -> bool
```

