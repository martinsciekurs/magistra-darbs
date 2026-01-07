---
sidebar_position: 641
---

# update_local_search

**File:** `unified-search-app/app/ui/sidebar.py` (lines 38-40)

## Signature

```python
def update_local_search(sv: SessionVariables)
```

## Description

Update local rag state.

Args:
    sv: SessionVariables
        The container of session variables; used to read and update the include_local_search flag from the Streamlit session state.

Returns:
    None
        The function does not return a value.

Raises:
    KeyError
        If the expected key sv.include_local_search.key is not found in st.session_state....

