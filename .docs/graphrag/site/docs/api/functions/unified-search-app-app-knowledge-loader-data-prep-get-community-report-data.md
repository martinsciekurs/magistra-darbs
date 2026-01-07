---
sidebar_position: 601
---

# get_community_report_data

**File:** `unified-search-app/app/knowledge_loader/data_prep.py` (lines 60-67)

## Signature

```python
def get_community_report_data(
    _datasource: Datasource,
) -> pd.DataFrame
```

## Description

Return a dataframe with community report data from the indexed-data.

Args:
    _datasource: Datasource to read the community report data from the indexed-data.

Returns:
    A dataframe with community report data loaded from the indexed-data.

Raises:
    Exception: If the underlying data source read operation fails.

