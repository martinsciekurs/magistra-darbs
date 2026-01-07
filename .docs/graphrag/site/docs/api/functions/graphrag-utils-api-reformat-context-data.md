---
sidebar_position: 399
---

# reformat_context_data

**File:** `graphrag/utils/api.py` (lines 144-172)

## Signature

```python
def reformat_context_data(context_data: dict) -> dict
```

## Description

Reformats context_data for all query responses.

Reformats a dictionary of dataframes into a dictionary of lists. One list entry for each
record. Records are grouped by original dictionary keys.

Note: depending on which query algorithm is used, the context_data may not contain the same information (keys).
In this case, the default behavior will be to set these keys as empty lists to preserve a standard output format.

Args:
    context_data: dict
        A mapping from key to either a pandas DataFrame-like object with to_dict(orient='records')
        or to a dict, or to None. DataFrames are converted to a list of dictionaries representing
        records. If a value is already a dict, it is used as-is. If a key yields no records, the
        key will be left with its default empty list.

Returns:
    dict
        A dictionary containing the reformatted data. It starts with the keys
        "reports", "entities", "relationships", "claims", and "sources" initialized to empty
        lists; for input keys with data, the corresponding value is replaced with the list of
        records (or the dict if the input value was a dict).

Raises:
    None

