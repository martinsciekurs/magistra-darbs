---
sidebar_position: 56
---

# load_file

**File:** `graphrag/index/input/json.py` (lines 25-45)

## Signature

```python
def load_file(path: str, group: dict | None) -> pd.DataFrame
```

## Description

Asynchronously load a JSON input file from storage and return it as a DataFrame.

Args:
  path (str): Path to the JSON file.
  group (dict | None): Optional grouping metadata to merge with the item. If None, an empty dict is used.

Returns:
  pd.DataFrame: DataFrame loaded from the JSON content, augmented with grouping keys (if any), processed by process_data_columns, and annotated with a creation_date column for each row.

Raises:
  json.JSONDecodeError: If the loaded content cannot be decoded as JSON.

## Dependencies

This function calls:

- `graphrag/index/input/util.py::process_data_columns`

