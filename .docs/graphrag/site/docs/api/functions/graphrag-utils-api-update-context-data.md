---
sidebar_position: 398
---

# update_context_data

**File:** `graphrag/utils/api.py` (lines 175-247)

## Signature

```python
def update_context_data(
    context_data: Any,
    links: dict[str, Any],
) -> Any
```

## Description

Update context data with index_name and index_id fields derived from the links mapping.

Args:
    context_data (dict[str, pandas.DataFrame]): The context data to update. Each value should be a DataFrame containing records with an 'id' field and other relevant columns. The dict's keys typically include 'reports', 'entities', 'relationships', 'claims', and 'sources'.
    links (dict[str, Any]): A dictionary of links to the original dataframes. Expected to contain the following mappings:
        - 'community_reports': dict-like mapping int(id) -&gt; &#123;'index_name', 'id'&#125;
        - 'entities': dict-like mapping int(id) -&gt; &#123;'index_name', 'id'&#125;
        - 'relationships': dict-like mapping int(id) -&gt; &#123;'index_name', 'id'&#125;
        - 'covariates': dict-like mapping int(id) -&gt; &#123;'index_name', 'id'&#125;
        - 'text_units': dict-like mapping int(id) -&gt; &#123;'index_name', 'id'&#125;

Returns:
    dict[str, list[dict]]: The updated context data. For each key in the input, the function returns a list of dictionaries representing the records augmented with:
        - index_name and index_id based on the provided links
        - Additional key-specific transformations (e.g., 'entity' trimmed to the portion before the first dash for 'entities', 'source' and 'target' trimmed for 'relationships', etc.)

Raises:
    KeyError: If required keys are missing in the links dictionary or if expected fields are missing in a context_data entry (e.g., missing 'id').
    TypeError: If context_data is not a dict[str, pandas.DataFrame] or if a value does not support to_dict(orient='records').
    ValueError: If an entry['id'] cannot be cast to int.

## Called By

This function is called by:

- `graphrag/api/query.py::multi_index_global_search`
- `graphrag/api/query.py::multi_index_local_search`
- `graphrag/api/query.py::multi_index_drift_search`

