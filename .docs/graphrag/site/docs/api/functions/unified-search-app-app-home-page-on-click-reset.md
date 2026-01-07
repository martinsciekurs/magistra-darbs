---
sidebar_position: 599
---

# on_click_reset

**File:** `unified-search-app/app/home_page.py` (lines 33-36)

## Signature

```python
def on_click_reset(sv: SessionVariables)
```

## Description

Reset the relevant session variables on reset action.

Args:
    sv (SessionVariables): The session variables container; resets sv.generated_questions.value to [], sv.selected_question.value to '', and sv.show_text_input.value to True.

Returns:
    None: This function does not return a value.

