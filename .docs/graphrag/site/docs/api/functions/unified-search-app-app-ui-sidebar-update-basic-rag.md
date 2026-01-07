---
sidebar_position: 636
---

# update_basic_rag

**File:** `unified-search-app/app/ui/sidebar.py` (lines 28-30)

## Signature

```python
def update_basic_rag(sv: SessionVariables)
```

## Description

Update basic rag state.

Args:
    sv: SessionVariables
        The container of session variables; used to read and update the include_basic_rag flag from the Streamlit session state.

Returns:
    None
        The function does not return a value.

Raises:
    KeyError
        If the expected key sv.include_basic_rag.key is not found in st.session_state.

## Example 💡 Generated

```python
from module import update_basic_rag
import streamlit as st
sv = type('S', (), {})()
sv.include_basic_rag = type('V', (), {})()
sv.include_basic_rag.key = 'include_basic_rag'
sv.include_basic_rag.value = False
st.session_state['include_basic_rag'] = True
update_basic_rag(sv)  # expected: True
```

