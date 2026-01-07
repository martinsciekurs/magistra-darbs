---
sidebar_position: 596
---

# load_dataset

**File:** `unified-search-app/app/app_logic.py` (lines 51-60)

## Signature

```python
def load_dataset(dataset: str, sv: SessionVariables)
```

## Description

Load the selected dataset and initialize related session state. This function updates several fields on the session variables container (sv) and, when possible, loads the corresponding data source and knowledge model.

Args:
- dataset (str): The dataset key to load. This is a key from sv.datasets.value, not a UI element.
- sv (SessionVariables): The session variables container that will be updated in place with the selected dataset's metadata and configuration, including sv.dataset.value, sv.dataset_config.value, sv.datasource.value, and sv.graphrag_config.value. If a matching dataset configuration is found, a data source is created from its path and the graphrag settings are read from that source; the function then calls load_knowledge_model(sv) to populate the knowledge model.

Returns:
- None

Notes:
- If the dataset key is not found in sv.datasets.value (i.e., sv.dataset_config.value becomes None), the function will not create a data source, will not read settings, and will not load the knowledge model.
- This function may raise exceptions originating from create_datasource or read_settings (depending on the dataset path and settings file) or from load_knowledge_model, if any of those operations fail.
- The dataset parameter refers to a dataset key, not a user interface element.

## Dependencies

This function calls:

- `unified-search-app/app/app_logic.py::load_knowledge_model`

## Called By

This function is called by:

- `unified-search-app/app/app_logic.py::initialize`

