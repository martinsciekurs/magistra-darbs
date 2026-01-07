---
sidebar_position: 67
---

# SessionVariable

**File:** `unified-search-app/app/state/session_variable.py`

## Overview

SessionVariable provides a small wrapper around Streamlit's session_state to manage a single variable with optional collision avoidance via a prefix.

Purpose:
- To store and retrieve a value associated with a unique key in st.session_state, with a configurable prefix to prevent collisions when multiple variables share the same base name.

Args:
  default: The initial/default value for the session variable.
  prefix: Optional prefix to prepend to the key to differentiate this variable from others with the same name.

Returns:
  None
  Note: __init__ initializes the instance and does not return a value.

Raises:
  None

Attributes:
  key: str. The session_state key used to access this variable. It is derived from the provided prefix and the internal variable name.
  value: Any. The current value stored in session_state for this variable. This is readable and writable; assigning a new value updates st.session_state accordingly.

__repr__:
  Returns: str. A string representation that includes both the key and the current value to aid debugging.

## Methods

### `__init__`

```python
def __init__(self, default: Any = "", prefix: str = "")
```

### `value`

```python
def value(self, value: Any) -> None
```

### `__repr__`

```python
def __repr__(self) -> Any
```

### `key`

```python
def key(self) -> str
```

