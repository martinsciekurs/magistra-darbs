---
sidebar_position: 642
---

# create_side_bar

**File:** `unified-search-app/app/ui/sidebar.py` (lines 48-97)

## Signature

```python
def create_side_bar(sv: SessionVariables)
```

## Description

Create a Streamlit sidebar panel in the app to configure dataset selection, the number of suggested questions, and search options.

This function renders the following UI components inside the Streamlit sidebar:
- a selectbox labeled "Dataset" to choose a dataset (options derived from sv.datasets.value and displayed using dataset_name as the label)
- a number input labeled "Number of suggested questions" for the count
- a subheader "Search options:" followed by four toggles:
  - "Include basic RAG"
  - "Include local search"
  - "Include global search"
  - "Include drift search" 

Behavior notes:
- Uses sv as the source of keys and current values, and registers callbacks (on_change) to update state when widgets change.
- The function does not return a value (returns None) and renders directly to the UI.

Assumptions:
- sv implements the following attributes and structure:
  - sv.datasets.value is iterable of items with .key
  - sv.dataset.key is the widget key for the dataset selectbox
  - sv.suggested_questions.key is the key for the number input
  - sv.include_basic_rag.key, sv.include_local_search.key, sv.include_global_search.key, sv.include_drift_search.key are keys for the toggles
  - update_dataset, update_basic_rag, update_local_search, update_global_search, update_drift_search are defined to handle changes

Raises:
- AttributeError if any required sv attribute is missing.

