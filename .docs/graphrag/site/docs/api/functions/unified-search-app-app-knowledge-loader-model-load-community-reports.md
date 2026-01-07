---
sidebar_position: 619
---

# load_community_reports

**File:** `unified-search-app/app/knowledge_loader/model.py` (lines 54-58)

## Signature

```python
def load_community_reports(
    _datasource: Datasource,
) -> pd.DataFrame
```

## Description

Load community report data from the indexed data source.

This function delegates to get_community_report_data to obtain a DataFrame of
community reports using the provided Datasource and returns the result.

Args:
    _datasource (Datasource): Datasource to read the community report data from the indexed data.

Returns:
    pd.DataFrame: DataFrame containing community report data loaded from the indexed data.

Raises:
    Exception: If the underlying data source read operation fails.

## Called By

This function is called by:

- `unified-search-app/app/knowledge_loader/model.py::load_model`

