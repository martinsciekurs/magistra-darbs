---
sidebar_position: 137
---

# SessionVariables

**File:** `unified-search-app/app/state/session_variables.py`

## Overview

SessionVariables stores and initializes per-session state for the unified search application.

Purpose:
    Manage session-scoped attributes used to track the user's search state across the app.

Attributes:
    dataset (QueryVariable): The currently selected dataset, initialized as QueryVariable("dataset", "").
    datasets (SessionVariable): The collection/state of datasets for the session, initialized to an empty list.

Constructor:
    __init__(self)
        Creates and initializes the session attributes to a consistent default state. Initializes dataset and datasets with their defaults. Seeds an initial set of suggested questions from default_suggested_questions when available.

Returns:
    None

Raises:
    Propagates exceptions raised by the initialization of the contained attributes (QueryVariable, SessionVariable).

## Methods

### `__init__`

```python
def __init__(self)
```

