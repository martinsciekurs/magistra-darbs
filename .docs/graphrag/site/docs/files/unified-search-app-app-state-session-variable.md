---
sidebar_position: 289
---

# unified-search-app/app/state/session_variable.py

## Overview

Module for managing a single Streamlit session_state variable with optional prefix-based collision avoidance.

Overview:
- This module provides a small wrapper around Streamlit's session_state to store and retrieve a value associated with a unique key, optionally prefixed to prevent collisions when multiple variables share the same base name.

Public API:
- SessionVariable: Class that provides a simple interface to a session variable.

Key concepts and usage:
- value: Exposed as a read/write property. Access via var.value to get the current value stored under this variable's key, or assign to var.value to update or create the entry in st.session_state. The value is stored under a key derived from the provided prefix (and an internal identifier) to avoid collisions.
- key: A read-only property that returns the string key used to index st.session_state for this variable.
- __repr__(self) -&gt; str: Returns the string representation of the stored value (i.e., the value converted to a string). May raise KeyError if the key is not present in st.session_state.

Constructor:
- __init__(default: Any = "", prefix: str = ""): Create a managed session variable with a default value and an optional prefix. The prefix helps avoid collisions between variables with the same base name. Returns None.

Behavior notes and edge cases:
- Initialization ensures the underlying key exists in st.session_state with the provided default, so normal reads should not raise KeyError unless the key is manually removed.
- If the key is missing (e.g., external removal) accessing value or repr may raise KeyError.
- Prefixing helps distinguish variables with identical base names; choose prefixes carefully to avoid unintended collisions.

Example:
- sv = SessionVariable(default=0, prefix="counter_")
- sv.value = 10
- print(sv.key)  # e.g., "counter_&lt;id&gt;"
- print(sv)      # "10"

## Classes

- [`SessionVariable`](../api/classes/unified-search-app-app-state-session-variable-sessionvariable)

## Functions

- [`__init__`](../api/functions/unified-search-app-app-state-session-variable-init)
- [`value`](../api/functions/unified-search-app-app-state-session-variable-value)
- [`__repr__`](../api/functions/unified-search-app-app-state-session-variable-repr)
- [`key`](../api/functions/unified-search-app-app-state-session-variable-key)

