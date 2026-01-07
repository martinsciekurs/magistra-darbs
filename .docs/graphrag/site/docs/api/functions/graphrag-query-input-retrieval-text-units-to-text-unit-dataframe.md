---
sidebar_position: 387
---

# to_text_unit_dataframe

**File:** `graphrag/query/input/retrieval/text_units.py` (lines 27-53)

## Signature

```python
def to_text_unit_dataframe(text_units: list[TextUnit]) -> pd.DataFrame
```

## Description

Convert a list of text units to a pandas DataFrame.

Args:
    text_units (list[TextUnit]): The text units to convert into a DataFrame. If the list is empty, an empty DataFrame is returned.

Returns:
    pd.DataFrame: A DataFrame where each row corresponds to a text unit. The columns are:
        - "id": the text unit's short_id
        - "text": the text of the text unit
        - any additional attribute columns derived from the first text unit's attributes keys (excluding "id" and "text"). Attribute values are converted to strings; missing attributes result in empty strings.

Raises:
    None: This function does not raise any exceptions.

## Called By

This function is called by:

- `graphrag/query/input/retrieval/text_units.py::get_candidate_text_units`

