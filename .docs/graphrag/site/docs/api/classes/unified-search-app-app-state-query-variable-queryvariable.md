---
sidebar_position: 141
---

# QueryVariable

**File:** `unified-search-app/app/state/query_variable.py`

## Overview

Manages a single URL query parameter and its corresponding Streamlit session_state entry.

Purpose:
  Maintain a two-way linkage between a URL query parameter and a Streamlit session_state entry. It reads the initial value from the URL query string when available; if the key is not present, it uses the provided default. When reading from the query string, the value is normalized to lowercase to support case-insensitive URLs.

Key attributes:
  key: The session_state key associated with this variable (derived from the provided key parameter).

Args:
  key: The URL query parameter key and the session_state key for this variable.
  default: The default value to use if the key is not present in the URL. Can be None.

Returns:
  None

Raises:
  None

## Methods

### `__init__`

```python
def __init__(self, key: str, default: Any | None)
```

### `key`

```python
def key(self) -> str
```

### `value`

```python
def value(self, value: Any) -> None
```

