---
sidebar_position: 603
---

# get_text_unit_data

**File:** `unified-search-app/app/knowledge_loader/data_prep.py` (lines 51-56)

## Signature

```python
def get_text_unit_data(dataset: str, _datasource: Datasource) -> pd.DataFrame
```

## Description

Return a dataframe containing text units (i.e. chunks of text from raw documents) from the indexed data.

Args:
    dataset: str The dataset identifier.
    _datasource: Datasource The data source to read text units from.

Returns:
    pd.DataFrame: A dataframe containing the text unit records from the indexed data.

Raises:
    Exception: If reading from the datasource or processing fails.

