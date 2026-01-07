---
sidebar_position: 626
---

# init_search_ui

**File:** `unified-search-app/app/ui/search.py` (lines 16-27)

## Signature

```python
def init_search_ui(
    container: DeltaGenerator, search_type: SearchType, title: str, caption: str
)
```

## Description

Initialize search UI component in the specified container for the given search type.

Args:
    container: DeltaGenerator
        The DeltaGenerator container to render the UI into.
    search_type: SearchType
        The type of search UI to configure.
    title: str
        The title text to display in the UI.
    caption: str
        The caption text to display in the UI.

Returns:
    None

## Example 💡 Generated

```python
from module import init_search_ui, SearchType
import streamlit as st
container = st.container()
init_search_ui(
    container, SearchType.SIMPLE, "File search",
    "Type keywords to find files"
)
# Expected: a titled UI with a caption and session state placeholders
```

