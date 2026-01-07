---
sidebar_position: 288
---

# unified-search-app/app/state/query_variable.py

## Overview

Module for synchronizing a single URL query parameter with a Streamlit session_state entry.

This module exposes the QueryVariable class, which maintains a two-way linkage between a URL query parameter and a Streamlit session_state entry. It reads the initial value for a given key from the URL query string when available; if the key is not present, it uses the provided default. When reading from the query string, the value is normalized to lowercase to support case-insensitive URLs. When the value is updated, the session_state entry is updated and the URL query parameter is set to the lowercase string representation of the value.

Exports:
- QueryVariable: Class that manages a single URL query parameter and its corresponding session_state entry.

## Classes

- [`QueryVariable`](../api/classes/unified-search-app-app-state-query-variable-queryvariable)

## Functions

- [`__init__`](../api/functions/unified-search-app-app-state-query-variable-init)
- [`key`](../api/functions/unified-search-app-app-state-query-variable-key)
- [`value`](../api/functions/unified-search-app-app-state-query-variable-value)

