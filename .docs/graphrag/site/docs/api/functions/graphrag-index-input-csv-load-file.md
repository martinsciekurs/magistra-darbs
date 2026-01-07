---
sidebar_position: 53
---

# load_file

**File:** `graphrag/index/input/csv.py` (lines 25-41)

## Signature

```python
def load_file(path: str, group: dict | None) -> pd.DataFrame
```

## Description

Asynchronously load a CSV file from storage and return it as a DataFrame.

This function reads the CSV using the configured encoding (config.encoding).
If grouping data is provided via 'group', the corresponding keys are added as new columns to every row (one column per key), rather than merging or stacking rows.

The DataFrame is then augmented by process_data_columns to include additional configured metadata columns (for example, id, text, and title) as defined by the configuration.

A creation_date column is added to all rows, with the same value derived from storage.get_creation_date(path) for the given path.

Args:
  path (str): Path to the CSV file in storage.
  group (dict | None): Optional mapping of grouping metadata. If None, treated as &#123;&#125;.

Returns:
  pd.DataFrame: Loaded CSV data with grouping columns (if provided), processed data columns, and a creation_date column added to every row.

Raises:
  Exception: If storage access, CSV parsing, or data processing fails.

## Dependencies

This function calls:

- `graphrag/index/input/util.py::process_data_columns`

