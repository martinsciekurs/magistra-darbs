---
sidebar_position: 620
---

# load_text_units

**File:** `unified-search-app/app/knowledge_loader/model.py` (lines 70-72)

## Signature

```python
def load_text_units(dataset: str, _datasource: Datasource) -> pd.DataFrame
```

## Description

Load text units from the specified dataset and data source.

This function delegates to get_text_unit_data to retrieve a DataFrame containing text unit records. It returns a DataFrame, not a list of objects.

Args:
    dataset: str The dataset identifier.
    _datasource: Datasource The data source to read text units from.

Returns:
    pd.DataFrame: A DataFrame containing the text unit records from the indexed data.
    The exact columns reflect the text unit schema defined by get_text_unit_data.

Raises:
    Exception: If reading from the data source or processing fails.

## Called By

This function is called by:

- `unified-search-app/app/knowledge_loader/model.py::load_model`

