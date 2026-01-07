---
sidebar_position: 638
---

# update_global_search

**File:** `unified-search-app/app/ui/sidebar.py` (lines 43-45)

## Signature

```python
def update_global_search(sv: SessionVariables)
```

## Description

Update global rag state.

Args:
    sv: SessionVariables
        The container of session variables; used to read and update the include_global_search flag from the Streamlit session state.

Returns:
    None
        The function does not return a value.

Raises:
    KeyError
        If the expected key sv.include_global_search.key is not found in st.session_state.

