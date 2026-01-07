---
sidebar_position: 290
---

# unified-search-app/app/state/session_variables.py

## Overview

Unified session state container for the unified search application.

Purpose:
Provide a per-session container of attributes that track the user's search state across the app. The SessionVariables class initializes default session values to ensure a consistent starting point for a new session.

Exports:
- SessionVariables: Class that stores and initializes per-session state for the unified search application.

Classes:
- SessionVariables:
  Stores and initializes per-session state for the unified search application.

  Attributes:
    dataset (QueryVariable): The currently selected dataset for the session, initialized as QueryVariable("dataset", "")
    datasets (list): The collection/state of datasets for the session, initialized as an empty list

Initialization:
__init__(self) -&gt; None:
  Initialize the per-session attributes with defaults:
    dataset = QueryVariable("dataset", "")
    datasets = []

## Classes

- [`SessionVariables`](../api/classes/unified-search-app-app-state-session-variables-sessionvariables)

## Functions

- [`__init__`](../api/functions/unified-search-app-app-state-session-variables-init)

