---
sidebar_position: 643
---

# update_dataset

**File:** `unified-search-app/app/ui/sidebar.py` (lines 18-25)

## Signature

```python
def update_dataset(sv: SessionVariables)
```

## Description

Update dataset from the dropdown and reinitialize related UI state.

Args:
    sv: SessionVariables
        Container holding session-related configuration, including dataset metadata and the keys used to read UI state from st.session_state. In particular, sv.dataset.key is used to retrieve the selected dataset value.

Returns:
    None

Side effects:
- Clears the Streamlit cache using st.cache_data.clear().
- Ensures st.session_state.response_lengths exists; resets it to an empty list.
- Loads the selected dataset via load_dataset(value, sv), where value is obtained as value = st.session_state[sv.dataset.key].

Notes:
- Exceptions are not handled within this function; they propagate to the caller.

