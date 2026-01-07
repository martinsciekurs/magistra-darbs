---
sidebar_position: 640
---

# update_drift_search

**File:** `unified-search-app/app/ui/sidebar.py` (lines 33-35)

## Signature

```python
def update_drift_search(sv: SessionVariables)
```

## Description

Update drift rag state.

Args:
    sv: SessionVariables
        The container of session variables; used to read and update the include_drift_search flag from the Streamlit session state.

Returns:
    None
        The function does not return a value.

Raises:
    KeyError
        If the expected key sv.include_drift_search.key is not found in st.session_state.

