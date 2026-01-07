---
sidebar_position: 600
---

# on_change

**File:** `unified-search-app/app/home_page.py` (lines 38-39)

## Signature

```python
def on_change(sv: SessionVariables)
```

## Description

Updates the current question in the session variables from the Streamlit session state.

Parameters:
    sv (SessionVariables): The session variables container; updates sv.question.value from the input.

Returns:
    None: This function does not return a value.

Raises:
    KeyError: If the key 'question_input' is not present in st.session_state.

